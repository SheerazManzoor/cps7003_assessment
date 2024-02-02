from data_layer.employee_data_layer import EmployeeDataLayer

class EmployeeService:
    def __init__(self):
        self.data_layer = EmployeeDataLayer()

    def get_employee_by_id(self, employee_id):
        return self.data_layer.get_employee_by_id(employee_id)

    def add_employee(self, first_name, last_name, position, email, phone_number):
        return self.data_layer.add_employee(first_name, last_name, position, email, phone_number)

    def delete_employee(self, employee_id):
        return self.data_layer.delete_employee(employee_id)

    def update_employee(self, employee_id, new_data):
        return self.data_layer.update_employee(employee_id, new_data)

    def get_all_employees(self):
        return self.data_layer.get_all_employees()

