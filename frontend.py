def return_a_car():
    print('==== return a car menu ===='.center(95))
    print('\r1. to return a car, enter your name:\n2. Back to main menu')
    return input("Please choose an option (1-2): ")

def admin_menu():
    print('==== Welcome to admin menu ===='.center(95))
    print(
        "\r1. Show car list \n"
        "2. Create rental car \n"
        "3. Update rental car \n"
        "4. Delete rental car \n"
        "5. Back to main menu")
    return int(input("Please choose an option (1-5): "))


def main_menu():
    print('==== Welcome to Rent-A-Car! How can we help? ===='.center(95))
    print("\r0.ADMIN \n1. Rent a car \n2. Return a car \n3. Exit")
    return input("Please choose an option (1-4): ")


# all_cars = [
#     {'id': '10', 'brand': 'Chrysler', 'model': 'Voyager', 'seats': '7', 'rental_price': '70', 'available': True},
#     {'id': '11', 'brand': 'Toyota', 'model': 'Aygo', 'seats': '5', 'rental_price': '30', 'available': True},
#     {'id': '12', 'brand': 'Citroen', 'model': 'C1', 'seats': '4', 'rental_price': '25', 'available': True},
#     {'id': '13', 'brand': 'Mercedes', 'model': 'Vito', 'seats': '9', 'rental_price': '120', 'available': True}]

# def show_car()):
#     while True
#         print('====Rental car menu===='. center(95))
#         print('\r1. Show available cars \n2. Rent a car \n3. back to main menu')

#     user_choice = input("Please choose an option (1-3): ")
#     if user_choice == 1:

#     if user_choice == 2:
#     if user_choice == 3:
