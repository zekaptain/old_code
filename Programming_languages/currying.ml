
(* 
   Currying in SML is pretty much like it was in Python. 
   The keyword "lambda" though needs to be changed to "fun"
   or "fn", and the colons are missing. This topic is 
   discussed in Section 5.14. Observe. Note the difference 
   between "fun" and "fn". "fn" is closer to "lambda" and 
   uses an arrow instead of a colon.
*)

fun power(x, 0) = 1
  | power(x, n) = x * power(x, n-1);

fun cur_power(n)(x) = power(x, n); 

val cube = cur_power(3);

val five_cubed = cube(5); 

val double = fn x => 2 * x; 

val cur_pow = fn n => fn x => power(x, n); 

val five_cubed_again = cur_pow(3)(5); 

