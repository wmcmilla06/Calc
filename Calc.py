print("CalcMachine 1.0")
print("Select a job for the calculator")
start = input("Job:")
if start == "basic math":
    
    n1 = input("Enter first number:")
    n2 = input("Enter second number:")
    opbasic = input("Enter operation:")
    if opbasic == "+":
        add = int(n1)+int(n2)
        print(add)

    if opbasic == "-":
        subtract = int(n1)-int(n2)
        print(subtract)

    if opbasic == "*":
        multiply = int(n1)*int(n2)
        print(multiply)
    
    if opbasic == "/":
        divison = int(n1)/int(n2)
        print(divison)
if start == "circle area":
    pi = 3.14
    radius = input("Enter Radius:")
    circleArea = int(radius)*int(radius)*pi
    print(circleArea)
if start == "square area":
    sside = input("Enter side length:")
    sqArea = int(sside)*int(sside)
    print(sqArea)
    
if start == "triangle area":
    basE1 = "Enter base:"
    height1 = "Enter height:"
    triAngleArea = 0.5*int(basE1)*int(height1)
    print("TriAngleArea")


    
    
