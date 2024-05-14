class Table:
    bill = [{"item": " ",
            "price": " ",
             "quantity": 1}]

    def __init__(self, table_number, no_of_guests):
        self.number = table_number
        self.no_of_guests = no_of_guests

    def order(self):
        item = input("Please enter an item: ")
        price = float(input("Please enter a price: "))
        quantity = int(input("Please enter a quantity: "))
        if not quantity:
            quantity = 1
        else:
            quantity = quantity

        new_item = {"item": item, "price": price, "quantity": quantity}
        bill.append(new_item)

    def get_subtotal(self):
        subtotal = 0
        for i in self.bill:
            sub_price = int(i["price"]) * int(i["quantity"])
            subtotal += sub_price

        return subtotal

    def get_total(self, service_charge=0.10):
        charges = {"Sub Total": "£" + subtotal,
                   "Service Charge": service_charge,
                   "Total": 0
        }

        return charges
