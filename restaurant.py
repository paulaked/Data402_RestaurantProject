class Table:
    def __init__(self, num_of_people):
        # Table object with number of people eating and empty bill list
        self.num_of_people = num_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        # Add an item to the bill. If the item already exists, update the quantity.
        index = 0
        for bill_item in self.bill:
            if bill_item["item"] == item and bill_item["price"] == price:
                self.bill[index]["quantity"] += quantity
                break
            index += 1
        else:      # If the item doesn't exist, add it to the bill
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity=1):
        # Remove an item from the bill. If quantity = zero, remove the item from the bill.
        index = 0
        for bill_item in self.bill:
            if bill_item["item"] == item and bill_item["price"] == price:
                if bill_item["quantity"] >= quantity:
                    self.bill[index]["quantity"] -= quantity
                    if self.bill[index]["quantity"] == 0:
                        self.bill.remove(bill_item)
                    return True
                else:
                    return False
            index += 1
        return False

    def get_subtotal(self):
        # Calculate the subtotal of the bill.
        subtotal = 0
        for item in self.bill:
            subtotal += item["price"] * item["quantity"]
        return subtotal
