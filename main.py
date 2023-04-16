from function import *


print("Welcome to Milk Tea shop!!!")
order=[]
bill=0
i=0
check=input("Would you like a Milk Tea?(y/n):")
while check=="y":
    i+=1
    toppings=get_topping()
    total_cost = calculate_total_cost(toppings)
    order.append(current_order(total_cost,toppings))
    print(check_bill(total_cost,toppings))
    bill = cal_bill(bill,total_cost)
    check=input("Would you like to order another cup?(y/n):")
else: print("Hope to see you next time!!!")
print(print_total(i,bill))
        


