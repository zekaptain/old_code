(*  author: Zeke Elkins *)


(* Insert at start of LLL function *)
fun insertAtStart(lst1,it)=
	if null(lst1) then [it]
	else insertAtStart(hd(lst1),it)::tl(lst1);

(* get first in LLL function *)
fun getFirst(lst1)=
	if null(lst1) then 0 (*return none/null*)
	else (*return hd(lst1)*) hd(lst1);


(* remove first from LLL *)
fun getRest(lst1)=
	if null(lst1) then [] (*return none/null*)
	else (*return tl(lst1)*) tl(lst1);


(* get last in LLL *)
fun getLast(lst1)=
	if null(lst1) then 0 (*return none/null*)
	else if null(tl(lst1)) then hd(lst1) (*return hd(lst1)*)
	else getLast(tl(lst1));


(* remove last from LLL *)
fun removeLast(lst1)=
	if null(lst1) then [] (*return none/null*)
	else if null(tl(lst1)) then [](*return none/null*)
	else hd(lst1)::removeLast(tl(lst1));


(* insert at end of LLL *)
(* want to insert "it" into a list in ml. it::nil <-- nil is an empty list. [it] is simpler and does the same thing.  *)
fun insertAtEnd(lst1,it)=
	if null(lst1) then [it]
	else hd(lst1)::insertAtEnd(tl(lst1),it); 


(* merge LLL *)
fun my_append(lst1,lst2)=
	if null(lst1) then lst2
	else hd(lst1)::my_append(tl(lst1), lst2);
	(* head (hd) is first thing in the list, tail (tl) is the rest -- the list you get when you throw away the head *)
	(* this entire final line makes hd(lst1) the head of the new list after the two colons, which take up the tail of the new list *)


(* reverse(LLL) *)
fun reverse(lst1)=
	if null(lst1) then [](*return none/null*)
	else insertAtEnd(reverse(tl(lst1)),hd(lst1));


(*  PART TWO  *)
(* pattern matching is something like this -- "h::t" *)

fun power(x,0) = 1
	power(x,n)=
		let val power1 = power(x,n-1)
		in
			x * power1
		end;

power(3,2)


fun combo(n,0)=1
	combo(0,r)=0
	combo(n,r)=
		let 
			val combo1 = combo(n-1,r)
			val combo2 = combo(n-1,r-1)
		in
			combo1 + combo2
		end;

combo(3,1)










