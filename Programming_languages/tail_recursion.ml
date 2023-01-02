
(* 
   Section 5.10 discusses the very interesting and 
   versatile topic of data types. However, the example
   of defining recursive datatypes seems a bit daunting 
   to me until after we get more experience doing some 
   more standard functional programming topics. 
   So we'll skip Section 5.10 for now and come back to 
   it later. 
*)
(*
   Section 5.11 starts with the classic example of how 
   inefficient recursion can be, when it is "abused." 
   Try computing fibo(42). If you get tired of waiting, 
   then use control-C to interrupt the computation. 
*)

fun fibo(0) = 0
  | fibo(1) = 1 
  | fibo(n) = fibo(n-1) + fibo(n-2)

(* 
   A helper function can be used to vastly reduce the 
   number of recursive calls. In the following, calling 
   fib(n) causes n+1 calls to fibhelper, like so:
      fibhelper(0, 1, 0)
      fibhelper(1, 1, 1)
      fibhelper(2, 2, 1)
      fibhelper(3, 3, 2)
      fibhelper(4, 5, 3)
      fibhelper(5, 8, 5)
      fibhelper(6, 13, 8)
      fibhelper(7, 21, 13)
      ...
      fibhelper(n, ?, ?).
   This is somewhat (only somewhat) similar to the way 
   my fiboTriple function worked. Now try computing fib(42).
*)

fun fib(n) = 
  let fun fibhelper(count, current, previous) = 
    if count = n then previous
    else fibhelper(count+1, previous+current, current)
  in
    fibhelper(0, 1, 0)
  end;

(* 
   Like many functional programming languages, SML makes 
   specially low-level code previsions for speeding up 
   a special kind of recursion known as "tail recursion."
   If you've taken CS 130 already, then you are in a position 
   to understand how this speedup works, if you dig into it, 
   but I won't discuss the speedup here. I will explain what 
   tail recursion is. It is simply the idea that inside a 
   function, a recursive call can only be made just before 
   the original call returns, and what that returns must be 
   what the recursive call returns. Tail recursion is 
   discussed in Section 5.13. 
*)

(* 
   Here is an absolutely useless example of tail recursion.
*)

fun f(0) = 0
  | f(n) = f(n-1)

(*
   Here is a familiar example of recursion that is NOT tail 
   recursion, though it is sort of close perhaps. 
*)

fun factorial(0) = 1
  | factorial(n) = n * factorial(n-1);

(* 
  Here is how factorial can be computed using tail recursion, 
  but tailfun is actually the helper function here that uses 
  tail recursion. 
*)

fun fac(n) = 
  let 
    fun tailfac(0, prod) = prod
      | tailfac(n, prod) = tailfac(n-1, prod * n)
    in 
      tailfac(n, 1)
    end;


(* 
  Calling fac(n) results in n+1 calls to tailfac: 
      tailfac(n, 1)
      tailfac(n-1, n)
      tailfac(n-2, n*(n-1))
      tailfac(n-3, n*(n-1)*(n-2))
      ...
      tailfac(0, n!)
*) 

