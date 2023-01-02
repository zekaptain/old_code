
(* 
	Let's write a mapping function similar to the map
	in Python. Recall that such a function takes two
	parameters, the first of which is a function, and 
	the second of which is a list. It returns a list 
	obtained by applying the function to the entries 
	in the original list. SML actually has a built-in 
	map function already, but let's build our own. 

	Since mapping is a function that has a parameter 
	that is also a function, it is said to be a "higher 
	order" function. Higher order functions are discussed 
	in Section 5.16.
*)

fun square(x) = x * x;

fun add_one(x) = x + 1; 

fun mapping(f, []) = []
  | mapping(f, lst) = f(hd(lst))::mapping(f, tl(lst));

 (* the data type of map (or in this case, mapping) is: ( 'a -> 'b ) * ( 'a list ) -> ('b list ) *)
 (* asterisk above implies ordered pair. first parentheses is a function, then a list in second, and that's all an ordered pair input into 
 another function containing a list *)

val new_list = mapping(square, [1, 2, 3, 4, 5]);

(*
   Let's now write a function compose_two to compose 
   two functions of a single parameter. 
*)

fun compose_two(f, g) = fn x => f(g(x));

val num1 = compose_two(square, add_one)(5); 

(* 
   Now let's write a function to recursively compose 
   a whole list of functions of a single parameter. 
*)

fun compose_list([f])  = f
  | compose_list(h::t) = compose_two(h, compose_list(t));

val num2 = compose_list([square, add_one, square])(2); 
