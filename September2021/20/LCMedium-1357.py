"""
https://leetcode.com/problems/apply-discount-every-n-orders

Explanation of zip function : https://www.youtube.com/watch?v=qj-V2Ep4coY
"""

class Cashier:

    def __init__(self, n: int, discount: int, products, prices):
        # discount for every n-th customer.
        self.n = n
        self.nth_customer = 1
        self.discount = discount
        self.pid_price = {prod: price for prod, price in zip(products, prices)} #zip function is inevitable for such
        # problems where you have columns from table that you want to combine together


    def getBill(self, product, amount) -> float:
        """
        product: ID
        amount = # of products
        subtotal = product[j]*amount[j]
        """
        def get_subtotal(product, amount):
            total = 0
            for pid, ea in zip(product, amount):
                total += (self.pid_price[pid]*ea)

            return total

        def get_discount(total):
            if self.nth_customer%self.n == 0:
                # Discount total price.
                self.nth_customer = 1
                return total*((100. - self.discount)/100.)
            else:
                # Don't discount.
                self.nth_customer += 1
                return total

        return get_discount(get_subtotal(product, amount))

cashier = Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
print(cashier.getBill([1,2],[1,2]))                     # return 500.0. 1st customer, no discount.
                                                        # bill = 1 * 100 + 2 * 200 = 500.
print(cashier.getBill([3,7],[10,10]))                   # return 4000.0. 2nd customer, no discount.
                                                        # bill = 10 * 300 + 10 * 100 = 4000.
print(cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1])) # return 800.0. 3rd customer, 50% discount.
                                                        # Original bill = 1600
                                                        # Actual bill = 1600 * ((100 - 50) / 100) = 800.
print(cashier.getBill([4],[10]))                        # return 4000.0. 4th customer, no discount.
print(cashier.getBill([7,3],[10,10]))                   # return 4000.0. 5th customer, no discount.
print(cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]))    # return 7350.0. 6th customer, 50% discount.
                                                        # Original bill = 14700, but with
                                                        # Actual bill = 14700 * ((100 - 50) / 100) = 7350.
print(cashier.getBill([2,3,5],[5,3,2]))                 # return 2500.0.  6th customer, no discount.