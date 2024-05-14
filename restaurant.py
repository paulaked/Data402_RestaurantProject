class Table:
    def __init__(self, num_of_people):
        self.num_of_people = num_of_people
        self.bill = []

    def order(self, item: str, price: int, quantity=1):
        for item_entry in self.bill:
            if item_entry["item"] == item and item_entry["price"] == price:
                item_entry["quantity"] += quantity
                return

            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item: str, price: int, quantity=1):
        for item_entry in self.bill:
            if item_entry["item"] == item and item_entry["price"] == price:
                if quantity < item_entry["quantity"]:
                    item_entry["quantity"] -= quantity
                    if item_entry["quantity"] == 0:
                        self.bill.remove({item_entry})
                    return True
                else:
                        return False
        return False

    def get_subtotal(self):
        subtotal = 0
        for item_entry in self.bill:
            subtotal += item_entry["price"] * item_entry["quantity"]
        return subtotal

    def get_total(self, service_charge_percentage=0.10):
        subtotal = self.get_subtotal()
        service_charge = subtotal * service_charge_percentage
        total = subtotal + service_charge

        subtotal_str = "£{:.2f}".format(subtotal)
        service_charge_str = "£{:.2f}".format(service_charge)
        total_str = "£{:.2f}".format(total)

        return {"Sub Total": subtotal_str, "Service Charge": service_charge_str, "Total": total_str}