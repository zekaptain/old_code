#!/usr/bin/perl -w

$| = 1;

open FILE, "DI Women's College Basketball - Stats _ NCAA.com.html";

while (<FILE>)
{

	if (/>Oregon<\/a>/) {  

		@_ = split /<[^<>]*>/;

    	foreach (@_) {

      		print $_."\n" if /\S/;
      	}

	}
}

close FILE;

open FILE, "DI Women's College Basketball - Stats _ NCAA.com.html";

print 'Enter college name (blank to quit): '; 
while (<STDIN>) {

 	chomp; 
  	last if $_ eq "";
  	$collegename = $_; 

  	while (<FILE>) {
  		  
  		if (/>$collegename<\/a>/) {  

			@_ = split /<[^<>]*>/;

    		foreach (@_) {
      			print $_."\n" if /\S/;
      		}
		}
  	}

  	close FILE;

  	open FILE, "DI Women's College Basketball - Stats _ NCAA.com.html";

  	print 'Enter college name (blank to quit): ';

}

close FILE;





