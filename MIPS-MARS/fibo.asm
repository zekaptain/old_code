# A MIPS program to generate Fibonacci numbers

	.data

myAge:          39

numnums:	.asciiz "How many Fibonnaci numbers would you like (>2)? "
listhdr:	.asciiz "Here are the Fibonnaci numbers:\n"
space:		.asciiz " "

	.text

main:
# prompt for how many numbers
		addi	$v0, $zero, 4		# same as saying li $v0, 4
		la	$a0, numnums		# li instruction really 
		syscall

# get number of numbers from user, and keep two less than it in $s0 
		addi	$v0, $zero, 5
		syscall
		addi	$s0, $v0, -2

# will use $s1, $s2, $s3 for consecutive Fibonacci numbers, so initialize 
		addi	$s1, $zero, 1		# $s1 = 1 
		addi	$s2, $zero, 1		# $s2 = 1

# display first two Fibonacci numbers:
		addi	$v0, $zero, 4
		la	$a0, listhdr
		syscall
		add	$a0, $zero, $s1
		addi	$v0, $zero, 1
		syscall
		addi	$v0, $zero, 4
		la	$a0, space
		syscall
		add	$a0, $zero, $s2
		addi	$v0, $zero, 1
		syscall
		addi	$v0, $zero, 4
		la	$a0, space
		syscall


loop:		
# compute next Fibonacci number and display it 
		add	$s3, $s1, $s2 
		add	$a0, $zero, $s3
		addi	$v0, $zero, 1
		syscall
		addi	$v0, $zero, 4
		la	$a0, space
		syscall

# shift the Fibonacci numbers
		add	$s1, $s2, $zero
		add	$s2, $s3, $zero

# decrement counter and maybe loop back 
		addi	$s0, $s0, -1
		bne	$s0, $zero, loop

# exit cleanly 
		li	$v0, 10 
		syscall