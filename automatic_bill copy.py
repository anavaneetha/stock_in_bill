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
Milk Rs 30/ltr
Cloth Rs 50/mtr 
Banana Rs 20/dzn 


'''
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
gst=[]
uomlist=[]
glist=[]


items={
    'Tomato':{'price':20, 'gst':4,'uom':'kg' },
    'Milk':{'price':30, 'gst':5 ,'uom':'ltr'},         
    'Cloth':{'price':50, 'gst':6,'uom':'mtr'},
    'Banana':{'price':20, 'gst':3,'uom':'dzn'},
    
      }


option=int(input('for list of items press 1:'))
if option==1:
    print(lists)


    for i in range(len(items)):
     while True:
    
      inp1=int(input('if you want to buy press1 or 2 for exit:'))
      if inp1==2:
         
        break
   
      if inp1==1:
       
        item=input('Enter your items:')


        if item == "tomato":
         quantity = float(input("Enter the weight of tomatoes in kilograms: "))
         item=item.title()

        elif item == "milk":
         quantity = float(input("Enter the volume of milk in liters: "))
         item=item.title()
        elif item == "banana":
         quantity = float(input("Enter the quantity of bananas in dozens: "))
         item=item.title()

        elif item == "cloth":
         quantity = float(input("Enter the length of cloth in meter: "))


         item=item.title()

        # quantity=int(input('Enter quantity:'))
         
        if item in items:
            price=quantity*(items[item]['price'])
        

            pricelist.append((item,quantity,items,price,gsttotal,(items[item]['uom']),(items[item]['gst'])))
           
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            uomlist.append((items[item]['uom']))
            glist.append((items[item]['gst']))
           
            gst = price * (items[item]['gst'])/100
           
         
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
    
    
        if finalamount!=0:
            print(25*'=','Reliance Smart',25*'=')
            print(28*' ','Hyderabad')
            print('Name:',name, 30*' ','Date:',datetime.now())
            print('Mobilenum:',mobile_no)

          
            print(75*'-')
            print('sno',8*' ','Items',8*' ','UOM',8*' ','Quantity',3*' ','Price',3*' ' ,'GST amount%',3*' ' ,'GST amount',3*' ' ,)
            for i in range(len(pricelist)):
                print(i+1,10*' ',ilist[i],5*' ',uomlist[i],10*' ',qlist[i],10*' ',plist[i],10*' ',glist[i],'%',10*' ',gstlist[i])
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

      