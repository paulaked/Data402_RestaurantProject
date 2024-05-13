class Table:

    def __init__(self, number_of_people):
        self.number_of_people = number_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        menu_item = {}
        if item not in menu_item:
            menu_item = {"item": item,
                         "price": price,
                         "quantity": quantity
                         }
            self.bill.append(menu_item)
        else:
            quantity += menu_item["quantity"]

