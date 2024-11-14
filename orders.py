from collections import deque

class OrderQueue:
    def __init__(self):
        # Initialize an empty deque for the kitchen's order queue
        self.queue = deque()
    
    def add_order(self, order_id, items, preparation_time, customer_name):
        """Adds a new order to the queue."""
        order = {
            'order_id': order_id,
            'items': items,
            'preparation_time': preparation_time,
            'customer_name': customer_name
        }
        self.queue.append(order)
        print(f"Order {order_id} added to the queue.")

    def process_order(self):
        """Removes and processes the first order in the queue."""
        if self.queue:
            order = self.queue.popleft()  # Remove the first order (FIFO)
            print(f"Processing Order {order['order_id']} for {order['customer_name']}.")
            return order
        else:
            print("No orders in the queue.")
            return None

    def view_queue(self):
        """Displays all orders in the queue."""
        if not self.queue:
            print("The queue is currently empty.")
        else:
            print("Current orders in the queue:")
            for order in self.queue:
                print(f"Order ID: {order['order_id']}, Customer: {order['customer_name']}, Items: {order['items']}")
