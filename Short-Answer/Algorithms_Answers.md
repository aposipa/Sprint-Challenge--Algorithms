#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  For this code, it will run while a is < n^3.  Then a will increase by n^2.  Because of that the output is actually just n (n^3/n^2 = n), making it O(n).


b)  For this code, there is a nested while loop in a for loop so we will combined the notations.  The for loop, j increases proportional to the size on n, so its O(n).  Then the while loops only while J is less than n, and doubles each time making it a (log(n)).  Since its nested we combine them so the full runtime is O(n log n).


c)  Even though its recursive the rate at which the bunny ears goes up is a constant/linear rate, so the runtime will be O(n).

## Exercise II

First pass solution: We could start at the top and iterate through checking each floor to see if the egg breaks from that floor until we get to f where it doesn't.  Then if floor > f, egg breaks, but if floor < f, egg doesn't break.
