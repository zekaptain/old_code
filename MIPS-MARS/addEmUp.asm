#
# customary to have a procedure receive info via the a registers ($a0, $a1) 
# and/or the stack
# it is also customary for it to return info via the v registers ($v0, $v1)
# 

	.data

numOfNums:	.asciiz "Please enter the number of numbers you will enter"
enterednum:	.asciiz "Enter a number"
	
	.text


main:
#get number that will be the num of nums
# prompt for integer num1 input 
	li	$v0, 4
	la	$a0, numOfNums
	syscall

# get integer input from user 
	li	$v0, 5
	syscall

# save number in $s0
	add	$s0, $zero, $v0
# loads $s0 in $t0
	li	$t0, $s0

loop:
#prompt for integer input 
	li	$v0, 4
	la	$a0, enterednum
	syscall
	
# get integer input from user 
	li	$v0, 5
	syscall
	
# save number in stack
	addi	$sp, $sp, -4
	sw 	$v0, ($sp)
# decrement counter
	addi 	$t0, $t0, -1
	bne	$t0, $zero, loop
	
# put number onto stack
	addi	$sp, $sp, -4
	sw 	$s0, ($sp)
	jal	addThemUp
# display the sum
	add	$a0, $v0, $zero
	li	$v0, 1
	syscall
# kill program cleanly
	li	$v0, 10
	syscall

addThemUp:
# add up the entered numbers
	lw	$t0, ($sp)
	addi	$sp, $sp, 4
	li	$v0, 0
loop2:	beq	$t0, $zero, done
# pop off stack
	lw	$t1, ($sp)
# increment sp counter
	addi	$sp, $sp, 4
# add what's in t1 to v0 (sum)
	add	$v0, $v0, $t1
# decrement counter
	addi	$t0, $t0, -1
# jump to loop
	j	loop
	
done2:	jr	$ra



