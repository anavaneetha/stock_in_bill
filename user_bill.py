from datetime import datetime
name=input('Enter your name:')


while True:
    mobile_no = input("Enter your mobile no : ")
    if not mobile_no.isdigit() or len(mobile_no) != 10:
        print("You entered an invalid mobile no. Please enter a valid 10-digit mobile no.")
    else:
        break


# Lists of items

lists='''

Tomato Rs 20/kg
Potato Rs 30/kg
Onion Rs 50/kg
Garlic Rs 20/kg
Ginger Rs 60/kg


'''


# lists=['Tomato Rs 20/kg','Potato Rs 30/kg','Onion Rs 50/kg','MiLk' ]

# for li in lists:
#     if li.lower()==li.lower():
#         print(li)
#     else:
#         pass


# print(lists)

#declaration
gsttotal=0
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
gstlist=[]
gstper=[]
uom=[]

#rates for items
# items={'Tomato'or 'tomato'or 'TOMATO':20, 'Potato'or 'potato'or'POTATO':30, 'Onion'or'onion'or 'ONION':50, 
#        'Garlic'or 'GARLIC'or 'garlic':20, 'Ginger'or 'GINGER'or 'ginger':60}
items={'Tomato':20, 'Potato':30, 'Onion':50, 'Garlic':20, 'Ginger':60}
# *************************************************
# while True:
#     items.lower()=='done' or items.lower()=='d':
#    break
# #    item=item.lower()
#    if item not in items:
#         print("Sorry, we don't have that item in stock.") 

# *************************************************


option=int(input('for list of items press 1:'))
if option==1:
    print(lists)
# bill{}

for i in range(len(items)):
    inp1=int(input('if you want to buy press1 or 2 for exit:'))
    if inp1==2:
         
        break
   

    if inp1==1:
        # if items.keys().lower()==items.keys().upper()==items.keys().title():
      
        item=input('Enter your items:')

        uom=input('Enter your uom:')

        item=item.title()

        quantity=int(input('Enter quantity:'))
        # gstper=float(int(input('Enter the % charged for gst:')))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price,gsttotal))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gstper=float(int(input('Enter the % charged for gst:')))
            # gstper=int(input('Enter the % charged for gst:'))
            # print(gstper)
          
            # gst=(price*5)/100
            gst = price * (gstper)/100
            gsttotal=gsttotal+gst
            # gst=(totalprice*5)/100
            gstlist.append(gst)
            finalamount=gsttotal+totalprice
            # GSTamount=gst
        else:
            print('sorry you entered item is not available')
    else:
        print('you entered wrong number')
    
    inp=input('Proceed for billing! yes or no :')
    if inp.lower == "no" or inp.lower == "n":
        break
    elif inp=='yes' or inp=='YES' or inp=='y' or inp=='Y':
    # elif inp.lower == "yes" or inp.lower == "y":
        # pass
        # break
    # bill[item] = bill.get(item,0) + quantity
   

    
        if finalamount!=0:
            print(25*'=','Reliance Smart',25*'=')
            print(28*' ','Hyderabad')
            print('Name:',name, 30*' ','Date:',datetime.now())
            print('Mobilenum:',mobile_no)

          
            print(75*'-')
            print('sno',8*' ','Items',8*' ','UOM',8*' ','Quantity',3*' ','Price',3*' ' ,'GST amount%',3*' ' ,'GST amount',3*' ' ,)
            for i in range(len(pricelist)):
                print(i+1,10*' ',ilist[i],5*' ',uom,10*' ',qlist[i],10*' ',plist[i],10*' ',gstper,'%',10*' ',gstlist[i])
            print(75*'-')
            print(50*' ','TotalAmount:','Rs',totalprice)
            print(50*' ','GSTtotal:','Rs',gsttotal)
            # print('GSTtotal',40*' ','Rs',gsttotal)
            print(75*'-')
            print(50*' ','FinalAmount:','Rs',finalamount)
            print(75*'-')
            print(20*' ','Thanks for visiting')
            print(75*'-')
            break

      