class Table:
    def __init__(self, num_of_guest):
        self.num_of_guest = num_of_guest
        self.bill = []

    def order(self, item, price, quantity=1):
        for item_bill in self.bill:
            if item_bill['item'] == item and item_bill['price'] == price:
                item_bill['quantity'] += quantity
                break
        else:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity):
        for item_bill in self.bill:
            if item_bill['item'] == item and item_bill["price"] == price:
                item_bill['quantity'] -= quantity
                if item_bill['quantity'] <= 0:
                    self.bill.remove(item_bill)
                return True
        return False

    def get_subtotal(self):
        total = 0
        for item_bill in self.bill:
            total += (item_bill["price"] * item_bill["quantity"])
        return round(total, 2)

    def get_total(self, service_charge):
        sub_total = round(self.get_subtotal(), 2)
        service_chg = round(sub_total * service_charge, 2)
        total = sub_total + service_chg

        result= {
            'Sub Total': "£" + str(sub_total),
            'Service Charge': "£" + str(service_chg),
            'Total': "£" + str(total)
        }

        return result

    def split_bill(self):
        per_person = round(self.get_subtotal() / self.num_of_guest, 2)
        return per_person
