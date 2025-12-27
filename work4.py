class Order:
    def __init__(self, order_id, items, is_vip):
        self.order_id = order_id
        self.items = items
        self.is_vip = is_vip


class OrderQueue:
    def __init__(self):
        self.queue = []

    def add_order(self, order):
        if order.is_vip:
            self.queue.insert(0, order)
        else:
            self.queue.append(order)

        print("Order added:", order.order_id)

    def process_next_order(self):
        if len(self.queue) == 0:
            print("No orders to process")
            return

        order = self.queue.pop(0)
        print("Processing Order:", order.order_id)
        print("Items:", order.items)
        
orders = OrderQueue()

orders.add_order(Order(1, "Burger", False))
orders.add_order(Order(2, "Pizza", False))
orders.add_order(Order(3, "Pasta", True))   
orders.add_order(Order(4, "Sandwich", False))

orders.process_next_order()
orders.process_next_order()