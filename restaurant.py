class Table:

    def __init(self, table_number, number_of_people):
        self.table_number = table_number
        self.number_of_people = number_of_people
        self.bill = []

    def order(self, item, price, quantity):
        bill = []
        menu_item = {"item": item, "price": price, "quantity": quantity}
        bill.append(menu_item)
        print("{item} aadded to the bill")

    def remove(self, item, price, quantity):
        for menu_item in bill:
            if menu_item == item and menu_item == price:
                bill.remove(menu_item)
                print("The {item} has been removed from the bill")


