def add(num1,num2):
    anadd = num1 + num2
    return anadd
def sub(num1,num2):
    ansub = num1 - num2
    return ansub
def mul(num1,num2):
    anmul = num1 * num2
    return anmul
def div(num1,num2):
    andiv = num1/num2
    return andiv

num1 = int(input("number"))
num2 = int(input("number"))
decision = input("What do you wish to do? Add, Sub, Mul or Div.")
decisionx=decision.lower()
if decisionx== "add":
    print(add(num1,num2))
elif decisionx == "sub":
    print(sub(num1,num2))
elif decisionx == "mul":
    print(mul(num1,num2))
elif decisionx == "div":
    print(div(num1,num2))
else:
    print("Improper input")
