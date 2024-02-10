import filehandler as f

def stock_replenishment():
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
