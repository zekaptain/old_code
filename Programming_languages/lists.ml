
		(* Building on Section 5.6 of Lee's Book Here *) 

(* 
   Various ways to make numeric lists in ML
*) 

val list1 = [1, 4, 9, 16];
val list2 = 1::[4, 9, 16];
val list3 = 1::4::9::16::nil;
val list4 = 1::(4::(9::(16::nil)));
val list5 = 1::4::9::[16];

(* 
   This next one is illegal:
   (((1::4)::9)::16)::nil;
*)

(* 
   A couple ways to make lists of character data. 
   #"a" is ML's crazy way to indicate the character a.
*) 

val list6 = [#"a", #"b", #"c"];
val list7 = #"a"::(#"b"::[#"c"]);

(*
   This one is illegal, no matter what the book says!
   #"a"::#"b"::[#"c"];
*)

(* 
   Arrays of strings and appending/joining/merging two lists together
*)

val list8 = ["eggman", "walrus", "carpenter", "cabbage", "king"];
val list9 = "queen"::"jack"::"lantern"::"green"::nil;
val list10 = list8 @ list9;

(* 
   This is not allowed: 
      list8 @ list7;
   Why not? 
*)

(* 
   hd and tl get head and tail, as we did in Python for "Lisp-like lists"
*)

val theHead = hd(list10); 
val theTail = tl(list10); 

(* 
   explode converts a string to a character list, 
   and implode does the opposite.
   A carat (^) is used for string concatenation.
*)

val str1 = "supercalifragilisticexpialidocious";
val list11 = explode(str1);
val str2 = substring(str1, 5, 4);
val chr1 = String.sub(str1, 21);
val youknow = implode(list11);
val stillknow = implode(tl(list11));
val howaboutnow = hd(tl(tl(tl(tl(tl(list11))))));
val list12 = List.rev(list11);
val str3 = implode(list12); 
val str4 = "Hi " ^ "there.";

(* 
   We can define our own version of implode and explode, 
   to again highlight the power of recursion and recursive thinking.
*)

fun my_implode(lst) = 
  if lst = [] then ""
  else str(hd(lst)) ^ my_implode(tl(lst));

fun my_explode(str) = 
  if str = "" then []
  else String.sub(str,0) ::
    my_explode(String.substring(str, 1, String.size(str)-1));

val list13 = my_explode(str1);
val str5   = my_implode(list13);

(* 
   A little more recursion - examples from the book
*)

fun my_length(lst) = 
  if null(lst) then 0
  else 1 + my_length(tl(lst)); 

fun my_append(lst1, lst2) = 
  if null(lst1) then lst2
  else hd(lst1)::my_append(tl(lst1), lst2);

val len = my_length(list13);
val list14 = my_append(list13, list12); 
val str6 = my_implode(list14); 

(* 
  "Pattern matching" function definitions - from Section 5.7
*)

fun new_append(nil, lst2) = lst2
  | new_append(hd1::tl1, lst2) = hd1::new_append(tl1, lst2);

val list15 = new_append(list13, list12); 
val str7 = my_implode(list15); 
