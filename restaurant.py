class Table:

    def __init__(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.bill = []

    def order(self, item: str, price: int, quantity: int = 1) -> list:
        menu_item = {}
        if item not in menu_item:
            menu_item = {"item": item,
                         "price": price,
                         "quantity": quantity
                         }
            self.bill.append(menu_item)
        else:
            menu_item["quantity"] += quantity

        return self.bill

    def remove(self, item: str, price: int, quantity: int) -> bool:
        # iterating through each dict in list
        for menu_item in self.bill:
            # checking if the item and the price match in dict
            if menu_item["item"] == item and menu_item["price"] == price:
                menu_item["quantity"] -= quantity
                if menu_item["quantity"] == 0:
                    self.bill.remove(menu_item)
                    return True
                elif menu_item["quantity"] > 0:
                    return True
                elif menu_item["quantity"] < 0:
                    return False
            else:
                return False

    def get_subtotal(self) -> float:
        total_cost = 0
        for menu_item in self.bill:
            total_cost += menu_item["price"] * menu_item["quantity"]

        return total_cost

    def get_total(self, service_charge: float = 0.1) -> dict:
        subtotal = Table.get_subtotal(self)
        service_charge = subtotal * service_charge
        total = subtotal + service_charge

        total_dict = {"Sub Total": "£{:.2f}".format(subtotal),
                      "Service Charge": "£{:.2f}".format(service_charge),
                      "Total": "£{:.2f}".format(total)
                      }
        return total_dict

    def split_bill(self) -> float:
        total = Table.get_subtotal(self)
        subtotal_cost = round(total / self.number_of_people, 2)

        return subtotal_cost
