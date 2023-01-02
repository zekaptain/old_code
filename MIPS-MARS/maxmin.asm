# A MIPS program to find the maximum and minimum of some integers

	.data

numnums:	.asciiz "How many numbers to compare? "
enternum:	.asciiz "Enter a number: "
maxis:		.asciiz "The maximum is "
minis:		.asciiz "The minimum is "
ret:		.asciiz "\n" 

	.text

main:
# prompt for how many numbers
		addi	$v0, $zero, 4			# same as saying li $v0, 4
		la	$a0, numnums			# li instruction really 
		syscall

# get number of numbers from user, and keep it in $s1 
		addi	$v0, $zero, 5
		syscall
		add	$s1, $zero, $v0                 #copy $v0 to $s1

# initialize maximum, minimum and loop counter
		add	$s0, $zero, $zero
		addi	$s2, $zero, 100000
		add	$t0, $zero, $zero

# a "while-loop" requires pretesting, so test to 
# see if $t0 has reached $s1 yet. Done if so. 
loop:		beq	$t0, $s1, done 

# loop body - get number, compare to max and min, etc., increment $t0 
		addi	$v0, $zero, 4
		la	$a0, enternum
		syscall					# prompt user
		addi	$v0, $zero, 5
		syscall					# get number from user 

		ble	$v0, $s0, skip1			# skip ahead unless biggest so far
		add	$s0, $zero, $v0			# copy number to maximum

skip1:		bge	$v0, $s2, skip2			# skip ahead unless biggest so far
		add	$s2, $zero, $v0			# copy number to maximum

skip2:		addi	$t0, $t0, 1			# increment loop counter 
		j	loop

# display "The maximum is " 
done:		addi	$v0, $zero, 4
		la	$a0, maxis
		syscall

# print the max 
		add	$a0, $zero, $s0
		addi	$v0, $zero, 1
		syscall

# print carriage return  
		addi	$v0, $zero, 4
		la	$a0, ret
		syscall

# display "The minimum is " 
		addi	$v0, $zero, 4
		la	$a0, minis
		syscall

# print the min 
		add	$a0, $zero, $s2
		addi	$v0, $zero, 1
		syscall

# exit cleanly 
		addi	$v0, $zero, 10 
		syscall