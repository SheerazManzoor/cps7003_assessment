from sqlalchemy.orm import joinedload

from create_database import create_database, Order


class OrderDataLayer:
    DBSession = create_database()

    def get_all_orders(self):
        session = self.DBSession()
        orders = session.query(Order).options(joinedload(Order.product)).all()
        session.close()
        return orders

    def get_order_by_id(self, order_id):
        session = self.DBSession()
        order = session.query(Order).filter_by(order_id=order_id).first()
        session.close()
        return order

    def get_all_orders_for_customer(self, customer_id):
        session = self.DBSession()
        orders = (
            session.query(Order)
            .options(joinedload(Order.product))
            .filter(Order.customer_id == customer_id)
            .all()
        )
        session.close()
        return orders

    def add_order(self, customer_id, product_id, employee_id, quantity):
        session = self.DBSession()
        new_order = Order(
            customer_id=customer_id,
            product_id=product_id,
            employee_id=employee_id,
            quantity=quantity
        )
        session.add(new_order)
        session.commit()
        order_id = new_order.order_id
        session.close()
        return order_id

    def delete_order(self, order_id):
        session = self.DBSession()
        order = session.query(Order).filter_by(order_id=order_id).first()
        if order:
            session.delete(order)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False
