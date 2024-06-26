# Restaurant Assignment

Complete the `Table` class in `restaurant.py`. It should be able to instantiate objects to represent tables of diners at a restaurant.  When objects are created they are passed in the number of people dining at that table.  The class should have an instance variable called `bill` that is a list.  The class should also contain the following methods:
- An `order` method that accepts an item and a price.  It should optionally accept a quantity, which should default to 1 if none is provided.  The method should append a menu item to the bill in the form of `{"item": item, "price": price, "quantity": quantity}`.  If the bill already contains an item with the same item name and price, then it should instead update the quantity by adding on the new quantity to the existing quantity.
- A `remove` method, that is similar to the `order` method but instead subtracts the quantity from the item in the bill with the matching item and price.  If this would reduce the quantity to zero, the item should be removed from the bill entirely.  The method should return `True` unless there is not an item with the corresponding item name and price (or the corresponding item has a quantity less than the quantity desired for removal), in which case it should return `False` and make no change to the bill.
- A `get_subtotal` method that returns the total cost for the table based on the prices and quantities in the bill.
- A `get_total` method that accepts a service charge percentage in the form of a decimal.  If no service charge percentage is provided, it should default to 10% (i.e. `0.10`).  This method should return a dictionary with the following keys: `Sub Total`, `Service Charge`, `Total`.  The values should be string representations of the corresponding prices in British pounds and pence.  e.g. `{"Sub Total": "£120.00", "Service Charge": "£12.00", "Total": "£132.00"}`
- A `split_bill` method, which returns the the subtotal cost of the bill divided by the number of diners as a float rounded up to the nearest penny.

## Instructions

- Clone this repo on to your computer
- Create a branch with your own name in lowercase (e.g. 'davidharvey')
- You can run the tests in `test_module.py` at any time to test your code using pytest or unittest
- Add, commit and push your changes to your own branch regularly
- Do not push non-relevant files
- Do not create a pull request
