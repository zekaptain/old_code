		.data

Space:		.asciiz " "
Carret: 	.asciiz "\n"
Option0:	.asciiz "\nOptions:\n0) Quit\n"
Option1:	.asciiz "1) Display all positive entries\n"
Option2:	.asciiz "2) Insert number after the other positive numbers\n"
Option3:	.asciiz "3) Insert number before the other positive numbers\n"
Option4:	.asciiz "4) Swap the greatest positive entry with the last positive entry\n"
Option5:	.asciiz "5) Swap the least positive entry with the first positive entry\n"
Option6:	.asciiz "6) Compute and display the sum of the positive entries\n"
SelectMes:	.asciiz "Select option: "
InputMes:	.asciiz "Input a number between 1 and 999: "
SumMes:		.asciiz "The sum of the entries is: "
ErrorMes:	.asciiz "\nNo. Just No. Try again.\n"

# think of both of these as arrays, though SIZE only contains one number: 
Size:		.word 6
Array:		.word 0,0,0,0,0,0

		.text

#initialize global variables
	addi	$s2, $zero, 999			# initialize greatest value
	addi	$s3, $zero, 1			# initialize smallest value
	
# display menu 		
main:	
	addi	$v0, $zero, 4		
	la	$a0, Option0
	syscall
	la	$a0, Option1 
	syscall
	la	$a0, Option2
	syscall
	la	$a0, Option3
	syscall
	la	$a0, Option4
	syscall
	la	$a0, Option5
	syscall
	la	$a0, Option6
	syscall		
	la	$a0, SelectMes
	syscall
	addi	$v0, $zero, 5 			# get menu option
	syscall
	add	$s1, $zero, $v0			# $s1 - menu option
	bne	$s1, $zero, displayPos		# quit if input is 0
	addi	$v0, $zero, 10 			# terminate program
	syscall

# Option 1
displayPos:
	addi	$s1, $s1, -1			# decrement Menu counter
	bne	$s1, $zero, insertAfter
	beqz 	$s4, error			# give error if Array is empty
	add	$t0, $zero, $s4			# initialize loop counter to number of positive entries in Array
	addi	$t3, $zero, 0			# initialize Array index
	
	addi	$v0, $zero, 4			# make it look better
	la	$a0, Carret
	syscall
printArray:
	lw	$a0, Array($t3)			# loop: get Array entry and display it 
	addi	$v0, $zero, 1
	syscall
	la	$a0, Space			# separate numbers with spaces
	addi	$v0, $zero, 4
	syscall
	addi	$t3, $t3, 4			# update array index (times four) 
	addi	$t0, $t0, -1			# decrement loop counter 
	bne	$t0, $zero, printArray		# maybe loop back 
	
	addi	$v0, $zero, 4			# make it look better
	la	$a0, Carret
	syscall
	j	main
	
# Option 2	
insertAfter:
	addi	$s1, $s1, -1			# decrement Menu counter
	bne	$s1, $zero, insertBefore
	addi	$v0, $zero, 4			# ask for input
	la	$a0, InputMes
	syscall
	addi	$v0, $zero, 5			# get user input
	syscall
	add	$t1, $zero, $v0			# $t1 - stores user input
	bgt	$t1, $s2, error			# error if > 999
	blt	$t1, $s3, error			# error if < 1
	sw	$t1, Array($s0)			# put number into Array
	addi	$s0, $s0, 4			# increment Array index
	addi	$s4, $s4, 1			# increment positive number counter
	addi	$s1, $s1, 1
	j	displayPos
	
# Option 3	
insertBefore:
	addi	$s1, $s1, -1			# decrement Menu counter
	bne	$s1, $zero, swapLast
	addi	$v0, $zero, 4			# ask for input
	la	$a0, InputMes
	syscall
	addi	$v0, $zero, 5			# get user input
	syscall
	add	$t1, $zero, $v0			# $t1 - stores user input
	bgt	$t1, $s2, error			# error if > 999
	blt	$t1, $s3, error			# error if < 1
	addi	$t2, $s0, -4			# set $t2 to index before $t3
	add	$t3, $zero, $s0			# set $t3 to first 0 in Array
processBefore:
	lw	$t4, Array($t2)			# $t4 - last positive entry
	sw	$t4, Array($t3)			# move last positive entry one to the right
	addi	$t2, $t2, -4			# decrement index
	addi	$t3, $t3, -4			# decrement index
	bne	$t3, $zero, processBefore	# branch if $t3 is not at first index
	sw	$t1, Array($t3)			# place user input at beginning of Array
	addi	$s0, $s0, 4			# increment Array index
	addi	$s4, $s4, 1			# increment positive number counter
	addi	$s1, $s1, 1
	j	displayPos
	
# Option 4	
swapLast:
	addi	$s1, $s1, -1			# decrement Menu counter
	bne	$s1, $zero, swapFirst
	beqz 	$s4, error			# give error if Array is empty
	addi 	$t6, $s0, -4			# put index at last number
	lw	$t5, Array($t6)			# put last number in $t5
	add	$t3, $zero, $s3			# initialize $t3 to 1 (greatest)
	addi	$t4, $zero, 0			# register to hold index of largest number
	add	$t0, $zero, $s4			# initialize loop counter to number of positive entries in Array	
	addi	$t1, $zero, 0			# initialize Array index
	
findGreatest:
	beq	$t0, 0, processSwapLast		# branch at the end of Array
	lw	$t2, Array($t1)			# retrieve Array value at $t1
	bgt	$t2, $t3, greaterThan		# branch if new greatest
	addi	$t1, $t1, 4			# update Array indexing register
	addi	$t0, $t0, -1			# decrement loop counter	
	j	findGreatest
	
greaterThan:
	add	$t3, $zero, $t2			# biggest number stored in $t3
	add	$t4, $zero, $t1			# register to hold index of biggest number	
	addi	$t1, $t1, 4			# update Array indexing register
	addi	$t0, $t0, -1			# decrement loop counter
	j	findGreatest

processSwapLast:
	addi	$t1, $t1, -4			# put index back at last spot	
	sw	$t3, Array($t1)			# put largest number at last index
	sw	$t5, Array($t4)			# put last number where largest was
	addi	$s1, $s1, 1
	j	displayPos

# Option 5	
swapFirst:
	addi	$s1, $s1, -1			# decrement Menu counter
	bne	$s1, $zero, displaySum
	beqz 	$s4, error			# give error if Array is empty
	lw 	$t5, Array($zero)		# put first number in $t5
	add 	$t3, $zero, $s2			# initialize $t3 to 999 (lowest)
	addi	$t4, $zero, 0			# register to hold index of smallest number
	add	$t0, $zero, $s4			# initialize loop counter to number of positive entries in Array	
	addi	$t1, $zero, 0			# initialize Array index

findLowest:
	beq	$t0, 0, processSwapFirst	# branch at the end of Array
	lw	$t2, Array($t1)			# retrieve Array value at $t1
	blt	$t2, $t3, lessThan		# branch if new lowest
	addi	$t1, $t1, 4			# update Array indexing register
	addi	$t0, $t0, -1			# decrement loop counter	
	j	findLowest

lessThan:
	add	$t3, $zero, $t2			# smallest number stored in $t3
	add	$t4, $zero, $t1			# register to hold index of smallest number	
	addi	$t1, $t1, 4			# update Array indexing register
	addi	$t0, $t0, -1			# decrement loop counter
	j	findLowest
	
processSwapFirst:		
	sw	$t3, Array($zero)		# put smallest number at index 0
	sw	$t5, Array($t4)			# put first number where smallest was
	addi	$s1, $s1, 1
	j	displayPos
	
# Option 6
displaySum:
	addi	$s1, $s1, -1
	bne	$s1, $zero, error
	beqz 	$s4, error			# give error if Array is empty
	add	$t0, $zero, $s4			# initialize loop counter to number of positive entries in Array
	addi	$t1, $zero, 0			# initialize Array index
	addi	$t3, $zero, 0			# initialize $t3 for sum
sumEntries:
	lw	$t2, Array($t1)			# load entry into $t2
	add	$t3, $t3, $t2			# accumulate total sum in $t3
	addi	$t0, $t0, -1			# decrement loop counter
	addi	$t1, $t1, 4			# increment index register
	bne	$t0, $zero, sumEntries		# loop back
	
	addi	$v0, $zero, 4			# make it look better
	la	$a0, Carret
	syscall
	
	addi	$v0, $zero, 4			# print Sum Message
	la	$a0, SumMes
	syscall
	
	addi	$v0, $zero, 1			# print sum
	add	$a0, $zero, $t3
	syscall
	
	addi	$v0, $zero, 4			# make it look better
	la	$a0, Carret
	syscall
	j	main

error:	
	addi	$v0, $zero, 4			# report error - bad choice 
	la	$a0, ErrorMes
	syscall
	j	main				# start over 
	
