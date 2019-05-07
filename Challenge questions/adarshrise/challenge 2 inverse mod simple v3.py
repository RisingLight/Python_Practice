def imod(inv, modnum):
 goal = 1
 while (goal % inv > 0):
     goal += modnum
     print(goal)
 return goal // inv
