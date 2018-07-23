# PythonToolbox
Various python scripts to make my analysis life easier

various dependencies (depending on the script):
ROOT
decimal
itertools - chain
gc
os
imp
math
rootpy


----The main script that may be useful for other people is round20.py

It is used to round a number and its error according to the rule of 20
It uses a messy algamation of strings, lists and ints to do the rounding.
The actual rounding is done over the number turned into a list of characters, 
and is converted back into a float or whatnot at the end. Note: can take care
most numbers including decimal and exponential formats, but fails for certain cases.
Those cases it fails for still need to be determined and added to the messy if; then chain.
