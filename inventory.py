# This program is designed to perform stock taking.
# It must read in data from a text file, be able to calculate the value,
# update the text file with new information and find information from
# the text file.


class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, the following attributes are initialised:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Code to returns a string representation of a Shoe object.
        '''
        return f'Shoe: {self.product}, Code: {self.code}, Country: {self.country}, Cost: R{self.cost}, Quantity: {self.quantity}.'


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

# ==========Functions outside the class==============


def read_shoes_data():
    '''
    Open the inventory text file, read the data, create Shoe objects and
    append them to the shoe_list.
    Skip the first line in the text file.
    Use try-except for error handing.
    '''
    with open('inventory.txt', 'r') as file:
        try:
            # skip the first line in inventory.txt
            next(file)
            for line in file:
                data = line.strip().split(',')
                if len(data) >= 5:
                    shoe = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
                    shoe_list.append(shoe)
                else:
                    print(f'Invalid {line}')

        except FileNotFoundError:
            print('File not found.')


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    It will also update the inventory text file with the new object.
    '''
    country = input('Enter the country: ')
    code = input('Enter the code: ')
    product = input('Enter the shoe make: ')
    cost = float(input('Enter the cost of the product: R '))
    quantity = int(input('Enter the quantity: '))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

    with open('inventory.txt', 'a') as file:
        file.write(f'{country}, {code}, {product}, {cost}, {quantity}\n')


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    lowest_quantity = float('inf')
    shoe_to_restock = None

    for shoe in shoe_list:
        if shoe.get_quantity() < lowest_quantity:
            lowest_quantity = shoe.get_quantity()
            shoe_to_restock = shoe
    
    
    if shoe_to_restock:
        print(f'The shoe with the lowest quantity is: {shoe_to_restock}')
        restock_qty = int(input('Enter the quantity to restock: '))
        shoe_to_restock.quantity += restock_qty
        print('Quantity restocked successfully.')

        # Update the file with the new quantity.
        with open('inventory.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                data = line.strip().split(',')
                if len(data) >= 5 and data[1] == shoe_to_restock.code:
                    # Update quantity in text file.
                    line = f'{data[0]}, {data[1]}, {data[2]}, {float(data[3])}, {shoe_to_restock.quantity}\n'
                    file.write(line)

    else:
        print('There are no shoes to restock.')


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
     '''
    search_code = input('Enter the shoe code to search: ').upper()
    found_shoe = None

    for shoe in shoe_list:
        if shoe.code == search_code:
            found_shoe = shoe
            break
    
    if found_shoe:
        print('Found shoe details:')
        print(found_shoe)
    else:
        print('Shoe not found.')


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    print('Value per item:')

    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f'Shoe = {shoe.product}, Value: R{round(value,2)} ')


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    highest_quantity = 0
    highest_quantity_shoe = None

    for shoe in shoe_list:
        if shoe.get_quantity() > highest_quantity:
            highest_quantity = shoe.get_quantity()
            highest_quantity_shoe = shoe

    if highest_quantity_shoe:
        print(f'The shoe with the highest quantity is: {highest_quantity_shoe}')
    else:
        print('No shoes available.')


# ==========Main Menu=============
'''
Create a menu that executes each function above.
'''
while True:
    print('\n=== Main menu ===')
    print('1. Read shoes from data file.')
    print('2. Capture shoe data')
    print('3. View all shoes.')
    print('4. Re-stock shoes.')
    print('5. Search for a shoe.')
    print('6. Calculate value per item.')
    print('7. Determine product with highest quantity')
    print('8. Exit')

    choice = int(input('Please select an option: '))

    if choice == 8:
        print('Have a great day!')
        break

    elif choice == 1:
        read_shoes_data()

    elif choice == 2:
        capture_shoes()

    elif choice == 3:
        view_all()

    elif choice == 4:
        re_stock()

    elif choice == 5:
        search_shoe()

    elif choice == 6:
        value_per_item()

    elif choice == 7:
        highest_qty()

    else:
        print('Invalid selection, Please retry.')
