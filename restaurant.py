class Table:
    def __init__(self, num_eaters):
        self.num_eaters = num_eaters
        self.bill = []

    def order(self, item, price, quantity=1):
        for item_in_bill in self.bill:
            if item_in_bill['item'] == item and item_in_bill['price'] == price:
                item_in_bill['quantity'] += quantity
                return
        self.bill.append({'item': item, 'price': price, 'quantity': quantity})

