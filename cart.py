class Product:
    def __init__(self, name, price, deal_price, rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.you_saved = price - deal_price
        
    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("Rating: {}".format(self.rating))
        print("You Saved: {}".format(self.you_saved))
        
    def get_deal_price(self):
        return self.get_deal_price
        
class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, rating, Warrety_in_months):
        super().__init__(name, price, deal_price, rating)
        self.Warrety_in_months = Warrety_in_months
        
    def display_product_details(self):
        super().display_product_details()
        print("Warrenty: {} moths".format(self.Warrety_in_months))

class GroceryItems(Product):
    def __init__(self, name, price, deal_price, rating, expiry_date):
        super().__init__(name, price, deal_price, rating)
        self.expiry_date = expiry_date
        
    def display_product_details(self):
        super().display_product_details()
        print("Expiry Date: {}".format(self.expiry_date))
        
class Orders:
    delivery_charges = {
        "Normal" : 0,
        "Prime Delivery" : 100
    }
    def __init__(self, delivery_method, delivery_address):
        self.cart_in_items = []
        self.delivery_method = delivery_method
        self.delivery_address = delivery_address
        
    def add_items(self,product, quantity):
        items = (product, quantity)
        self.cart_in_items.append(items)
        
    def display_order_product_details(self):
        print("Delivery Meethod: {}".format(self.delivery_method))
        print("Delivery Address: {}".format(self.delivery_address))
        print("Prducts")
        print("----------------------------------------------------------")
        print("")
        for product, quantity in self.cart_in_items:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
            print("")
        print("----------------------------------------------------------")
        total_bill = self.get_total_bill()
        print("Total Bill: {}".format(total_bill))
            

    def get_total_bill(self):
        total_bill = 0
        for product,quantity in self.cart_in_items:
            total_bill += product.get_deal_price() * quantity
            order_delivery_charges=order_delivery_charges[self.delivery_method]
            total_bill=total_bill+order_delivery_charges
        return total_bill    
        
        
        
    
tv = ElectronicItem("Tv", 20000, 15000, 4.5, 24)
milk = GroceryItems("Milk", 50, 42, 4.5, 2022)

my_order = Orders("Normal", "Hyderabad")
my_order.add_items(tv,1)
my_order.add_items(milk, 5)
my_order.display_order_product_details()