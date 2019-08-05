menu = {1 :['Cherry Coke', 2.75], 2 :['Orange Fanta', 2.50],3 :['7up', 2.25],4 :['Water', 1.25]}



def payment(dri,pri):
   pay = 0.00
   print('\n\nyou selected a ', dri , '\n Cost : $' ,str(pri))

   while(pay < pri):

     if pay== 0:
       pay += float(input("Insert\t: $"))
     else: 
       print('Missing: $', str(pri-pay))
       pay += float(input("Insert: $"))

   print("\n\nEnjoy your ", dri, "\n Your Payment: $", str(pay))   
   if pay > pri:
     print('your change is : $' , str(pay-pri))



     


def selection(choice):
 
  drink =''
  price=''
  
  if choice <= len(menu) or choice >0:

    #check for the choice
    if choice in menu:
      drink, price = menu[choice]
    else:
      print('invalid choice thank you')
  payment(drink , price )

   
def displaymenu():
  print("Vending machine Selection")

  for num in menu:
    drink, price = menu[num]
    print(str(num), ")" , drink, " Cost : $", str(price))

displaymenu()
sel = int(input("enter a selection: "))
selection(sel)


