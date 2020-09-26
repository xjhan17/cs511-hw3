from z3 import *

# Translated from scheduling.smt2

A = Int('A')
At = Int('At')
B = Int('B')
Bt = Int('Bt')
C = Int('C')
Ct = Int('Ct')
D = Int('D')
Dt = Int('Dt')
E = Int('E')
Et = Int('Et')
F = Int('F')
Ft = Int('Ft')
End = Int('End')

A >= 0
At = 2
B >= 0
Bt = 1
C >= 0
Ct = 2
D >= 0
Dt = 2
E >= 0
Et = 7
F >= 0
Ft = 5
End = 14

phi1 = Or(((A+At)<=C), ((C+Ct)<=A))
phi2 = Or(((B+Bt)<=D), ((D+Dt)<=B))
phi3 = Or(((B+Bt)<=E), ((E+Et)<=B))
phi4 = Or(((D+Dt)<=E), ((E+Et)<=D))
phi5 = And(((D+Dt)<=F), ((E+Et)<=F))

s = Solver()
s.add((A+At)<=B)
s.add(A<=(End-At))
s.add(B<=(End-Bt))
s.add(C<=(End-Ct))
s.add(D<=(End-Dt))
s.add(E<=(End-Et))
s.add(F<=(End-Ft))


print (s.check())
print (s.model()[A], s.model()[B], s.model()[C],s.model()[D], s.model()[E], s.model()[F])