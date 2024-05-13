class Table:
    def __init__(self, num_diners):
        self.num_people = num_diners
        self.bill = []

    #order method
    def order(self, item, price, quantity=1):
        for i, bill_i in enumerate(self.bill):
            if bill_i["item"] ==item and bill_i["price"] == price:
                self.bill[i]["quantity"] += quantity
                break
        else:
            self.bill.append({"item": item, "price" :price, "quantity"})


    #remove method




