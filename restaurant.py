class Table:
    def __init__(self, num_of_people):
        self.num_of_people = num_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        for i, bill_item in enumerate(self.bill):
            if bill_item["item"] == item and bill_item["price"] == price:
                self.bill[i]["quantity"] += quantity
                break
        else:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self):
        for i, bill_item in enumerate(self.bill):
            if bill_item["item"] == item and bill_item['price'] == price:
                if bill_item["quantity"] >= quantity:
                    self.bill[i]['quantity'] -= quantity
                    if self.bill[i]['quantity'] == 0:
                        del self.bill[i]
                    return True
                else:
                    return False
        return False



