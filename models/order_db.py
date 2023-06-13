from classes.order import Order


order_contents1 = [["Tears of the Kingdom",50],["Minecraft",50]]
order1 = Order(1,"James","11/12/13",order_contents1,100)
order_contents2 = [["Apple VR Headset",3000]]
order2 = Order(2,"Jessie","04/05/22",[],3000)
order_contents3 = [["HTC Vive",400],["Half Life Alyx",100]]
order3 = Order(220,"John","23/10/16",[],500)

orders = [order1,order2,order3]

def return_order_by_id(orders,order_id):
    for order in orders:
        if order.order_id == int(order_id):
            return order