(* 

Author: Zeke Elkins
Description: Homework #9 for Programming Languages

*)


(* PROBLEM 1 *)
(* tail recursive power function *)

(* FOR REFERENCE
fun power(x,0)=
	| power(x,n)=
	let
		val y = power(x,n-1)
	in 
		x*y
	end;
*)

fun pow(x,n) = 
	let
		|fun tailpower(x,0,prod) = prod
			| tailpower(x,n,prod) = tailpower(x,n-1,x*prod)
		in
			tailpower(x,0)
		end;

(* FOR REFERENCE
fun factorial(0) = 1
  | factorial(n) = n * factorial(n-1);

fun fac(n) = 
  let 
    |fun tailfac(0, prod) = prod
      | tailfac(n, prod) = tailfac(n-1, prod * n)
    in 
      tailfac(n, 1)
    end;
*)

(* PROBLEM 2 *)
(* triangle number code basically, add the returned number and input-1 returned number -- both normal recursive and tail recursion *)
fun triangle_number(0) = 0
|  triangle_number(1) = 1
|  triangle_number(n) = 
		let
			val tri1 = triangle_number(n-1)
			val tri2 = triangle_number(n-2)
		in
			tri1 + tri2
		end;


fun tri(n) = 
	let
		|fun tailtri(0,prod) = prod
			| tailtri(n,prod) = tailtri(n-1,prod * (n-2))
		in
			tailtri(n,0)

		end;



(* (* PROBLEM 3  [] or nil is an empty list. To have a list containing one thing, it's this: [h] or h::nil or h::[]. 
To match a list with at least two items in it, do this: h::s::t  *) *)
fun opp_reduce_them(oper, init, lst) = init
	if null(lst) then []
	if null(tl(lst)) then hd(lst)
	if null(tl(tl(lst))) then tl(lst)::hd(lst)
  | opp_reduce_them(oper, init, f::s::t) = oper(t, opp_reduce_them(oper, init, f::s));


(* PROBLEM 4 *)
fun reverse_order(f,g) = fn x => fn y => f(g(y,x))







