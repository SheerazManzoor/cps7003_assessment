from create_database import create_database, Employee


class EmployeeDataLayer:
    DBSession = create_database()

    def get_employee_by_id(self, employee_id):
        session = self.DBSession()
        employee = session.query(Employee).filter_by(employee_id=employee_id).first()
        session.close()
        return employee

    def add_employee(self, first_name, last_name, position, email, phone_number):
        session = self.DBSession()
        new_employee = Employee(
            first_name=first_name,
            last_name=last_name,
            position=position,
            email=email,
            phone_number=phone_number
        )
        session.add(new_employee)
        session.commit()
        employee_id = new_employee.employee_id
        session.close()
        return employee_id

    def delete_employee(self, employee_id):
        session = self.DBSession()
        employee = session.query(Employee).filter_by(employee_id=employee_id).first()
        if employee:
            session.delete(employee)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False

    def update_employee(self, employee_id, new_data):
        session = self.DBSession()
        employee = session.query(Employee).filter_by(employee_id=employee_id).first()
        if employee:
            for key, value in new_data.items():
                setattr(employee, key, value)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False

    def get_all_employees(self):
        session = self.DBSession()
        employees = session.query(Employee).all()
        session.close()
        return employees