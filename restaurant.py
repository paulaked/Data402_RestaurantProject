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

    def remove(self, item, price, quantity):
        for item_in_bill in self.bill:
            if item_in_bill['item'] == item and item_in_bill['price'] == price:
                if item_in_bill['quantity'] - quantity > 0:
                    item_in_bill['quantity'] -= quantity
                    return True
                elif item_in_bill['quantity'] - quantity == 0:
                    self.bill.remove(item_in_bill)
                    return True
                else:
                    return False
        return False

    def get_subtotal(self):
        subtotal = round(sum([item_in_bill['quantity']*item_in_bill['price'] for item_in_bill in self.bill]), 2)
        return subtotal


