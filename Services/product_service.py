from data_layer.product_data_layer import ProductDataLayer

class ProductService:
    def __init__(self):
        self.data_layer = ProductDataLayer()
    def get_product_by_id(self, product_id):
        return self.data_layer.get_product_by_id(product_id)

    def add_product(self, product_name, category, price, stock_quantity):
        return self.data_layer.add_product(product_name, category, price, stock_quantity)

    def delete_product(self, product_id):
        return self.data_layer.delete_product(product_id)

    def update_product(self, product_id, new_data):
        return self.data_layer.update_product(product_id, new_data)

    def add_product(self, product_name, category, price, stock_quantity):
        return self.data_layer.add_product(product_name, category, price, stock_quantity)

    def get_all_products(self):
        return self.data_layer.get_all_products()

    def get_top_selling_products(self, limit=5):
        return self.data_layer.get_top_selling_products(limit)
