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

    def remove(self):
        pass

    def get_subtotal(self):
        pass

    def get_total(self):
        pass

    def split_bill(self):
        pass

