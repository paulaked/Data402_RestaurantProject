class Table:
    def __init__(self, no_of_diners: int = 0):
        self.no_of_diners = no_of_diners
        self.bill = []

    def order(self, new_item: str, price: float, quantity: int = 1):
        item_found = False

        for bill_item in self.bill:
            if bill_item['item'] == new_item and bill_item['price'] == price:
                bill_item['quantity'] += quantity
                item_found = True
                break

        if not item_found:
            self.bill.append({'item': new_item, 'price': price, 'quantity': quantity})

    def remove(self, new_item: str, price: float, quantity: int = 1):
        item_found = False

        for bill_item in self.bill:
            if bill_item['item'] == new_item and bill_item['price'] == price:
                bill_item['quantity'] -= quantity
                item_found = True
        self.bill = [bill_item for bill_item in self.bill if bill_item['quantity'] != 0]

        return item_found

    def get_subtotal(self):
        sub_total = 0
        for bill_item in self.bill:
            sub_total += bill_item['price'] * bill_item['quantity']
        return sub_total

    def get_total(self, service_percentage: float = 0.1):
        total = self.get_subtotal() * (1 + service_percentage)
        total_list = {'Sub Total': f'£{self.get_subtotal():.2f}',
                      'Service Charge': f'£{service_percentage * self.get_subtotal()}', 'Total': f'£{total}'}
        print(self.get_subtotal() * 2)
        return total_list

    def split_bill(self):
        subtotal_over_diners = self.get_subtotal() / self.no_of_diners
        rounded_value = round(subtotal_over_diners, 2)
        return rounded_value

    pass
