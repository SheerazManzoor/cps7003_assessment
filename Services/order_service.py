from data_layer.order_data_layer import OrderDataLayer
from Services.customer_service import CustomerService
class OrderService:
    def __init__(self):
        self.data_layer = OrderDataLayer()
        self.customer_service = CustomerService()

    def get_order_by_id(self, order_id):
        return self.data_layer.get_order_by_id(order_id)

    def get_all_orders(self):
        return self.data_layer.get_all_orders()

    def add_order(self, customer_id, product_id, employee_id, quantity):
        return self.data_layer.add_order(customer_id, product_id, employee_id, quantity)

    def delete_order(self, order_id):
        return self.data_layer.delete_order(order_id)

    def get_customer_order_history(self, customer_id):
        customer = self.customer_service.get_customer_by_id(customer_id)

        if not customer:
            return f"Customer with ID {customer_id} not found."

        orders = self.data_layer.get_all_orders_for_customer(customer_id)

        total_spent = sum(order.quantity * order.product.price for order in orders)

        order_history = [
            {
                'order_id': order.order_id,
                'order_date': order.order_date,
                'product_name': order.product.product_name,
                'quantity': order.quantity,
                'price_per_unit': order.product.price,
                'total_price': order.quantity * order.product.price,
            }
            for order in orders
        ]

        result = {
            'customer_id': customer.id,
            'customer_name': f'{customer.first_name} {customer.last_name}',
            'order_history': order_history,
            'total_spent': total_spent,
        }

        return result


