
(* 
   Remember: You are not responsible for this material,
   but it's kind of fun. 
*)

datatype 
   day = Monday | Tuesday | Wednesday | Thursday | Friday;

fun happyYet(Monday)    = false
  | happyYet(Tuesday)   = false
  | happyYet(Wednesday) = false
  | happyYet(Thursday)  = false
  | happyYet(Friday)    = true;

datatype
   AST = add'      of AST * AST 
       | sub'      of AST * AST 
       | mul'      of AST * AST 
       | neg'      of AST 
       | num'      of int

fun eval(num'(n)) = n
  | eval(neg'(ast)) = 0 - eval(ast)
  | eval(add'(ast1,ast2)) = 
    eval(ast1) + eval(ast2)
  | eval(sub'(ast1,ast2)) = 
    eval(ast1) - eval(ast2)
  | eval(mul'(ast1,ast2)) = 
    eval(ast1) * eval(ast2);

(* Here is the example of an AST from the Power Point slides *)
eval( sub'(mul'(num'(47),num'(13)),mul'(num'(3),neg'(num'(24)))) );




