import filehandler

#Used to search the groceries.txt file based on user criteria.
#A Few options are: Item Description, Code Range, Category, Price Range
def search():
    run = "Y"
    while run == "Y":
        print("\nChoose what you would like to search by: \n \t1. Item Description \n\t 2. Code Range \n\t 3. Category "
              "\n\t 4. Price Range ")
        choice = int(input("Choice: "))

        #Searching by Description
        if choice == 1:
            description = input("Enter the description you are looking for: ")
            exist = False
            with open("groceries.txt", "r") as file:
                for line in file:
                    details = line.split()
                    if description.lower() in details[1].lower():
                        print(line)
                        exist = True
            if not exist:
                print("Sorry the item with that description does not exist")

        #Searching by Code Range
        elif choice == 2:
            exist = False
            up_range = int(input("\nEnter upper code range: "))
            low_range = int(input("Enter lower code range: "))
            with open("groceries.txt", "r") as file:
                for line in file:
                    details = line.split()
                    if low_range <= int(details[0]) <= up_range:
                        print(line)
                        exist = True
            if not exist:
                print("Sorry, item code in that range does not exist")

        #Searching by Category
        elif choice == 3:
            exist = False
            print("\tVegetable \n\tFruit \n\tSnacks \n\tDairy \n\tMeat")
            categ = (input("Choose a Category: "))
            with open("groceries.txt", "r") as file:
                for line in file:
                    details = line.split()
                    if details[2] == categ:
                        print(line)
                        exist = True
            if not exist:
                print("Sorry, item in that category does not exist")

        #Searching by Price Range
        elif choice == 4:
            exist = False
            price_low = float(input("\nEnter lower price range: "))
            price_up = float(input("Enter upper price range: "))
            with open("groceries.txt", "r") as file:
                for line in file:
                    details = line.split()
                    if price_low <= float(details[4]) <= price_up:
                        print(line)
                        exist = True
            if not exist:
                print("Sorry, item code in that range does not exist")

        run = input("\n\t Enter Y to search again, press any other key to exit: ")

#Defining a function to modify the quantities of stock
def stock_take():
    run = "Y"
    while run == "Y":
        item_code = input("Enter item code: ")
        with open("groceries.txt", "r") as file:
            found = False
            for line in file:
                details = line.split()
                if item_code == details[0]:
                    found = True
                    print("Item:", details[1])
                    print("Available quantity:", details[5])
                    new_quantity = input("Enter new quantity: ")
                    details[5] = new_quantity
                    break
        if not found:
            print("Item does not exist.")
            return
        with open("groceries.txt", "r") as file:
            lines = file.readlines()
        with open("groceries.txt", "w") as file:
            for line in lines:
                if item_code == line.split()[0]:
                    file.write("\t".join(details) + "\n")
                else:
                    file.write(line)
        print("Quantity updated successfully.")

        run = input("\n\t Enter Y to modify again, press any other key to exit: ")
