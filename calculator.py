def add(a,b):
        return a+b

def sub(a,b):
        return a-b

def mul(a,b):
        return a*b

def div(a,b):
        if b==0:
                return "zero cannot  not divsible"
        return a/b


while True:
        num1 = float(input("enter the number 1 :"))
        num2 = float(input("enter the number 2 : "))

        print(" 1. addition")
        print(" 2. subtraction")
        print(" 3. multiplication")
        print(" 4. division")
        print(" 5. exit")

        choice = int(input("enter the number to choice : "))


        if choice == 1:
        
                             print("Result :" , add(num1,num2))

        elif choice == 2:
                             print("Result :" , sub(num1,num2))


        elif choice == 3:
                            print("Result :" , mul(num1,num2))


        elif choice == 4:
                            print("Result : " , div(num1,num2))
        elif choice == 5:
                            print("exit")
                            break
        else:
              print("Invalid choice")
        

        