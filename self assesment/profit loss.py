#program to calculate profit or loss based on cost price and selling price
#input of cost price
cp = float(input("Enter cost price (in Rs): "))
#to validate cost price
if(cp <= 0):
print("Invalid cost price")
exit() #exiting the program if cost price is invalid
else:
#input of selling price
sp = float(input("Enter selling price (in Rs): "))
#to validate selling price
if(sp <= 0):
print("Invalid selling price")
exit() #exiting the program if selling price is invalid
else:
#calculating profit or loss
if(sp > cp):
print("Profit: Rs", (sp-cp))
elif(cp > sp):
print("Loss: Rs", (cp-sp))
else:
print("No profit no loss")