#!/usr/bin/perl -w

#          Perl Example 5

# turn on autoflushing to cause prints to work immediately
$| = 1;

# Regular Expressions and matchings are a very important part of Perl.
# When seraching for a regular expression, it is put between forward slashes. 
# There are lots of special characters to worry about though. They behave
# as "metacharacters". Here are some metacharacters: 
#
#   ()  parentheses are used to delineate a block of text
#   []  square brackets are used to list several character options
#   |   is another way to give several options, which could be blocks ("or")
#   .   stands in for any single character
#   *   means zero or more occurrence of the previous character or block
#   +   means one or more occurrence of the previous character or block
#   {}  used to specify a precise number of required repetitions
#   ^   matches imaginary character at the start of the string
#   $   matches imaginary character at the end of the string
#
# Note that [^...] means characters other than those listed. For instance,
# [^abc] would match any single character except a, b or c.  
#
# When a character is normally used as a metacharacter, then to use it in
# a literal way instead, preface it with a backslash, as for example: \+
# However, some characters that are not ordinarily metacharacters become
# metacharacters by prefacing them with a backslash, as for example, these:
#
# \s   means any whitespace character
# \S   means any non-whitespace character
# \d   means any digit
# \D   means any non-digit 
#
# The notation "=~" is used to search the string on the left for the regular
# expression on the right. If something is found, it is put in $1.
# By using parentheses to group, certain special system variables,
# $1, $2, $3, ..., can be used to capture the results. Watch:
# Here are a few examples of all this stuff:

if ("This is a sentence." =~ /is/) {
  print "Found it.\n";
}
if ("This is a sentence." =~ /[qrs]/) {
  print "Found that too.\n";
}
if ("I wonder if this will work." =~ /(this)|(that)/) {
    print "Yep!\n";
} else {
    print "Nope!\n";
}
if ("I wonder if this will work." =~ /thi(s|t)hat/) {
    print "Yep!\n";
} else {
    print "Nope!\n"; 
}
if ("I wonder if this will work." =~ /this|that/) {
    print "Yep!\n";
} else {
    print "Nope!\n"; 
}
if ("Hey, maybe this + will be found" =~ /\+/) {
  print "Found the plus.\n";
}
if ("What happens if I try this?" =~ 
    /(\sh\S*\s).*(\sI\s).*(\s\S*\?)/) {
  print $1, "\t\t", $2, "\t\t", $3, "\n";
}
if ("This is really a simple example actually?" =~
    /(\s\S+\s).*(\s\S+\s).*(\s\S+\s)/) {
  print $1, "\t\t", $2, "\t\t", $3, "\n";
}
if ("Next, let's try this little experiment." =~
    /^(.*)(little)(.*)$/) {
  print $1, "\t\t", $2, "\t\t", $3, "\n";
}
if ("Let's try something else." =~
    /^(.*)([ighnt]{5,})(.*)$/) {
  print $1, "\t\t", $2, "\t\t", $3, "\n";
}
if ("Now I will wonder here what will happen." =~
    /^(.*)(w[^wr]*r)(.*)$/) {
  print $1, "\t\t", $2, "\t\t", $3, "\n";
}

print "\nTry out as many matching attempts as you wish here.\n";
print 'Enter test string (blank to quit): '; 
while (<STDIN>) {
  chomp;
  last if $_ eq "";
  $teststring = $_; 
  print 'Enter regular expression: '; 
  $regexpr = <STDIN>;
  chomp $regexpr;
  if ($teststring =~ /($regexpr)/) { 
    print 'Found it: ', $1, "\n"; 
  } else { 
    print "Cannot find it.\n"; 
  } 
  print 'Enter test string: '; 
}

print "\nNow try a variation on this, as much as you wish.\n";
print 'Enter test string (blank to quit): '; 
while (<STDIN>) {
  chomp; 
  last if $_ eq "";
  $teststring = $_; 
  print 'Enter regular expression: '; 
  $regexpr = <STDIN>;
  chomp $regexpr;  
  if ($teststring =~ /^(.*)($regexpr)(.*)$/) { 
    print 'Found it: ', $2, "\n"; 
    print 'Preceded by: ', $1, "\n";
    print 'Followed by: ', $3, "\n";
  } else { 
    print "Cannot find it.\n"; 
  } 
  print 'Enter test string: '; 
}

# Notice the syntax below for finding a pattern (regular expr.) and then
# globally substituting something else for it: "... =~ s/.../.../g".
# Leave off the "g" at the end to just do a single substitution.
# Deleting a substring is possible by replacing it with the empty string.
# Here are some examples of substitutions and removals that act on the
# special variable "$_" , and hence it is unnecessary to use "... =~" :
#
print "\n\n";
$_ = "   I  want    a  simple   example.    \n";
print;
s/ a / some /g;         # substitute " some " for " a "
print;
s/want/WANT/g;          # capitalize "want" 
print;
s/^\s+//;               # remove leading whitespace
s/\s+$//;               # remove trailing whitespace
s/\s\s+/ /g;            # remove extra whitespace
print $_, "\n";

print "\nNext try out as many global substitutions as you wish.\n";
print 'Enter test string (blank to quit): '; 
while (<STDIN>) {
  chomp;
  last if $_ eq "";
  $teststring = $_;
  print 'Enter regular expression to find: ';
  $regexpr = <STDIN>;
  chomp $regexpr;
  print 'Enter replacement string: ';
  $replacement = <STDIN>;
  chomp $replacement;
  $teststring =~ s/($regexpr)/$replacement/g;
  print "Result: $teststring\n";
  print 'Enter test string: ';
}

# Another important application of regular expressions is to
# locate intended dividers in a string, and "split" the string
# into substrings, by cutting out these dividers
$_ = "I will  use whitespace, commas and semicolons to divide; all of it.";
@_ = split /[\s,;]+/;        # implicitly:  @_ = $_ split /[\s,;]+/;  
print $_, "\n" foreach @_; 

print "\nTry out splitting a string, as many times as you like. \n";
print 'Enter test string (blank to quit): '; 
while (<STDIN>) {
  chomp; 
  last if $_ eq "";
  $teststring = $_; 
  print 'Regular expression for splitting: '; 
  $regexpr = <STDIN>;
  chomp $regexpr;
  @result = split /$regexpr/, $teststring; 
  print "Result: @result\n"; 
  print $_, "\n" foreach @result; 
  print 'Enter test string: '; 
}
print "\n\n"; 


# *******************************************************

# Processing files and directories is also big business
# in the Perl world, and we'll finish up with a bit of this

# Different styles for opening data files for reading 
open FILE1, '<', "PerlExample1.pl"; 
open FILE2, "<PerlExample2.pl"; 
open FILE3, "PerlExample3.pl";

# Each <...> here is being used in a scalar context, causing
# each occurrence to read one single line of the file, and so
# the following grabs three lines of each of three input files.
$s = <FILE1>.<FILE1>.<FILE1>; 
print $s, "\n"; 
$s = <FILE2>.<FILE2>.<FILE2>; 
print $s, "\n"; 
$s = <FILE3>.<FILE3>.<FILE3>; 
print $s, "\n";

# Here though <...> causes the remainder of the file to be 
# read all at once, because nothing implies scalar context
print "\n\nHit enter/return to display rest of first file";
<STDIN>;
print <FILE1>; 
close FILE1;

# You could also cause the lines to be read into an array
# and then display, or process in some other way, these lines
print "\n\nHit enter/return to display rest of second file";
<STDIN>;
@lines = <FILE2>;
print @lines; 
close FILE2;
$numlines = @lines;  # interprets "@lines" in scalar context
print "\n---> Number of lines here is ", $numlines, "\n\n";
print "Hit enter/return to show it again";
<STDIN>;
print "LINE:  ", $_ foreach (@lines);

# But we can also loop to read one line of a file at a time,
# and display that line, or process it in some other way
print "\n\nHit enter/return to display rest of third file";
<STDIN>;
while (<FILE3>)
{
  print;   # "print" here means "print $_"
  chomp;   # "chomp" here means "chomp $_"
  if ($_ ne "") { print "AGAIN: ", $_, "\n\n"; } 
}
close FILE3;

# *** WE WILL PROBABLY STOP HERE, AND IGNORE FILE OUTPUT ***

print "\n\nHit enter/return to copy files to a new file (dump.dat)";
<STDIN>; 
open INPUT, '<', "PerlExample4.pl";

# The '>' here suggests an output file to write to from scratch
open OUTPUT, '>', "dump.dat"; 
print OUTPUT <INPUT>; 
close INPUT; 
close OUPUT; 
open INPUT, '<', "PerlExample5.pl"; 

# The '>>' here suggests an output file to append to
open OUTPUT, '>>', "dump.dat"; 
while (<INPUT>) { 
  print OUTPUT $_;
} 
close INPUT; 
close OUPUT; 

# DO NOT WORRY ABOUT THE REST OF THIS STUFF UNLESS YOU WANT TO 

print "\n\nHit enter/return to show some environmental information";
<STDIN>; 
print "\n", %ENV, "\n"; 
print "User is $ENV{USER}.\n"; 
print "Home directory is $ENV{HOME}.\n"; 
print "Executables path list is $ENV{PATH}.\n"; 

print "\n\nHit enter/return to display some of current directory";
<STDIN>;
print "\n"; 
print $_, "\t", foreach <*.pl>;

print "\n\nHit enter/return to display whole directory in greater detail";
<STDIN>; 
foreach (<*>) { 
   next if /^\./;
   print $_, " " x (30 - length);
   print "d" if -d $_; 
   print "r" if -r _; 
   print "w" if -w _; 
   print "x" if -x _; 
   print "o" if -o _; 
   print "\t"; 
   print -s _ if -r _ and -f _; 
   print "\n"; 
} 

print "\n\nHit enter/return to tour some directories";
<STDIN>; 
opendir DH, $ENV{HOME} or die "Couldn't open home directory: $!";
@a = readdir(DH); 
print "\nLet's play with directories...\n";
print "Here is contents of home directory: @a.\n\n";
close DH;

opendir DH, "." or die "Couldn't open current directory: $!"; 
@a = readdir(DH); 
print "\nHere is contents of current directory: @a.\n\n"; 
close DH;

$d = ""; 
foreach(@a) {
   if (-d $_ && !/^\./) { 
      $d = $_; 
      last; 
   } 
} 

if ($d ne "") {
  chdir $d; 
  print "Just went into subdirectory $d.\n"; 
  opendir DH, "." or die "Couldn't open current directory: $!"; 
  @a = readdir(DH); 
  print "\nHere is contents of current directory: @a.\n\n"; 
  close DH;
  chdir ".."; 
} 

print "\n         THAT SHOULD REALLY BE ENOUGH!!\n"