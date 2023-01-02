
# be CLEAR with what you do with each and every register

# plan for this problem

# enter two numbers and sum all the numbers b/w them, inclusively

# put the entered number someplace, store it in $s1 initially

# $s2 - hold second number intitially 

# $s0 -- keeps track of adding/summing "running sum" -- initialize this first

# w/ this problem, doesn't matter if you change $s1. 
# pseudocode:
# get #'s from user, store in $s1 and $s2
# initialize $s0 -- addi $s0, $zero, 0 OR add $s0, $zero, $zero OR li $s0, 0
# if $s1 > $s2, display error message & start over
# otherwise, start a loop
# add $s1 to $s0, then increment $s1 while $s1 is <= $s2 (if time to stop loop ($s1 > $s2), branch over the loop)
# loop:		bgt $s1, $s2, done //branch if greater than -- actual code
#		add $s0, $s0, $s1 //take current running sum, add what's in s1, put it in s0
#		addi $s1, $s1, 1 //increment s1 
#
#		j loop
# done:		

#this program determines the sum from lowest entered number to highest entered number
	.data
	
num1:	.asciiz "Enter a smallish number: "
num2:	.asciiz "Enter a number larger than the previous number: "
sumis:	.asciiz "The sum is "


	.text
# prompt for integer num1 input 
	addi	$v0, $zero, 4
	la	$a0, num1
	syscall

# get integer input from user 
	addi	$v0, $zero, 5
	syscall

# save number
	add	$s1, $zero, $v0
		
# prompt for integer num2 input 
	addi	$v0, $zero, 4
	la	$a0, num2
	syscall

# get integer input from user 
	addi	$v0, $zero, 5
	syscall

# save number
	add	$s2, $zero, $v0

#store 0 in $s0
	addi	$s0, $zero, 0
	
loop:	bgt	$s1, $s2, done	
	add	$s0, $s0, $s1
	addi	$s1, $s1, 1
	j	loop
done:	addi	$v0, $zero, 4
	la	$a0, sumis	#displays "The sum is "
	syscall
	
	#now display the sum
	add	$a0, $zero, $s0
	addi	$v0, $zero, 1
	syscall
	
	#halt cleanly
	li	$v0, 10 
	syscall
