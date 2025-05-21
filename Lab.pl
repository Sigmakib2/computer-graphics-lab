% Define even rule
even(Number) :-
    Number mod 2 =:= 0,
    write(Number), write(' is even.').

% Define odd rule
odd(Number) :-
    Number mod 2 =:= 1,
    write(Number), write(' is odd.').

% Main rule to check even or odd
check(Number) :-
    (even(Number) -> true ; odd(Number)).
