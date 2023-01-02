fun babsqrt(x, guess) =
  if Real.abs(x-guess*guess) < x/1000000.0 then
    guess
  else
    babsqrt(x, (guess+x/guess)/2.0);
