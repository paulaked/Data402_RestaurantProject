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
            menu_item["quantity"] += quantity

        return self.bill

    def remove(self, item, price, quantity):
        # iterating through each dict in list
        for menu_item in self.bill:
            # checking if the item and the price match in dict
            if menu_item["item"] == item and menu_item["price"] == price:
                menu_item["quantity"] -= quantity
                if menu_item["quantity"] == 0:
                    self.bill.remove(menu_item)
                    return True
                elif menu_item["quantity"] > 0:
                    return True
                elif menu_item["quantity"] < 0:
                    return False
            else:
                return False

