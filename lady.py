import z3

#True: lady in room; False: tiger in room
Lady = [z3.Bool(f'room_{i}') for i in range(3)]
Note0 = z3.Not(Lady[0])
Note1 = Lady[1]
Note2 = z3.Not(Lady[1])
Note = [Note0, Note1, Note2]

One_note = z3.PbLe([(Note[i], True) for i in range(3)], 1)
One_lady = z3.PbEq([(Lady[i], True) for i in range(3)], 1)

#print out results whether each room contains lady
solver = z3.Solver()
solver.add(One_note, One_lady)
solver.check()
m = solver.model()
for lady in Lady:
    print(f'lady_{lady}: {m[lady]}')

#prove lady in room 0 by contradiction: add z3.Not(Lady[0])
solver1 = z3.Solver()
solver1.add(One_note, One_lady)
solver1.add(z3.Not(Lady[0]))
solver1.check()
print("Lady not in room 0: " , solver1.check())

#prove tiger in room 1 (lady not in room 1) by contradiction: add Lady[1]
solver2 = z3.Solver()
solver2.add(One_note, One_lady)
solver2.add(Lady[1])
solver2.check()
print("Tiger not in room 1: " , solver2.check())

#prove tiger in room 2 (lady not in room 2) by contradiction: add Lady[2]
solver3 = z3.Solver()
solver3.add(One_note, One_lady)
solver3.add(Lady[2])
solver3.check()
print("Tiger not in room 2: " , solver3.check())