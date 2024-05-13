class Table:
    bill = list()

    def __init__(self, tab_num):
        self.tab_num = tab_num
        self.bill = []

    def order(self, item, price, quantity=1):
        sub_order = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        if len(self.bill) != 0:
            self_check = False
            for i in range(len(self.bill)):

                if self.bill[i]["item"] == item and self.bill[i]["price"] == price:
                    self.bill[i]["quantity"] += quantity
                    self_check = True

            if not self_check:
                self.bill.append(sub_order)
        else:

            self.bill.append(sub_order)

    def remove(self, item, price, quantity):
        if len(self.bill) == 0:
            return False
        for i in range(len(self.bill)):
            if self.bill[i]["item"] == item and self.bill[i]["price"] == price:
                if self.bill[i]["quantity"] < quantity:
                    return False
                self.bill[i]["quantity"] -= quantity
                if self.bill[i]["quantity"] == 0:
                    self.bill.pop(i)
                    return True

        return False

    def get_subtotal(self):
        bill_sum = 0
        for i in range(len(self.bill)):
            bill_sum += (self.bill[i]["price"] * self.bill[i]["quantity"])
        return bill_sum

    def get_total(self, serv_charge: float = 0.10):
        sub_total = round(self.get_subtotal(), 2)
        serv_charge_price = sub_total * serv_charge
        final_total = sub_total + serv_charge_price
        final_total = '%.2f' % round(final_total, 2)
        serv_charge_price = '%.2f' % round(serv_charge_price, 2)
        sub_total = '%.2f' % sub_total

        receipt = {
            "Sub Total": f"£{sub_total}",
            "Service Charge": f"£{serv_charge_price}",
            "Total": f"£{final_total}"
        }

        return receipt

    def split_bill(self):
        sub_total = self.get_subtotal()
        split_cost = round((sub_total / self.tab_num), 2)
        return split_cost
