from data_layer.purchase_history_data_layer import PurchaseDataLayer


class PurchaseHistoryService:
    def __init__(self):
        self.data_layer = PurchaseDataLayer()

    def get_purchase_history_by_id(self, purchase_id):
        return self.data_layer.get_purchase_history_by_id(purchase_id)

    def get_all_purchase_history(self):
        return self.data_layer.get_all_purchase_history()

    def add_purchase_history(self, customer_id, product_id, purchase_date, price, quantity):
        return self.data_layer.add_purchase_history(customer_id, product_id, purchase_date, price, quantity)

    def delete_purchase_history(self, purchase_id):
        return self.data_layer.delete_purchase_history(purchase_id)

    def update_purchase_history(self, purchase_id, new_data):
        return self.data_layer.update_purchase_history(purchase_id, new_data)
