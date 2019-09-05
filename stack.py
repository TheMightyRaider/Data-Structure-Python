# -------- USING CLASS --------

class Stack():
    def __init__(self):
        self.data=[]

    def insert(self):
        print('Enter the Size :')
        size=int(input())
        for quantity in range(0,size):
            number=int(input())
            self.data.append(number)

    def pop():
        print('Enter the number of elements to be removed :')
        number_of_pop=int(input())
        for pops in range(number_of_pop):
            self.data.pop()
    
    def display():
        print(self.data)
         
def choice():
    print('Choose an Operation')
    print('1. Insert')
    print('2. Delete')
    print('3 .Display')
    print('4. Exit')
    def options():
        x=int(input())
        if(x==1):
            stack.insert() 
            choice()
        elif(x==2):
            stack.delete()
            choice()
        elif(x==3):
            stack.display()
            choice()
        elif(x==4):
            pass
        else:
            print('Wrong Input')
    options()

stack=Stack()
choice()

# -------- USING FUNCTION --------

# a=[]
# x=int(input())

# def push(x):
#     for number in range(0,x):
#         num=int(input())
#         a.append(num)

# def removeanumber(remove_number):
#     for number in range(remove_number):
#         a.pop()

# def display():
#     print(a)

# print('Inserting a Number')
# push(x)
# print('How many number do you wanna remove ?')
# remove_number=int(input())
# print(f'Removing {remove_number} Number')
# removeanumber(remove_number)
# print('Displaying the list')
# display()
