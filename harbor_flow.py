def show_menu():
    print("HARBORFLOW DISPATCH CONSOLE")
    print("1. Close console")
    print("2. Validate booking reference")
    print("3. Calculate delivery quote")
    print("4. Consolidate parcel labels")
    print("5. Check van capacity")
    print("6. Classify service performance")
    print("7. Produce weekly dispatch report")


def task_validate_reference():
    print("(Task 2 not implemented yet)")

def calculate_quote(distance, weight, service_code):
    subtotal = 45.00 + distance * 6.50 + weight * 4.00

    if service_code == "S":
        service_multiplier = 1.00
    elif service_code == "X":
        service_multiplier = 1.25
    else:
        service_multiplier = 1.60

    quote = subtotal * service_multiplier
    return quote


def delivery_quote():
    distance = float(input("Distance (km): "))
    weight = float(input("Weight (kg): "))
    service_code = input("Service code: ").strip().upper()

    quote = calculate_quote(distance, weight, service_code)

    print(f"Delivery quote: {quote:.2f} SEK")




def task_consolidate_labels():
    print("(Task 4 not implemented yet)")


def task_check_capacity():
    print("(Task 5 not implemented yet)")


def task_classify_performance():
    promised = int(input("Promised minutes: "))
    actual = int(input("Actual minutes: "))
    damaged = int(input("Damaged parcels: "))
    classify_performance(promised, actual, damaged)


def classify_performance(promised, actual, damaged):
    delay = actual - promised
    if damaged > 0:
        status = "SERVICE FAILURE"
    elif delay <= 0:
        status = "ON TIME"
    elif delay <= 15:
        status = "MINOR DELAY"
    else:
        status = "MAJOR DELAY"
    print("Delay:", delay, "minutes")
    print("Service status:", status)


def task_weekly_report():
    print("(Task 7 not implemented yet)")


def main():
    running = True
    while running:
        show_menu()
        choice = int(input("Select service: "))

        if choice == 1:
            print("Console closed. Dispatch data remains safe.")
            running = False
        elif choice == 2:
            task_validate_reference()
        elif choice == 3:
            task_calculate_quote()
        elif choice == 4:
            task_consolidate_labels()
        elif choice == 5:
            task_check_capacity()
        elif choice == 6:
            task_classify_performance()
            running = False
        elif choice == 7:
            task_weekly_report()


if __name__ == "__main__":
    main()
