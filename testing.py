# creating a pakage
from pakage import calculator


cal=calculator.calc(
    a=30,
    b=40
)
print(f"this is added value {cal.addition()}")
print(f"this is substracted value {cal.substraction()}")
print(f"this is multiplied value {cal.multiplication()}")