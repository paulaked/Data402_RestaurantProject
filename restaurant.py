class Table: # represents each table at restaurant
    def __init__(self, num_people): # when a Table object is created

        self.bill = [] # empty list for bill list is created
        self.num_people = num_people # store number of people at table
        pass

    def order(self, item, price, quantity=1): #default quantity of 1
        for i in range(len(self.bill)): #interate through bill
            if self.bill[i]['item'] == item and self.bill[i]['price'] == price: # check if current item already on bill
                self.bill[i]['quantity'] += quantity #increment if so
                break
        else: # if current item is not on bill
            self.bill.append({'item': item, 'price': price, 'quantity': quantity}) # add new dictionary with new items to bill list

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
        pass

    def get_total(self):
        pass

    def split_bill(self):
        pass

