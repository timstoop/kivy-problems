# Problem: Passing data betweem Screens

I'm looking for a solution to pass data between Screens. This solves things that should be simple, like passing a score for a level to the next screen, so it can congratulate you on achieving that score or something.

In the code, I made two examples. One is directly in the Python code (passing y to x). Another is is the kv language (passing value from Label 'settableLabel' to another Label).

Currently, I solve this by storing that kind of data in the top level App, but it seems kludgy. Any hints on how to do this better?

(Having the reference the other way around would work for me as well, of course. For instance, if MySecondScreen had a short cut to request the value of y from MyFirstScreen, that solves the problem as well.)