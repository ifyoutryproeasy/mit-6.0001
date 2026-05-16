#MIT 6.0001 - Lecutre 1
#Heron's Algorithm for computing square roots
s = 47
g = 3
nariivchlal = 0.001
while abs(g*g-s) > nariivchlal:
    g = (g + s/g)/2
    print(g)

print(f"47-ийн квадрат язгуур нь ойролцоогоор {g} байна.")
print(f"шалгах: {g} x {g} = {g*g}")