from create_database import create_database, Customer


class CustomerDataLayer:
    DBSession = create_database()

    def create_customer(self, first_name, last_name, email, phone_number, address):
        session = self.DBSession()
        new_customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address
        )
        session.add(new_customer)
        session.commit()
        session.close()

    def get_all_customers(self):
        session = self.DBSession()
        customers = session.query(Customer).all()
        session.close()
        return customers

    def get_customer_by_id(self, customer_id):
        session = self.DBSession()
        customer = session.query(Customer).filter_by(id=customer_id).first()
        session.close()
        return customer

    def delete_customer(self, customer_id):
        session = self.DBSession()
        customer = session.query(Customer).filter_by(id=customer_id).first()
        if customer:
            session.delete(customer)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False

    def update_customer(self, customer_id, new_data):
        session = self.DBSession()
        customer = session.query(Customer).filter_by(id=customer_id).first()
        if customer:
            for key, value in new_data.items():
                setattr(customer, key, value)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False
