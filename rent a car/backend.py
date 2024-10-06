import frontend


# def all_cars():
#     cars = [
#         {'id': '10', 'brand': 'Chrysler', 'model': 'Voyager', 'seats': '7', 'rental_price': '70', 'available': True},
#         {'id': '11', 'brand': 'Toyota', 'model': 'Aygo', 'seats': '5', 'rental_price': '30', 'available': True},
#         {'id': '12', 'brand': 'Citroen', 'model': 'C1', 'seats': '4', 'rental_price': '25', 'available': True},
#         {'id': '13', 'brand': 'Mercedes', 'model': 'Vito', 'seats': '9', 'rental_price': '120', 'available': True}]
#     return cars


def rent_a_car(a):
    tenant = str(input('What is your name?: '))
    index = 0
    for car in all_cars:
        if str(a) == car['id']:
            if not car['available']:
                print('Car is not available')
                return available_cars()
            else:
                all_cars[index]['available'] = False
                all_cars[index]['tenant'] = tenant
                print(f'Hello {tenant}, you rent a car with ID:{car["id"]},'
                      f' brand:{car["brand"]}, model:{car["model"]}. Have a nice trip!')
                return user_main_menu()
        else:
            index += 1


def available_cars():
    print('==== Here you can rent a car ===='.center(95))
    print('==== Those cars are available ====\n'.center(95))
    total_available_cars = 0
    for count in all_cars:
        if count['available']:
            total_available_cars += 1
    if total_available_cars == 0:
        print('Sorry, we don\'t have available cars for rent')
        return user_main_menu()
    else:
        print(f'We have {total_available_cars} available cars for rent!:')
    for car in all_cars:
        if car['available']:
            for a, b in car.items():
                if a != 'available' and a != 'tenant':
                    print(f'{a}: {b},', end="  ")
            print()
    user_choice = int(input('Enter the chosen car id or 1 for main menu: '))

    while True:
        if 10 <= user_choice <= 20:
            return rent_a_car(user_choice)
        elif user_choice == 1:
            user_main_menu()
            break
        else:
            print("Invalid choice!")
            user_choice = int(input("Please choose an id or 1 for main menu: "))
            continue


def user_return_a_car():
    user_choice = frontend.return_a_car()
    id_of_rented_car = ''
    if user_choice == '2':
        user_main_menu()
    else:
        for car in all_cars:
            if car['tenant'] == str(user_choice):
                print()
                print('You have rented: ', end='')
                for a, b in car.items():
                    if a != 'available' and a != 'tenant':
                        print(f'{a}: {b},', end='')
    print()
    id_of_rented_car = input('Id of the car you want to return:')
    index = 0
    for rented_car in all_cars:
        if id_of_rented_car == rented_car['id'] and rented_car['tenant'] == str(user_choice):
            all_cars[index]['available'] = True
            all_cars[index]['tenant'] = ''
            print(f'You have returned {rented_car["brand"]} {rented_car["model"]}.')
            return user_main_menu()
        else:
            index += 1


def user_main_menu():
    # user_choice = int((input("Please choose an option (1-4): ")))
    user_choice = int(frontend.main_menu())
    attempts = 1
    while True:
        if 0 <= user_choice < 5:
            if user_choice == 0:

                # Admins Password Is pass123

                password = input('Enter admin\'s password: ')
                if password == 'pass123':
                    user_admin_menu()
                    break
                if attempts == 3:
                    print('Too many tries!')
                    break
                else:
                    print('Invalid password! Please try again: ')
                    attempts += 1
                    continue
            if user_choice == 1:
                available_cars()
            if user_choice == 2:
                user_return_a_car()
                break
            if user_choice == 3:
                break
        else:
            print("Invalid choice!")
            user_choice = int(input("Please choose an option (1-4): "))
            continue


def user_admin_menu():
    user_choice = frontend.admin_menu()
    while True:
        if 0 <= user_choice < 6:
            if user_choice == 1:
                print(all_cars)
            elif user_choice == 2:
                user_main_menu()
            elif user_choice == 3:
                user_main_menu()
            elif user_choice == 4:
                user_main_menu()
            elif user_choice == 5:
                user_main_menu()
            break
        else:
            print("Invalid choice!")
            user_choice = int(input("Please choose an option (1-5): "))
            continue


all_cars = [
    {'id': '10', 'brand': 'Chrysler', 'model': 'Voyager', 'seats': '7', 'rental_price': '70', 'available': True,
     'tenant': ''},
    {'id': '11', 'brand': 'Toyota', 'model': 'Aygo', 'seats': '5', 'rental_price': '30', 'available': True,
     'tenant': ''},
    {'id': '12', 'brand': 'Citroen', 'model': 'C1', 'seats': '4', 'rental_price': '25', 'available': True,
     'tenant': ''},
    {'id': '13', 'brand': 'Mercedes', 'model': 'Vito', 'seats': '9', 'rental_price': '120', 'available': True,
     'tenant': ''}]

user_main_menu()

# index = 0
# rented_cars = []
# for a in cars_offered():
#     for i in a:
#         if frontend.rented_id == a[i] and i == 'id':
#             rented_cars.append(a)
#             rented_cars[index]['available'] = False
#             index += 1
#             print(rented_cars)

# if cars_offered()[frontend.rented_id - 1]['available'] == False:
#     print('Yes')
# else:
#     print('No')


# for rent_car in cars_offered():
#     if frontend.rented_id == 2:

# if rent == 1:
#     cars_offered([1])
#     print(cars_offered())
# for car in cars_offered():
#     if car['available']:
#         print(f'{car["brand"]} {car["model"]}')
