		
#program that tells if entered number is 1, 2, or 3 and prints out a message		
		.data

enterednum:	.asciiz "Please enter a number between 1 and 3, including 1 and 3: "
errormsg:	.asciiz "Error: enter number between 1 and 3 \n"
numis1:		.asciiz "One is the loneliest number"
numis2:		.asciiz "Two is company"
numis3:		.asciiz "Three's a crowd" 

		.text
		

	
#store 1 in $s2
	addi	$s2, $zero, 1
#store 2 in $s3
	addi	$s3, $zero, 2
#store 3 in $s4
	addi	$s4, $zero, 3

	
#do-while loop. 
loop:	

	#store the entered num into $s1
	# prompt for integer num1 input 
	addi	$v0, $zero, 4
	la	$a0, enterednum
	syscall
	# get integer input from user 
	addi	$v0, $zero, 5
	syscall

	# save number
	add	$s1, $zero, $v0
	
	#check if num equals 1 2 or 3 and branch if so
	beq	$s1, $s2, ifone 
	beq	$s1, $s3, iftwo
	beq	$s1, $s4, ifthree
	#otherwise print error message and loop, asking for new num
	addi	$v0, $zero, 4
	la	$a0, errormsg	#displays the error message
	syscall
	j	loop


ifone:
	addi	$v0, $zero, 4
	la	$a0, numis1	#displays numis1
	syscall
	j	done

iftwo:
	addi	$v0, $zero, 4
	la	$a0, numis2	#displays numis2
	syscall
	j	done

ifthree:
	addi	$v0, $zero, 4
	la	$a0, numis3	#displays numis3
	syscall
	j	done

done:
	#halt cleanly
	li	$v0, 10 
	syscall