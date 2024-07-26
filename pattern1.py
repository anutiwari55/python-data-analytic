from turtle import *
speed('slowest')
pencolor('orange')
bgcolor('white')
total = 0
while total < 1000:
    total += 5
    fd(total)
    lt(70)

mainloop()