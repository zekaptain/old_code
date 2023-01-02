# Modified example from Prof. Urness to test if number is positive or negative 
# Revised again 9/22/2010

	.data

HEL:   .asciiz "Please enter a number (0 to quit): "
BYE:   .asciiz "Goodbye\n"
POS:   .asciiz " is positive\n"
NEG:   .asciiz " is negative\n"

		.text

Main:
# prompt for integer input 
		addi	$v0, $zero, 4
		la	$a0, HEL
		syscall

# get integer input from user 
		addi	$v0, $zero, 5
		syscall

# quit if zero 
		beq	$v0, $zero, Goodbye

# save number
		add	$s1, $zero, $v0

# print number
		add	$a0, $zero, $v0
		addi	$v0, $zero, 1
		syscall

# branch depending on sign 
		blt	$s1, $zero, Negative

# print " is positive" and loop back 
Positive: 	addi	$v0, $zero, 4
		la	$a0, POS
		syscall
		j Main

# print " is negative" and loop back 
Negative:	addi	$v0, $zero, 4
		la	$a0, NEG
		syscall
		j Main

# say good-bye and then ...
Goodbye:	addi	$v0, $zero, 4
		la	$a0, BYE
		syscall

# exit cleanly 
		li	$v0, 10 
		syscall