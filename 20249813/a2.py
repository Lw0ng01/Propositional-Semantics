# This is your unique solution file

from config import *
from lib204 import semantic_interface

# Assignment for 20lylw

# Note: All of these answers are almost certainly wrong

a2q12 = [ [s1, s4], [s2, s3] ]

a2q13 = {
    Q: False,
    R: False,
    T: False
}

a2s5nnf = [
    [((R >> S) >> (Q | (~R & S))), 'starting formula'],
    [(~(~R | S) | (Q | (~R & S))), 'removing implications'],
    [((~~R & ~S) & (Q | (~R & S))), 'de morgans, push negation in'],
    [((R & ~S) & (Q | (~R & S))), 'de morgans, removed double negation'],
]

a2s6nnf = [
    [((R >> ~(S | ~Q)) | (~Q & S)), 'starting formula'],
    [((~R | ~(S | ~Q)) | (~Q & S)), 'removing implications'],
    [((~R | (~S & ~~Q)) | (~Q & S)), 'de morgans, push negation in'],
    [((~R | (~S & Q)) | (~Q & S)), 'remove double negations'],
]

a2s5cnf = [
    [((R >> S) >> (Q | (~R & S))), 'starting formula'],
    [((R & ~S) & (Q | (~R & S))), 'convert to NNF like above'],
    [((~R | S) & ((Q | ~R) & (Q | S))), 'apply distribution'],
]

a2s6cnf = [
    [((R >> ~(S | ~Q)) | (~Q & S)), 'starting formula'],
    [((~R | (~S & Q)) | (~Q & S)), 'convert to NNF like above'],
    [(~R | ~S | ~Q) & (~R | Q | S), 'apply distribution']
]

a2s5tseitin = semantic_interface.Encoding()
# Fill in the Tseitin steps and finalize
x1 = a2s5tseitin.tseitin(~R, 'x1')
x2 = a2s5tseitin.tseitin(x1 & S, 'x2')
x3 = a2s5tseitin.tseitin(Q | x2, 'x3')
x4 = a2s5tseitin.tseitin(R >> S, 'x4')
x5 = a2s5tseitin.tseitin(x4 >> x3, 'x5')
a2s5tseitin.finalize(x5)  # make sure you update the variable!

a2s6tseitin = semantic_interface.Encoding()
# Fill in the Tseitin steps and finalize
x1 = a2s6tseitin.tseitin(~Q, 'x1')
x2 = a2s6tseitin.tseitin(x1 & S, 'x2')
x3 = a2s6tseitin.tseitin(S | x1, 'x3')
x4 = a2s6tseitin.tseitin(x3 | x2, 'x4')
x5 = a2s6tseitin.tseitin(~x4, 'x5')
x6 = a2s6tseitin.tseitin(R >> x5, 'x6')
a2s6tseitin.finalize(x6)  # make sure you update the variable!
