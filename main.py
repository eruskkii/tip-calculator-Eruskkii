#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
greeting = "Welcome to the tip calcualtor"
print (greeting)
total_bill = input("What was the total bill? $")

tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

bill_split = input("People split the bill? ")

tip_main = int(tip) / 100 + 1
final_bill = (float(total_bill) / int(bill_split)) * tip_main
final_bill_rounded = round(final_bill, 2)
final_bill_rounded = "{:.2f}".format(final_bill)

proposed_tip = f"Each person should pay: ${final_bill_rounded}"
print (proposed_tip)