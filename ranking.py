import z3

M = z3.Int('Mary')
B = z3.Int('Bob')
J = z3.Int('Jim')
L = z3.Int('Lisa')
BM = z3.Bool('Biology Mary')
BB = z3.Bool('Biology Bob')
BJ = z3.Bool('Biology Jim')
BL = z3.Bool('Biology Lisa')
people = [M, B, J, L]
bio = [BM, BB, BJ, BL]

solver = z3.Solver()
for person in people:
    solver.add(1 <= person)
    solver.add(person <= 4)

solver.add(z3.Distinct(people))

#Fact 1
solver.add(z3.And((L-B) != 1, (B-L) != 1))
#Fact 2
solver.add(z3.Implies((M-J) == 1, BM))
solver.add(z3.Implies((L-J) == 1, BL))
solver.add(z3.Implies((B-J) == 1, BB))
#Fact 3
solver.add((J-B) == 1)
#Fact 4
solver.add(z3.Or(BM, BL))
#Fact 5
solver.add(z3.Or(L == 1, M == 1))

solver.check()
m = solver.model()
for person in people:
    print(f'{person}: {m[person]}')