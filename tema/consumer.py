"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
import time
from threading import Thread

class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        self.name = kwargs['name']

    def run(self):
        for cart in self.carts:
            cart_id = self.marketplace.new_cart()
            for products in cart:
                if products['type'] == 'add':
                    for _ in range(int(products['quantity'])):
                        prod = self.marketplace.add_to_cart(cart_id, products['product'])
                        while not prod:
                            time.sleep(self.retry_wait_time)
                            prod = self.marketplace.add_to_cart(cart_id, products['product'])
                if products['type'] == 'remove':
                    for _ in range(int(products['quantity'])):
                        prod = self.marketplace.remove_from_cart(cart_id, products['product'])
                        while not prod:
                            time.sleep(self.retry_wait_time)
                            prod = self.marketplace.remove_from_cart(cart_id, products['product'])
            cart_products = self.marketplace.place_order(cart_id)
            for product in cart_products:
                print(self.name + " bought", product)
