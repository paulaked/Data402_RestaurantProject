class Table: # represents each table at restaurant
    def __init__(self, num_people): # when a Table object is created

        self._bill = [] # empty list for bill list is created
        self._num_people = num_people # store number of people at table

    @property                   # decorator which defines getter method for accessing bill
    def bill(self):             # defines getter method for bill attribute
        return self._bill

    @bill.setter                # decorator which defines setter method for modifying bill attribute
    def bill(self, new_bill):   # define setter method for bill attribute
        self._bill = new_bill   # sets bill value to value of new bill

    @property                   # decorator which defines getter method for accessing num_people
    def num_people(self):
        return self._num_people

    @num_people.setter                      # decorator defines a setter method for modifying _num_people attribute
    def num_people(self, new_num_people):
        self._num_people = new_num_people

    def order(self, item, price, quantity=1):                                    # default quantity of 1
        for i in range(len(self.bill)):                                          # interate through bill
            if self.bill[i]['item'] == item and self.bill[i]['price'] == price:  # check if current item already on bill
                self.bill[i]['quantity'] += quantity                             # increment if so
                break
        else: # if current item is not on bill
            self.bill.append({'item': item, 'price': price, 'quantity': quantity})  # add new dict w/ new items to list

    def remove(self, item, price, quantity):
        for i in range(len(self.bill)):
            if self.bill[i]['item'] == item and self.bill[i]['price'] == price: # if the current item matches another item in bill
                if self.bill[i]['quantity'] >= quantity: # if quantity to remove greater than actual quantity
                    self.bill[i]['quantity'] -= quantity # decrease by 1
                    if self.bill[i]['quantity'] == 0: # if quantity 0
                        del self.bill[i] # delete item from the bill
                    return True # if removed return True
                else:
                    return False # if item or quantity not in bill
        return False # if item not in bill

    def get_subtotal(self):
        subtotal = sum(item['price'] * item['quantity'] for item in self.bill)
        return subtotal

    def get_total(self, service_charge=0.10):
        subtotal = self.get_subtotal()
        service_charge_amount = subtotal * service_charge
        total = subtotal + service_charge_amount
        return {
            'Sub Total': '£{:.2f}'.format(subtotal), # format as string with £ prefix, float to two decimal places
            'Service Charge': '£{:.2f}'.format(service_charge_amount),
            'Total': '£{:.2f}'.format(total)
        }

    def split_bill(self):
        subtotal = self.get_subtotal()
        split_cost = subtotal / self.num_people # divide cost by number of people
        return round(split_cost, 2) # returns cost to 2 decimal places
