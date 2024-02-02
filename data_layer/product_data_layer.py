from sqlalchemy import func

from create_database import create_database, Product, PurchaseHistory


class ProductDataLayer:
    DBSession = create_database()


    def get_product_by_id(self, product_id):
        session = self.DBSession()
        product = session.query(Product).filter_by(product_id=product_id).first()
        session.close()
        return product

    def add_product(self, product_name, category, price, stock_quantity):
        session = self.DBSession()
        new_product = Product(
            product_name=product_name,
            category=category,
            price=price,
            stock_quantity=stock_quantity
        )
        session.add(new_product)
        session.commit()
        product_id = new_product.product_id
        session.close()
        return product_id

    def delete_product(self, product_id):
        session = self.DBSession()
        product = session.query(Product).filter_by(product_id=product_id).first()
        if product:
            session.delete(product)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False

    def update_product(self, product_id, new_data):
        session = self.DBSession()
        product = session.query(Product).filter_by(product_id=product_id).first()
        if product:
            for key, value in new_data.items():
                setattr(product, key, value)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False

    def get_all_products(self):
        session = self.DBSession()
        products = session.query(Product).all()
        session.close()
        return products

    def add_product(self, product_name, category, price, stock_quantity):
        session = self.DBSession()
        new_product = Product(
            product_name=product_name,
            category=category,
            price=price,
            stock_quantity=stock_quantity
        )
        session.add(new_product)
        session.commit()
        product_id = new_product.product_id
        session.close()
        return product_id

    def get_top_selling_products(self, limit=5):
        session = self.DBSession()
        top_selling_products = (
            session.query(
                Product.product_id,
                Product.product_name,
                func.sum(PurchaseHistory.quantity).label('total_quantity_sold')
            )
            .join(PurchaseHistory, PurchaseHistory.product_id == Product.product_id)
            .group_by(Product.product_id, Product.product_name)
            .order_by(func.sum(PurchaseHistory.quantity).desc())
            .limit(limit)
            .all()
        )
        session.close()
        return top_selling_products
