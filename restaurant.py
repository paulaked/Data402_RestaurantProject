class Table:
    def __init__(self, num_of_people):
        self.bill = []
        self.num_of_people = num_of_people

    def order(self, item: str, price: int, quantity=1):
        for item_entry in self.bill:
            if item_entry["item"] == item and item_entry["price"] == price:
                item_entry["quantity"] += quantity
                return

            self.bill.append({"item": item, "price": price, "quantity": quantity})
