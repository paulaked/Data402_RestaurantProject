class Table:
    def __init__(self, number_of_people):
        self.number_of_people = number_of_people
        self.bill = []

    def order(self, item: str, price: float, quantity: int = 1) -> None:
        for entry in self.bill:
            if entry["item"] == item and entry["price"] == price:
                entry["quantity"] += quantity
                return
        self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item: str, price: float, quantity: int = 1) -> bool:
        for entry in self.bill:
            if entry["item"] == item and entry["price"] == price:
                entry["quantity"] -= quantity
                if entry["quantity"] < 1:
                    self.bill.remove(entry)
                return True
        return False

    def get_subtotal(self) -> float:
        subtotal = sum(entry["price"] * entry["quantity"] for entry in self.bill)
        return round(subtotal, 2)

    def get_total(self, service_perc: float = 0.10) -> dict:
        subtotal = self.get_subtotal()
        service_charge = subtotal * service_perc
        total = subtotal + service_charge
        text = '{:.2f}'.format(subtotal)
        bill_total = {"Sub Total": f'£{text}', "Service Charge": f'£{service_charge}', "Total": f'£{total}'}
        return bill_total

    def split_bill(self) -> float:
        subtotal = self.get_subtotal()
        split_bill = round((subtotal / self.number_of_people), 2)
        return split_bill

