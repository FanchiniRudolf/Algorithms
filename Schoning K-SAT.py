"""input: a formula in -CNF with variables
Guess an initial assignment ,
uniformly at random
Repeat times:
If the formula is satisfied by the actual
assignment: stop and accept
Let be some clause not being satisfied by
the actual assignment
Pick one of the literals in the clause
at random and flip its value
in the current assignment"""