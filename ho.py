store_database=[]
user_input = 0
while user_input != 5:
    print("pella store list")
    user_input = int(input("1.buy item \n"
                           "2.view cart \n"
                           "3. remove from cart \n"
                           "4. make purchase \n"
                           "5.about us \n"
                           "6.exit app \n"
                           "choose option"))
    store=0
    if user_input == 1:
        store=str(input ("enter product"))
        store=int(input ("quantity product"))
        atore=input("unit price")
        store_database.append(store)
    elif user_input == 2:
        if len(store_database)<=0:
         print("viewed successfully")    
    elif user_input ==3:
        if len(store_database)<=0:
         store=str(input("enter item to remove"))
         store_database.remove(store)
         print("remove cart")
    elif user_input ==4:
        total_amount = sum(store["product"] + store["quantity product"] + store["unit price"])
    elif user_input ==5:
        store=input("enter payment")
        store_database.append(store)
    elif user_input ==6:
        store=input("about us")
        continue
    else:
        print("exit app")



        

        







