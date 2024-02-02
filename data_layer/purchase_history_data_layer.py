from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

from create_database import create_database, PurchaseHistory


class PurchaseDataLayer:
    DBSession = create_database()

    def get_purchase_history_by_id(self, purchase_id):
        session = self.DBSession()
        purchase_history = session.query(PurchaseHistory).filter_by(purchase_id=purchase_id).first()
        session.close()
        return purchase_history

    def get_all_purchase_history(self):
        session = self.DBSession()
        purchase_history_list = session.query(PurchaseHistory).all()
        session.close()
        return purchase_history_list

    def add_purchase_history(self, customer_id, product_id, purchase_date, price, quantity):
        session = self.DBSession()
        new_purchase = PurchaseHistory(
            customer_id=customer_id,
            product_id=product_id,
            purchase_date=purchase_date,
            price=price,
            quantity=quantity
        )
        session.add(new_purchase)
        session.commit()
        purchase_id = new_purchase.purchase_id
        session.close()
        return purchase_id

    def delete_purchase_history(self, purchase_id):
        session = self.DBSession()
        purchase_history = session.query(PurchaseHistory).filter_by(purchase_id=purchase_id).first()
        if purchase_history:
            session.delete(purchase_history)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False
