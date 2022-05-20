"""
2.2.1.1 PROJECT: Vintage cars database
https://edube.org/learn/pcpp1-working-with-restful-apis/project-vintage-cars-database
"""
import requests
import json


def check_server(cid=None):
    """
    Returns True or False;
    When invoked without arguments simply checks if server responds;
    Invoked with car ID checks if the ID is present in the database;
    """
    if cid is None:
        try:
            reply = requests.get("http://localhost:3000/cars")
        except requests.RequestException:
            print("Communication error")
            return False
        else:
            if reply.status_code == requests.codes.ok:
                return reply.json()
            else:
                print("Server error")
                return False
    else:
        try:
            reply = requests.get("http://localhost:3000/cars")
        except requests.RequestException:
            print("Communication error")
            return False
        else:
            if reply.status_code == requests.codes.ok:
                ids_list = [tag['id'] for tag in reply.json()]
                return True if cid in ids_list else False
            else:
                print("Server error")
                return False


def print_menu():
    """
    Prints user menu - nothing else happens here.
    """
    print("""
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
""")


def read_user_choice():
    """
    Reads user choice and checks if it's valid;
    Returns '0', '1', '2', '3' or '4'
    """
    select = input('Enter your choice(0..4): ')
    while select not in ['0', '1', '2', '3', '4']:
        select = input('Enter your choice(0..4): ')
    return select


def print_header():
    """
    Prints elegant cars table header
    """
    dummy_var = ''
    print(f'id{dummy_var:<{8}}', '| ', end='')
    print(f'brand{dummy_var:<{11}}', '| ', end='')
    print(f'model{dummy_var:<{6}}', '| ', end='')
    print(f'production_year{dummy_var:<{7}}', '| ', end='')
    print(f'convertible{dummy_var:<{5}}', '|')


# def print_car(car):
#     """
#     Prints one car's data in a way that fits the header.
#     """
    # TODO: Not implemented


def list_cars():
    """
    Gets all cars' data from server and prints it;
    if the database is empty prints diagnostic message instead;
    """
    data_base = check_server()
    if data_base:
        print_header()
        for data in data_base:
            print(f'{data["id"]:<{10}}', '| ', end='')
            print(f'{data["brand"]:<{16}}', '| ', end='')
            print(f'{data["model"]:<{11}}', '| ', end='')
            print(f'{data["production_year"]:<{22}}', '| ', end='')
            print(f'{data["convertible"].__str__():<{16}}', '|')
        print('\n')
    else:
        print('*** Database is empty ***')


# def name_is_valid(name):
#     """
#     checks if name (brand or model) is valid;
#     valid name is non-empty string containing
#     digits, letters and spaces;
#     returns True or False;
#     """
    # TODO: Not implemented. As the name could be everything, but not empty string this function is left empty


def enter_id():
    """
    allows user to enter car's ID and checks if it's valid;
    valid ID consists of digits only;
    returns int or None (if user enters an empty line);
    """
    cars_id = ''
    while True:
        try:
            cars_id = input('Car ID (empty string to exit): ')
            cars_id = int(cars_id)  # Split for exception handling
            break
        except ValueError:
            if cars_id == '':
                return None
            else:
                print("Cars ID must be an integer.")
            continue
    return cars_id


def enter_production_year():
    """
    allows user to enter car's production year and checks if it's valid;
    valid production year is an int from range 1900..2000;
    returns int or None  (if user enters an empty line);
    """
    year = ''
    while True:
        try:
            year = input('Car production year (empty string to exit): ')
            year = int(year)  # Split for exception handling
            if not 1900 < year < 2000:
                print('Valid production year is an int from range 1900..2000!')
                continue
            break
        except ValueError:
            if year == '':
                return None
            else:
                print("Year must be an integer.")
            continue
    return year


def enter_name(what):
    """
    allows user to enter car's name (brand or model) and checks if it's valid;
    uses name_is_valid() to check the entered name;
    returns string or None  (if user enters an empty line);
    argument describes which of two names is entered currently ('brand' or 'model');
    """
    if what == 'brand':
        string = input('Car brand (empty string to exit): ')
    else:
        string = input('Car model (empty string to exit): ')
    if string == '':
        return None
    else:
        return string


def enter_convertible():
    """
    allows user to enter Yes/No answer determining if the car is convertible;
    returns True, False or None  (if user enters an empty line);
    """
    convertible = 0
    while convertible not in ['n', 'y']:
        convertible = input('Is this car convertible? [y/n] (empty string to exit): ')
        if convertible == '':
            return None
    if convertible == 'y':
        convertible = True
    else:
        convertible = False
    return convertible


def delete_car():
    """
    asks user for car's ID and tries to delete it from database;
    """
    cars_id = ''
    while True:
        try:
            cars_id = input('Car ID (empty string to exit): ')
            cars_id = int(cars_id)  # Split for exception handling
            taken = check_server(int(cars_id))
            if not taken:
                print('There is no such ID in database. Try different one!')
                return None
            else:
                headers = {'Connection': 'Close'}
                try:
                    requests.delete(f'http://localhost:3000/cars/{cars_id}')
                    reply = requests.get('http://localhost:3000/cars/', headers=headers)
                except requests.RequestException:
                    print('Communication error')
                else:
                    if reply.status_code == requests.codes.ok:
                        print('Success!')
                    elif reply.status_code == requests.codes.not_found:
                        print("Resource not found")
                    else:
                        print('Server error')
            break
        except ValueError:
            if cars_id == '':
                return None
            else:
                print("Cars ID must be an integer.")
            continue


def input_car_data(with_id):
    """
    Lets user enter car data;
    Argument determines if the car's ID is entered (True) or not (False);
    Returns None if user cancels the operation or a dictionary of the following structure:
    {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }
    """
    if with_id:
        while True:
            cars_id = enter_id()
            if cars_id is None:
                return None
            taken = check_server(int(cars_id))
            if taken:
                print('This ID is already taken. Choose different one!')
                continue
            else:
                break
        brand = enter_name('brand')
        if brand is None:
            return None
        model = enter_name('model')
        if model is None:
            return None
        year = enter_production_year()
        if year is None:
            return None
        convertible = enter_convertible()
        if convertible is None:
            return None
        return {'id': cars_id, 'brand': brand, 'model': model, 'production_year': year, 'convertible': convertible}
    else:
        brand = enter_name('brand')
        if brand is None:
            return None
        model = enter_name('model')
        if model is None:
            return None
        year = enter_production_year()
        if year is None:
            return None
        convertible = enter_convertible()
        if convertible is None:
            return None
        return {'brand': brand, 'model': model, 'production_year': year, 'convertible': convertible}


def add_car():
    """
    invokes input_car_data(True) to gather car's info and adds it to the database
    """
    h_close = {'Connection': 'Close'}
    h_content = {'Content-Type': 'application/json'}
    car = json.dumps(input_car_data(True))
    try:
        requests.post('http://localhost:3000/cars', headers=h_content, data=car)
        reply = requests.get('http://localhost:3000/cars/', headers=h_close)
    except requests.RequestException:
        print('Communication error')
    else:
        if reply.status_code == requests.codes.ok:
            print('Success!')
        elif reply.status_code == requests.codes.not_found:
            print("Resource not found")
        else:
            print('Server error')


def update_car():
    """
    invokes enter_id() to get car's ID if the ID is present in the database;
    invokes input_car_data(False) to gather new car's info and updates the database
    """
    cars_id = enter_id()
    if cars_id is None:
        return None
    taken = check_server(int(cars_id))
    if not taken:
        print('There is no such ID in database. Try different one!')
    else:
        car = {"id": cars_id}
        car.update(input_car_data(False))
        h_close = {'Connection': 'Close'}
        h_content = {'Content-Type': 'application/json'}
        try:
            requests.put(f'http://localhost:3000/cars/{cars_id}', headers=h_content, data=json.dumps(car))
            reply = requests.get('http://localhost:3000/cars/', headers=h_close)
        except requests.RequestException:
            print('Communication error')
        else:
            if reply.status_code == requests.codes.ok:
                print('Success!')
            elif reply.status_code == requests.codes.not_found:
                print("Resource not found")
            else:
                print('Server error')


while True:
    server_status = check_server()
    if not server_status:
        if type(server_status) == list:
            pass
        else:
            print("Server is not responding - quitting!")
            exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()
