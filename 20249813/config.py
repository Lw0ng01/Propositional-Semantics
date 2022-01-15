
# DO NOT EDIT

# Assignment for 20lylw

from lib204 import wff
P, Q, R, S, T = map(wff.Variable, 'PQRST')
s1 = (~T>>~(Q|R))
s2 = ((Q|T)|(~Q>>~R))
s3 = (T|(R>>Q))
s4 = ((~R|T)&(T|~Q))

s5 = ((R>>S)>>(Q|(~R&S)))
s6 = ((R>>~(S|~Q))|(~Q&S))
