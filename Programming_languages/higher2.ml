(* 
	Let's write a "mapping" function similar to the "map"
	in Python, even though SML also has a built-in "map"
        function too. Recall that such a function takes two
	parameters, the first of which is a function, and 
	the second of which is a list. It returns a list 
	obtained by applying the function to the entries 
	in the original list. 

	Since "mapping" is a function that has a parameter 
	that is also a function, it is said to be a "higher 
	order" function. Higher order functions are discussed 
	in Section 5.16.
*)

(* Two styles for defining functions of a single parameter *) 

fun square(x) = x * x;

val add_one = fn x => x + 1; 

(* Now for the "mapping" function *)

fun mapping(f, []) = []
  | mapping(f, lst) = f(hd(lst))::mapping(f, tl(lst));

val new_list = mapping(square, [1, 2, 3, 4, 5]);

(*
   Let's now write a function "compose_two" to compose 
   two functions of a single parameter. Let's write a 
   curried form of it too. 
*)

fun compose_two(f, g) = fn x => f(g(x));

val cur_compose_two = fn f => fn g => fn x => f(g(x)); 

val num1 = compose_two(square, add_one)(5); 

val num2 = cur_compose_two(square)(add_one)(5); 

(* 
   Now let's write a function to recursively compose 
   a whole list of functions of a single parameter. 
*)

val identity_function = fn x => x; 

fun compose_list([])   = identity_function
  | compose_list([f])  = f
  | compose_list(h::t) = compose_two(h, compose_list(t));

val num3 = compose_list([square, add_one, square])(2); 

(*
  Next we'll make a function "reduce_them" that behaves like the 
  "reduce" function we saw in Python. Recall that this receives 
  a function of two arguments (a binary operation, basically), 
  together with a list, and it repeatedly applies the binary 
  operation. 

  As a simple example, if the binary operation is adition, 
  then we end up summing up everything in the list. To make it 
  a little more general purposed, let's add another parameter 
  (in between the other two) to tell reduce_them what to return 
  when given an empty list. 
*)

fun add_two(x, y) = x + y; 

fun reduce_them(oper, init, []) = init
  | reduce_them(oper, init, h::t) = oper(h, reduce_them(oper, init, t));

val the_sum = reduce_them(add_two, 0, [2, 5, 6, 4]); 

(*
  Next we'll make a function "filter_them" that behaves like the 
  "filter" function we saw in Python. Recall that this receives
  a predicate (i.e. a function that returns a boolean value),
  together with a list. It builds a new list that that consists of 
  the entries in the original list for which the predicate is true.
*)

fun is_positive(x) = (x > 0); 

fun filter_them(pred, []) = []
  | filter_them(pred, h::t) = 
    if pred(h)
      then h::filter_them(pred, t)
      else filter_them(pred, t);

val new_list = filter_them(is_positive, [~3, ~4, 2, 0, 3, 5, ~8, 9]);
