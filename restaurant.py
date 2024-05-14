class Table:

    def __init(self, table_number, number_of_people: int):
        self.table_number = table_number
        self.number_of_people = number_of_people
        self.bill = []

    def order(self, item: str, price: int, quantity: int):
        bill = []
        menu_item = {"item": item, "price": price, "quantity": quantity}
        bill.append(menu_item)
        print("{item} added to the bill")

    def remove(self, item: str, price: int, quantity: int):
        for menu_item in self.bill:
            if menu_item == item and menu_item == price and menu_item == quantity:
                self.bill.remove(menu_item)
                print("The {item} has been removed from the bill")

    def get_subtotal(self):
        subtotal = 0
        for menu_item in self.bill:
            subtotal += menu_item.price * menu_item.quantity
            return subtotal

    def get_total(self, service_charge=0, discount=0) -> float:
        subtotal = self.get_subtotal()
        service_fee = subtotal * service_charge
        discount_amount = subtotal * discount
        total = subtotal + service_fee - discount_amount
        return total

    def split_bill(self, total_amount: float, num_people: int) -> float:
        if num_people <= 0:
            raise ValueError("There are 0 people")
        return total_amount / num_people
