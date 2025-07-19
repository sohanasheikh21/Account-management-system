import json
with open('balance.json','r') as files:
   data=json.load(files)
def deposit():
  global data
  while True:
    amount=int(input("Enter the amount you want to deposit:"))
    if amount>0:
        data['balance'] +=amount
        with open('balance.json','w') as file_s:
            json.dump(data,file_s)
        print("Deposited Successfully ✅")
        check_balance()
        break
    else:
        print("Try again! You entered invalid❌ amount")
def withdraw():
  global balance
  while True:
    amount=int (input("Enter the amount you want to withdraw:"))
    if amount>0:
        if amount>=data['balance']:
            data['balance']+=amount
            with open('balance.json','w') as file:
                json.dump(data,file)
            print("Withdraw Successful✅")
            print("Want to check balance ?)",end='')
            balance_check=input("Enter (yes/no): ").lower()
            if balance_check=="no":
                check_balance()
                break
            else:
                print("Thanks for visiting")
                break
        else:
            print("Not sufficient balance❌")
            break
    else:
        print("Try again! You entered invalid❌ amount")
   
def check_balance():
    print(f"Your account balance: {data['balance']}rs")
    print("Thanks for visiting")