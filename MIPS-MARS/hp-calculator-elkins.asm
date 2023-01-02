	.data

ret:      	.asciiz	"\n"

tabin:    	.asciiz "\t\t\t"

welcome:  	.asciiz "\nWelcome to old HP-style calculator.\n"

options:  	.asciiz "Options: 0=enter, 1=add, 2=sub, 3=mul, 4=div, 5=quit\n"

prompt:   	.asciiz "Choose an option: "

enter:    	.asciiz "Enter an integer: "

byenow:   	.asciiz "\nBye now!\n\n" 

size:     	.word  4

array:    	.space 1024

	.text


#display welcome
	li	$v0, 4
	la	$a0, welcome
	syscall

	lw	$s0, size($zero) 	#keep array length in $s0
	
	add	$t0, $zero, $s0		# $t0 = loop counter (count down)
	addi	$t1, $zero, 0		# $t1 is array index times four
storeZeros:
	#store 0 in array at position $t1
	addi	$s1, $zero, 0
	sw	$s1, array($t1)
	
	addi	$t1, $t1, 4		# update array index (times four) 
	addi	$t0, $t0, -1		# decrement loop counter 
	bne	$t0, $zero, storeZeros	# maybe loop back if counter isn't zero yet

	#load zeros into array of size 4
	lw	$s0, size($zero) 	#keep array length in $s0
	
	add	$t0, $zero, $s0		# $t0 = loop counter (count down)
	addi	$t1, $zero, 0		# $t1 is array index times four
	
	jal	showNumbers
	
main:
#loop through this -- if 0, continue on in this main function. 1, call add function. so on.

#display options:
	li	$v0, 4
	la	$a0, options
	syscall
#display prompt:
	li	$v0, 4
	la	$a0, prompt
	syscall

#get input from user
	li	$v0, 5
	syscall
#store integer into some variable
#use this number to compare to 1, 2, 3, 4, 5
	add 	$s4, $zero, $v0

#if input = 1, call add function on two ints in array.
	beq	$s4,1,doAdd
#if input = 2, call subtract
	beq	$s4,2,doSub
#if input = 3, call multiply
	beq	$s4,3,doMul
#if input = 4, call divide
	beq	$s4,4,doDiv
#if input = 5, call quit cleanly function
	beq	$s4,5,endCleanly
#if input = 0, store input into $a0, pass to insert function
#ask for integer input:
	li	$v0, 4
	la	$a0, enter
	syscall
#get input from user
	li	$v0, 5
	syscall
#store this into $a0
	add	$a0,$zero,$v0
#jump to insert function
	jal	insert
	
#load numbers into array of size 4
	lw	$s0, size($zero) 	#keep array length in $s0
	
	add	$t0, $zero, $s0		# $t0 = loop counter (count down)
	addi	$t1, $zero, 0		# $t1 is array index times four
	
	jal	showNumbers
#loop back to main
	j	main
	
showNumbers:
	la	$a0, tabin		# tab three times before displaying number
	addi	$v0, $zero, 4
	syscall
	
	lw	$a0, array($t1)		# loop: get array entry and display it 
	addi	$v0, $zero, 1
	syscall
	la	$a0, ret		# separate numbers with newline 
	addi	$v0, $zero, 4
	syscall
	addi	$t1, $t1, 4		# update array index (times four) 
	addi	$t0, $t0, -1		# decrement loop counter 
	bne	$t0, $zero, showNumbers	# maybe loop back if counter isn't zero yet
	
	jr	$ra


shiftDown:
#shift the second number into top number, have zero take up last spot in array
#store s7 in array at position $t1
	
	sw	$s7, array($t1)
	addi	$t1, $t1, 4		# update array index (times four)
	addi	$t2, $t1, 4		# find the next next array index
	lw	$s7, array($t2)				# store next item in temp variable to pass into current variable 
	addi	$t0, $t0, -1		# decrement loop counter 
	bne	$t0, $zero, shiftDown	# maybe loop back if counter isn't zero yet

	jr	$ra

shiftUp:
#shift each number in the array up one
	lw	$s5, array($t1)
	addi	$t1, $t1, 4		# update array index (times four)
	sw	$s5, array($t1) 
	addi	$t1, $t1, -8		# find the next next array index, one down from previous
	addi	$t0, $t0, -1		# decrement loop counter 
	bne	$t0, $zero, shiftDown	# maybe loop back if counter isn't zero yet
	#return to insert
	jr	$ra

insert:
#will call shift up (jal -- jump and link)
#need to pop current $ra onto stack
# save number in stack
	addi	$sp, $sp, -4
	sw 	$ra, ($sp)
#make $t1 12 for the shiftUp loop that shifts all numbers up one starting with last number
	addi	$t1,$zero,12
#make counter as well
	lw	$s0, size($zero) 	# keep array length in $s0
	add	$t0, $zero, $s0		# $t0 = loop counter (count down) 
	
	jal	shiftUp
	addi	$t1, $zero, 0
	sw	$a0, array($t1)

#after shifting, insert $a0 into first point in array	

#pop number from stack into $ra
	lw	$ra, ($sp)
# increment sp counter
	addi	$sp, $sp, 4
#after inserting, return to main
	jr	$ra
	

doAdd:
#add together the bottom two numbers of the array
#will call shift down

	addi	$t1, $zero, 0		# $t1 is array index times four
	addi	$s5, $zero, 0
	lw	$s5, array($t1)
	addi	$t1, $t1, 4		# update array index (times four)
	addi	$s6, $zero, 0
	lw	$s6, array($t1)
	add	$s7, $s5, $s6 
	
	#make $t1 0 again for the shiftDown loop that shifts all numbers down one
	addi	$t1,$zero,0
	#make counter as well
	lw	$s0, size($zero) 	#keep array length in $s0
	add	$t0, $zero, $s0		# $t0 = loop counter (count down)
	jal	shiftDown
	
	j	main
	

doSub:
#subtract the bottom two numbers of the array
#will call shift down
	addi	$t1, $zero, 0		# $t1 is array index times four
	addi	$s5, $zero, 0
	lw	$s5, array($t1)
	addi	$t1, $t1, 4		# update array index (times four)
	addi	$s6, $zero, 0
	lw	$s6, array($t1)
	sub	$s7, $s5, $s6 
	
	jal	shiftDown
	
	j	main
doMul:
#multiply the bottom two numbers of the array
#will call shift down
	addi	$t1, $zero, 0		# $t1 is array index times four
	addi	$s5, $zero, 0
	lw	$s5, array($t1)
	addi	$t1, $t1, 4		# update array index (times four)
	addi	$s6, $zero, 0
	lw	$s6, array($t1)
	mult	$s5,$s6
	mflo	$s7
	
	jal	shiftDown
	
	j	main

doDiv:
#multiply the bottom two numbers of the array
#will call shift down
	addi	$t1, $zero, 0		# $t1 is array index times four
	addi	$s5, $zero, 0
	lw	$s5, array($t1)
	addi	$t1, $t1, 4		# update array index (times four)
	addi	$s6, $zero, 0
	lw	$s6, array($t1)
	div	$s5,$s6
	mflo	$s7
	
	jal	shiftDown
	
	j	main


endCleanly:
	li	$v0, 10
	syscall





