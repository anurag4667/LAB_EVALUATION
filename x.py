
database ={}

while(True):

    print("\n\n select the following option")
    print("1. add contact")
    print("2. update contact")
    print("3. delete contact")
    print("4. show contacts")
    print("5. search contacts")
    print("6. contacts with initital letters")
    print("press any other key to exit \n\n")

    ch = int(input("enter your choice"))
    if(ch == 1):
        name = input("enter name").lower()
        pno = int(input("enter phone number"))

        data = []
        data.append(pno)

        email = input("email available ? yes or no").lower()
        if(email == "yes"):
            email = input("enter your email ")
        else:
            email = "na"
        
        data.append(email)

        database[name] = data
    elif(ch == 2):
        name = input("enter your name").lower()

        if(name not in database):
            print("name not found")
        else:
            print("enter the details to be updated")
            print("1. pno")
            print("2. email")

            f = int(input("enter your choice"))
            if(f == 1):
                pno = int(input("enter your number"))
                database[name][0] = pno
            if(f == 2):
                email = input("enter your email").lower()
                database[name][1] = email

    elif(ch == 3):
        name = input("enter your name").lower()

        if(name in database):
            database.pop(name)

        print("contact deleted")

    elif(ch == 4):

        for i in database:
            print(i + " " ,end = " ")
            print(database[i])

    elif(ch == 5):
        print("search contact")
        print("1. name")
        print("2. email")

        f = int(input("enter your choice"))
        if(f == 1):
            name = input("enter your name").lower()
            if(name in database):
                print(name + " : ",end = "")
                print(database[name])
            else:
                print("contact not found")
        if(f == 2):
            email = input("enter your email").lower()

            for i in database:
                if(database[i][1] == email):
                    print("contact found ")
                    print(i + " : ",end = "")
                    print(database[i])
                    break
            else :
                print("contact not found ")
            
    elif(ch == 6):
        
        x = input("enter the starting charater").lower()

        l = len(x)

        for i in database:
            if(i[:l] == x):
                print(i + " : ",end = "")
                print(database[i])
        
    else:
        break
