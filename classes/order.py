class Order:
    def __init__(self,order_id, customer_name, order_date, order_items, order_total):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.order_items = order_items
        self.order_total = order_total
        self.url = "/order/" + str(order_id)