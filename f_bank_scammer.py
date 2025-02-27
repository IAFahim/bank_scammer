added_on_each_deposite=5
total_amount=0

while(True):
    deposite_money = int(input("Enter your deposite please: "))
    total_amount += deposite_money
    
    if total_amount>=1000:
        print(f"The Bank is closed!!!! Last Balance {total_amount}")
        break

    total_amount += added_on_each_deposite
    print(f"Current balance: {total_amount}")
