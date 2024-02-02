from data_layer.customer_data_layer import CustomerDataLayer

class CustomerService:
    def __init__(self):
        self.data_layer = CustomerDataLayer()

    def create_customer(self, first_name, last_name, email, phone_number, address):
        return self.data_layer.create_customer(first_name, last_name, email, phone_number, address)

    def get_all_customers(self):
        return self.data_layer.get_all_customers()

    def get_customer_by_id(self, customer_id):
        return self.data_layer.get_customer_by_id(customer_id)

    def delete_customer(self, customer_id):
        return self.data_layer.delete_customer(customer_id)

    def update_customer(self, customer_id, new_data):
        return self.data_layer.update_customer(customer_id, new_data)

