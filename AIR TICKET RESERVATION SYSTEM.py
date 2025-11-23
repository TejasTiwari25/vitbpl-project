PDATA = []  # List to store customer registration data
CLASSTYPE = [(1, 'First class', 6000),
    (2, 'Business class', 4000),
    (3, 'Economy class', 2000)]
FOOD = [(1, 'tea', 10), (2, 'coffee', 10), (3, 'colddrink', 20),
    (4, 'samosa', 10), (5, 'sandwich', 50), (6, 'dhokla', 30),
    (7, 'kachori', 10), (8, 'milk', 20), (9, 'noodles', 50),
    (10, 'pasta', 50)]
LUGGAGE_RATE = 1000 # Rate per kg of extra luggage
s = 0  # Stores Ticket and Food Bill total
z = 0  # Stores Luggage Bill total
def registercust():
    global PDATA
    print("\n--- New Customer Registration ---")
    name = input("Enter name: ")
    addr = input("Enter address: ")
    jr_date = input("Enter date of journey: ")
    departure = input("Enter departure: ")
    destination = input("Enter destination: ")
    customer_data = {'custname': name, 'addr': addr, 'jrdate': jr_date, 
                     'departure': departure, 'destination': destination}
    PDATA.append(customer_data)
    print("Customer data saved.")
def classtypeview():
    print("\n--- View Available Classes ---")
    print(f"{'S.No':<5}{'Class Type':<15}{'Price (PN)':>10}")
    for sno, class_type, price in CLASSTYPE:
        print(f"{sno:<5}{class_type:<15}{price:>10}")
def ticketprice():
    global s
    print("\n--- Ticket Price Calculation ---")
    classtypeview()
    try:
        x = int(input("Enter Your Choice Please (S.No) -> "))
        n = int(input("No of passenger: "))
        selected_class = next((item for item in CLASSTYPE if item[0] == x), None)
        if selected_class:
            price = selected_class[2]
            s = price * n
            print(f"Total ticket amount is = {s}")
        else:
            print("Invalid class choice.")
            s = 0
    except ValueError:
        print("Invalid input.")
def menuview():
    print("\n--- View Food Menu ---")
    print(f"{'S.No':<5}{'Item Name':<15}{'Rate':>10}")
    for sno, item_name, rate in FOOD:
        print(f"{sno:<5}{item_name:<15}{rate:>10}")
def orderitem():
    global s
    print("\n--- Food Order & Bill ---")
    menuview()
    try:
        d = int(input("Enter S.No of item to purchase: "))
        selected_item = next((item for item in FOOD if item[0] == d), None)
        if selected_item:
            rate = selected_item[2]
            a = int(input(f"Enter quantity: "))
            current_bill = rate * a
            s += current_bill
            print(f"Item amount: {current_bill}. Current total bill (s): {s}")
        else:
            print("Invalid item choice.")
    except ValueError:
        print("Invalid input.")
def lugagebill():
    global z
    print("\n--- Luggage Bill Calculation ---")
    try:
        y = int(input("Enter the weight of extra luggage (in kg) -> "))
        z = y * LUGGAGE_RATE
        print(f"Your luggage bill: {z}")
        return z
    except ValueError:
        print("Invalid input.")
def totalamount():
    global s, z
    print("\n--- Complete Bill Summary ---")
    print(f"Ticket/Food Total (s): {s}")
    print(f"Luggage Bill (z): {z}")
    total = s + z
    print(f"*** GRAND TOTAL AMOUNT: {total} ***")
def main_menu():
    print("\n===== ✈️ AIR TICKET RESERVATION SYSTEM ✈️ =====")
    print("Enter 1: To enter customer data")
    print("Enter 2 : To view class types")
    print("Enter 3 : For ticket amount calculation")
    print("Enter 4 : For viewing food menu")
    print("Enter 5 : For food bill calculation")
    print("Enter 6 : For luggage bill calculation")
    print("Enter 7 : For complete amount summary")
    print("Enter 8 : For EXIT")
    print("=" * 50)
    try:
        userinput = int(input("Enter your choice: "))
    except ValueError:
        print("\nInvalid choice. Please enter a number.")
        return
    if userinput == 1:
        registercust()
    elif userinput == 2:
        classtypeview()
    elif userinput == 3:
        ticketprice()
    elif userinput == 4:
        menuview()
    elif userinput == 5:
        orderitem()
    elif userinput == 6:
        lugagebill()
    elif userinput == 7:
        totalamount()
    elif userinput == 8:
        print("Exiting the system. Goodbye!")
        quit()
    else:
        print("Please enter a correct choice.")
def run_program():
    import os
    import platform
    while True:
        main_menu()
        run_agn = input("\nWant to run again (y/n): ")
        if run_agn.lower() != 'y':
            break
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
if __name__ == "__main__":
    run_program()