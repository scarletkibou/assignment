Topping = {
    "Bubble": 5,
    "Grass Jelly": 10,
    "Red Bean": 15,
    "Wip Cream": 15
}
def choose_choice():
    choose=input("Select your topping(1/2/3/4):")
    while choose not in ["1","2","3","4"]:
        choose=input("Wrong Input please Enter 1,2,3,4: ")
    return choose

def choose_choice2(x):
    choose=x
    while choose== x:
        choose=input("Select your topping(1/2/3/4):")
        while choose not in ["1","2","3","4"]:
            choose=input("Wrong Input please Enter 1,2,3,4: ")
        if choose==x:
            print(choose_same_topping(choose,x))
    return choose

def choose_same_topping(x,y):
    if x==y:
        return ("You have already choose this topping please choose another choice!!!")

def add_topping(choice):
        if choice=="1":
            return "Bubble"
        elif choice=="2":
            return "Grass Jelly"
        elif choice=="3":
            return "Red Bean"
        elif choice=="4":
            return "Wip Cream"
    
def check_num_topping():
    num=int(input("How many toppings do you want (0 to 2)? "))
    while num<0 or num>2:
        num = int(input("Wrong Input you can type (0,1,2) only!! : "))
    return num

def get_topping():
    print("We have 4 toppings")
    print(Topping) 
    num_toppings = check_num_topping()
    toppingc=[]
    if num_toppings > 0 and num_toppings <=2:
        for i in range (num_toppings):
            if i==0:
                x=choose_choice()
                toppingc.append(add_topping(x))
            if i ==1:
                y=choose_choice2(x)
                toppingc.append(add_topping(y))
    elif num_toppings==0:
        return toppingc
    else:
        print("invalid input")
    return toppingc

def calculate_total_cost(toppings):
    total_cost = 25
    for topping in toppings:
        total_cost += Topping[topping]
    return total_cost

def cal_bill(bill,x):
    bill = bill+x
    return bill

def current_order(total_cost,toppings):
    order=[total_cost , toppings]
    return order

def print_total(x,y):
    return  f"You have ordered {x} Milk tea, Total cost is ${y} Thanks for purchasing!!!"

def check_bill(total_cost,toppings):
    return (f"Great! Your order with {', '.join(toppings)} costs ${total_cost}. Enjoy your milk tea!")
    