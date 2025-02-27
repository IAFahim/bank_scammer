
bank_account_openning_money=5
total_amount=0
count=1
while(total_amount<1000):
    deposite_money = int(input("Enter your amount please: "))
    total_amount+=deposite_money+((bank_account_openning_money*count))
    count+=1


if deposite_money>=1000:
    print(f"The saving amount is {total_amount}")

else:
    print(f"The saving amount is {total_amount}.The Bank is closed!!!!")