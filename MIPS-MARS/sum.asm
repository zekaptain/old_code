
# a MIPS program to add 1 to entered number, returning the sum

	.data
	
enterednum:	.asciiz "Please enter a non-negative number: "
sumis:		.asciiz "The sum is "

	.text
#get number that will be the upper limit of the loop
# prompt for integer num1 input 
	addi	$v0, $zero, 4
	la	$a0, enterednum
	syscall

# get integer input from user 
	addi	$v0, $zero, 5
	syscall

# save number
	add	$s1, $zero, $v0

# $s0 will hold the sum
	addi $s0, $zero, 0
	
# store 1 in $s2
	addi $s2, $zero, 1

#loop from 1 to upper limit of loop, adding them together				
loop:	bgt $s2, $s1, done
	add	$s0, $s0, $s2
	addi	$s2, $s2, 1
	j	loop
done:	addi	$v0, $zero, 4
	la	$a0, sumis	#displays "The sum is "
	syscall
	
	#now display the sum
	add	$a0, $zero, $s0
	addi	$v0, $zero, 1
	syscall
	
	# halt cleanly
	li	$v0, 10 
	syscall

	
