# Asking for user to input the sales amount and associate status
sales_amount = float(input("Enter the amount you sold in 2022: "))
associate_statues = str(input("Are you senior associate or junior associate? \nType s for senior associate and j for junior associate: "))

# For Juniors, rate

#sales below 5,000 = 0.03
#sales below 25,000 = 0.04
#sales below 100,000 = 0.05
#sales equals and above 100,001 = 0.07

#For Seniors, rate

#sales below 5,000 = 0.04
#sales below 25,000 = 0.05
#sales below 100,000 = 0.07
#sales equals and above 100,001 = 0.1

#For Junior associate

if associate_statues == "j":
  if sales_amount < 0:
    print("You made less than $0. Contact HR")
  elif sales_amount <= 5000:
    commission_amount1 = sales_amount * 0.03
    print(f" This year you made {commission_amount1} in sales commission.")
  elif sales_amount <= 25000:
    commission_amount2 = ((sales_amount-5000)*0.04) +(5000*0.03)
    print(f"This year you made {commission_amount2} in sales commission.")
  elif sales_amount <= 100000:
    commission_amount3 = ((sales_amount-25000)*0.05) + ((25000-5000)*0.04) +(5000*0.03)
    print(f"This year you made {commission_amount3} in sales commssion.")
  elif sales_amount  >=100001:
    commission_amount4 = ((sales_amount-100000)*0.07) + ((100000-25000-5000)*0.05) + (25000*0.04) + (5000*0.03)
    print(f"This year you made {commission_amount4} in sales commission.")

#For Senior associate
elif associate_statues == "s":
  if sales_amount < 0:
    print("You made less than $0. Contact HR")
  elif sales_amount <= 5000:
    commission_amount5 = sales_amount * 0.04
    print(f" This year you made {commission_amount5} in sales commission.")
  elif sales_amount <= 25000:
    commission_amount6 = ((sales_amount-5000)*0.05) +(5000*0.04)
    print(f"This year you made {commission_amount6} in sales commission.")
  elif sales_amount <= 100000:
    commission_amount7 = ((sales_amount-25000)*0.07) + ((25000-5000)*0.05) +(5000*0.04)
    print(f"This year you made {commission_amount7} in sales commssion.")
  elif sales_amount  >=100001:
    commission_amount8 = ((sales_amount-100000)*0.1) + ((100000-25000-5000)*0.07) + (25000*0.05) + (5000*0.04)
    print(f"This year you made {commission_amount8} in sales commission.")
