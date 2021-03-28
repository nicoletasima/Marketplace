"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
from threading import Lock

class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """

    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        # pass
        self.queue_size_per_producer = queue_size_per_producer
        self.products_dict = {} # dictionar id_producator : products
        self.producer_id = 0
        self.carts = {}         # carts dictionary for consumers
        self.cart_id = 0
        self.reserved = {}  # dictionar (produs, producator)

        self.reg_producer_lock = Lock()
        self.new_cart_lock = Lock()
        self.add_to_cart_lock = Lock()
        self.remove_from_cart_lock = Lock()

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        with self.reg_producer_lock:
            producer_id = self.producer_id
            self.products_dict[producer_id] = []
            self.producer_id = self.producer_id + 1
        return producer_id

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        #print(product)
        if len(self.products_dict[producer_id]) >= self.queue_size_per_producer:
            return False
        self.products_dict[producer_id].append(product)
        return True

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        with self.new_cart_lock:
            cart_id = self.cart_id
            self.carts[cart_id] = []
            self.cart_id = self.cart_id + 1
        return cart_id

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        with self.add_to_cart_lock:
            for key in self.products_dict:
                for prod in self.products_dict[key]:
                    if prod == product:
                        self.products_dict[key].remove(product)
                        self.carts[cart_id].append(product)
                        self.reserved[product] = key
                        return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        with self.remove_from_cart_lock:
            reserved_product = self.reserved[product]
            if len(self.products_dict[reserved_product]) >= self.queue_size_per_producer:
                return False
            if product not in self.carts[cart_id]:
                return False
            self.carts[cart_id].remove(product)
            self.products_dict[reserved_product].append(product)
        return True

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        return self.carts[cart_id]
