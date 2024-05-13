class Table:

    def __init__(self, people: int) -> None:
        self.people = people
        self.bill = []

    def order(self, item: str, price: float, quantity: int = 1) -> None:
        for items in self.bill:
            if items['item'] in item:
                items['quantity'] += quantity
                break
        else:
            self.bill.append({'item': item, 'price': price, 'quantity': quantity})

    def remove(self, item: str, price: float, quantity: int = 1) -> bool:
        for items in self.bill:
            if items["item"] in item:
                if items["quantity"] - quantity > 0:
                    items["quantity"] -= quantity
                    return True
                elif items["quantity"] - quantity == 0:
                    self.bill.remove(items)
                    return True
                elif items["quantity"] - quantity < 0:
                    return False

    def get_subtotal(self) -> float:
        sub_total = 0
        for items in self.bill:
            sub_total += items["price"] * items["quantity"]
        return sub_total

    def get_total(self,service_charge: float = 0.10) -> dict:
        total = self.get_subtotal() * (service_charge + 1)
        return {"Sub Total": self.get_subtotal(), "Service Charge": service_charge, "Total": f"{total:.2f}"}

    def split_bill(self):
        split_total = self.get_subtotal() / self.people
        return f"£{split_total:.2f} per person"
