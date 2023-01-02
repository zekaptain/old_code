
(* 
   These examples of binding and scope come from Section 5.9 
   or are motivated by the discussion there.
*)

(* 
   Here is one example from the book, though I added prints. 
   Beware: x is not a variable (there is no such thing).
   x is an identifier (label) that gets bound to a value, 
   but cannot change value later, as with variables in 
   other languages. 
   Because of scoping (familiar to you in other languages?),
   there are actually two different bindings, one occuring 
   "outside" and one occurring "inside". Though the identifier
   "x" is used in both cases, the bindings are independent of 
   each other, and are valid in different sections of code, 
   i.e. they have different scopes. 
*)

let val x = 10      (* the "outer binding" for x *)
in
   let val x = x+1  (* use outer binding to define inner binding *)
   in 
      print(Int.toString(x)^"\n")  (* print value for inner binding *) 
   end;
   print(Int.toString(x)^"\n")  (* print value for outer binding *)
end;

(* The following would cause an error after the above code:
        print(Int.toString(x)^"\n");
*) 

(* Another example from book *)
fun sumupto(0) = 0
  |  sumupto(n) = 
    let val sum = sumupto(n-1) (* recursion happens right now? *)
    in
       n + sum  (* or right now? *) 
    end;
(* Answer: the first one *)

sumupto(5);

(* Modified example from book *)
fun weirdsumupto(0) = 0
  | weirdsumupto(n) = 
    let val sum = weirdsumupto(n-1)
    in
       n + sum*sum
    end;

weirdsumupto(1);
weirdsumupto(2);
weirdsumupto(3);
weirdsumupto(4);

(* 
    Challenge #1: Using the style of sumupto, 
    write a recursive function fibo for 
    generating Fibonacci numbers. Arrange 
    for fibo(0) = 0, fibo(1) = 1, and otherwise, 
    fibo(n) = fibo(n-1) + fibo(n-2).
*) 

(* My solution *)
fun fibo(0) = 0
  | fibo(1) = 1 
  | fibo(n) = 
    let 
      val fib1 = fibo(n-1)
      val fib2 = fibo(n-2)
    in
      fib1 + fib2
    end;

fibo(8);

(* 
   Challenge #2: Still using the same style, write 
   a recursive function fiboTriple that returns a 
   list containing three consecutive Fibonacci 
   numbers, in reverse order (biggest first).
   Have this function receive an integer n. 
   If n is 0, then have it return [1, 1, 0].
   If n is 1, then have it return [2, 1, 1].
   If n is 2, then have it return [3, 2, 1].
   If n is 3, then have it return [5, 3, 2].
   If n is 4, then have it return [8, 5, 3].
   And so forth. 
   fiboTriple should make at most one recursive call.
   If you need the entries in one of these lists, 
   then use hd and tl to get them. 
*)

(* My solution *)
fun fiboTriple(0) = [1, 1, 0]
  | fiboTriple(n) = 
    let 
      val triple = fiboTriple(n-1)
      val first  = hd(triple)
      val second = hd(tl(triple))
    in
       [first+second, first, second]
    end;
fiboTriple(6);

(* A tricky example from the end of Section 5.9 *) 

fun doit() = 
  (* function a returns function b, and function a is returned to function c at the end *)
  let fun a() = 
    let val x = 1
      fun b() = x
    in 
      b
    end
    val x = 2
    val c = a()
  in 
    c()
  end;

(*
   Let's figure that out. Take a deep breath. 
   When calling doit(), the call c() is also invoked. 
   But this first requires obtaining the funcion c.  
   as the returned value of the call a(). 
   But the function returned by a() is the function b, 
   and this function is such that a call to it always 
   returns 1, because 1 is the value of x at the 
   time that the function b is defined. Setting c = a()
   causes c and b to become the same function, namely, 
   the function that always returns 1. 

   Why this horrible and terrifying example? 
   To show you that SML, like nearly every modern 
   programming language uses "STATIC SCOPING."
   If instead it used "DYNAMIC SCOPING," then 
   c would become the function that always 
   returned 2. Why? Because in that case, the 
   definition of the function b would be set up 
   dynamically while calling c(), and the x that 
   would get used in defining b would be the x 
   that was set up just before calling c(), and 
   that x has value 2. 
*)
