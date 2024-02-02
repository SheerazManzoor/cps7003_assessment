from Services.product_service import ProductService
from Services.customer_service import CustomerService
from Services.employee_service import EmployeeService
from Services.order_service import OrderService
from Services.purchase_history_service import PurchaseHistoryService
from Services.communication_log_service import CommunicationLogService


class ConsoleFrontend:
    def __init__(self):
        self.customer_service = CustomerService()
        self.product_service = ProductService()
        self.employee_service = EmployeeService()
        self.order_service = OrderService()
        self.purchase_history_service = PurchaseHistoryService()
        self.communication_log_service = CommunicationLogService()

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.handle_customer_menu()
            elif choice == '2':
                self.handle_product_menu()
            elif choice == '3':
                self.handle_order_menu()
            elif choice == '4':
                self.handle_communication_logs_menu()
            elif choice == '5':
                self.handle_purchase_history_menu()
            elif choice.lower() == 'exit':
                break
            else:
                print("Invalid choice. Please try again.")

    def print_menu(self):
        print("\n--- Menu ---")
        print("1. Customer")
        print("2. Product")
        print("3. Order")
        print("4. Communication Logs")
        print("5. Purchase History")
        print("5. Exit")

    def handle_customer_menu(self):
        while True:
            self.print_customer_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.show_all_customers()
            elif choice == '2':
                self.show_customer_details()
            elif choice == '3':
                self.create_new_customer()
            elif choice == '4':
                self.delete_customer()
            elif choice == '5':
                self.update_customer()
            elif choice == '6':
                self.display_customer_order_history()
            elif choice.lower() == 'back':
                break
            else:
                print("Invalid choice. Please try again.")

    def print_customer_menu(self):
        print("\n--- Customer Menu ---")
        print("1. Show all customers")
        print("2. Show customer details")
        print("3. Create a new customer")
        print("4. Delete a customer")
        print("5. Update customer details")
        print("6. Get Order History")
        print("Type 'back' to return to main menu")

    def handle_product_menu(self):
        while True:
            self.print_product_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.show_all_products()
            elif choice == '2':
                self.show_product_details()
            elif choice == '3':
                self.create_new_product()
            elif choice == '4':
                self.delete_product()
            elif choice == '5':
                self.update_product()
            elif choice == '6':
                self.list_top_selling_products()
            elif choice.lower() == 'back':
                break
            else:
                print("Invalid choice. Please try again.")

    def list_top_selling_products(self):
        top_selling_products = self.product_service.get_top_selling_products(limit=5)

        print("Top Selling Products:")
        for product in top_selling_products:
            print(
                f"Product ID: {product.product_id}, Product Name: {product.product_name}, Total Quantity Sold: {product.total_quantity_sold}")
    def print_product_menu(self):
        print("\n--- Product Menu ---")
        print("1. Show all products")
        print("2. Show product details")
        print("3. Create a new product")
        print("4. Delete a product")
        print("5. Update product details")
        print("6. Get Top Selling Product")
        print("Type 'back' to return to main menu")


    def handle_order_menu(self):
        while True:
            self.print_order_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.show_all_orders()
            elif choice == '2':
                self.show_order_details()
            elif choice == '3':
                self.create_new_order()
            elif choice == '4':
                self.delete_order()
            elif choice.lower() == 'back':
                break
            else:
                print("Invalid choice. Please try again.")

    def handle_purchase_history_menu(self):
        while True:
            self.print_purchase_history_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.show_all_purchase_history()
            elif choice == '2':
                self.show_purchase_history_details()
            elif choice == '3':
                self.create_new_purchase_history()
            elif choice == '4':
                self.delete_purchase_history()
            elif choice.lower() == 'back':
                break
            else:
                print("Invalid choice. Please try again.")

    def print_purchase_history_menu(self):
        print("\n--- Purchase History Menu ---")
        print("1. Show all purchase history")
        print("2. Show purchase history details")
        print("3. Create new purchase history")
        print("4. Delete purchase history")
        print("Type 'back' to return to main menu")

    def print_order_menu(self):
        print("\n--- Order Menu ---")
        print("1. Show all orders")
        print("2. Show order details")
        print("3. Create a new order")
        print("4. Delete an order")
        print("Type 'back' to return to main menu")

    def handle_communication_logs_menu(self):
        while True:
            self.print_communication_logs_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.show_all_communication_logs()
            elif choice == '2':
                self.show_communication_log_details()
            elif choice == '3':
                self.create_new_communication_log()
            elif choice == '4':
                self.update_communication_log()
            elif choice == '5':
                self.delete_communication_log()
            elif choice.lower() == 'back':
                break
            else:
                print("Invalid choice. Please try again.")

    def print_communication_logs_menu(self):
        print("\n--- Communication Logs Menu ---")
        print("1. Show all communication logs")
        print("2. Show communication log details")
        print("3. Create new communication log")
        print("4. Update communication log details")
        print("5. Delete communication log")
        print("Type 'back' to return to main menu")

    def show_all_customers(self):
                customers = self.customer_service.get_all_customers()
                print("\n--- All Customers ---")
                for customer in customers:
                    print("\nCustomer ID:", customer.id)
                    print("Name:", f"{customer.first_name} {customer.last_name}")
                    print("Email:", customer.email)
                    print("Phone Number:", customer.phone_number)
                    print("Address:", customer.address)

    def show_customer_details(self):
        customer_id = input("Enter customer ID: ")
        try:
            customer_id = int(customer_id)
            customer = self.customer_service.get_customer_by_id(customer_id)
            if customer:
                print("\n--- Customer Details ---")
                print(f"ID: {customer.id}")
                print(f"Name: {customer.first_name} {customer.last_name}")
                print(f"Email: {customer.email}")
                print(f"Phone Number: {customer.phone_number}")
                print(f"Address: {customer.address}")
            else:
                print("Customer not found.")
        except ValueError:
            print("Invalid input. Please enter a valid customer ID.")

    def create_new_customer(self):
        print("\n--- Create a New Customer ---")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")
        address = input("Enter address: ")

        customer_id = self.customer_service.create_customer(first_name, last_name, email, phone_number, address)
        print(f"New customer created with ID: {customer_id}")


    def delete_customer(self):
        customer_id = input("Enter customer ID to delete: ")
        try:
            customer_id = int(customer_id)
            success = self.customer_service.delete_customer(customer_id)
            if success:
                print("Customer deleted successfully.")
            else:
                print("Customer not found.")
        except ValueError:
            print("Invalid input. Please enter a valid customer ID.")


    def update_customer(self):
        customer_id = input("Enter customer ID to update: ")
        try:
            customer_id = int(customer_id)
            new_data = {
                'first_name': input("Enter new first name: "),
                'last_name': input("Enter new last name: "),
                'email': input("Enter new email: "),
                'phone_number': input("Enter new phone number: "),
                'address': input("Enter new address: ")
            }
            success = self.customer_service.update_customer(customer_id, new_data)
            if success:
                print("Customer updated successfully.")
            else:
                print("Customer not found.")
        except ValueError:
            print("Invalid input. Please enter a valid customer ID.")

    def display_customer_order_history(self):
        customer_id_to_query = input("Enter Customer ID: ")

        try:
            customer_id_to_query = int(customer_id_to_query)

            customer_order_history = self.order_service.get_customer_order_history(customer_id_to_query)

            if isinstance(customer_order_history, str):
                print(f"Error: {customer_order_history}")
                return

            print(f"Customer ID: {customer_order_history['customer_id']}")
            print(f"Customer Name: {customer_order_history['customer_name']}")
            print("\nOrder History:")
            for order in customer_order_history['order_history']:
                print(f"Order ID: {order['order_id']}")
                print(f"Order Date: {order['order_date']}")
                print(f"Product Name: {order['product_name']}")
                print(f"Quantity: {order['quantity']}")
                print(f"Price per Unit: {order['price_per_unit']}")
                print(f"Total Price: {order['total_price']}")
                print("----------")

            print(f"Total Spent: {customer_order_history['total_spent']}")

        except ValueError:
            print("Error: Please enter a valid integer for Customer ID.")

    def show_all_products(self):
        products = self.product_service.get_all_products()
        print("\n--- All Products ---")
        for product in products:
            print("\nProduct ID:", product.product_id)
            print("Name:", product.product_name)
            print("Category:", product.category)
            print("Price:", product.price)
            print("Stock Quantity:", product.stock_quantity)

    def show_product_details(self):
        product_id = input("Enter product ID: ")
        try:
            product_id = int(product_id)
            product = self.product_service.get_product_by_id(product_id)
            if product:
                print("\n--- Product Details ---")
                print(f"ID: {product.product_id}")
                print(f"Name: {product.product_name}")
                print(f"Category: {product.category}")
                print(f"Price: {product.price}")
                print(f"Stock Quantity: {product.stock_quantity}")
            else:
                print("Product not found.")
        except ValueError:
            print("Invalid input. Please enter a valid product ID.")


    def create_new_product(self):
        print("\n--- Create a New Product ---")
        product_name = input("Enter product name: ")
        category = input("Enter product category: ")
        price = input("Enter product price: ")
        stock_quantity = input("Enter stock quantity: ")

        product_id = self.product_service.add_product(product_name, category, price, stock_quantity)
        print(f"New product created with ID: {product_id}")


    def delete_product(self):
        product_id = input("Enter product ID to delete: ")
        try:
            product_id = int(product_id)
            success = self.product_service.delete_product(product_id)
            if success:
                print("Product deleted successfully.")
            else:
                print("Product not found.")
        except ValueError:
            print("Invalid input. Please enter a valid product ID.")


    def update_product(self):
        product_id = input("Enter product ID to update: ")
        try:
            product_id = int(product_id)
            new_data = {
                'product_name': input("Enter new product name: "),
                'category': input("Enter new category: "),
                'price': input("Enter new price: "),
                'stock_quantity': input("Enter new stock quantity: ")
            }
            success = self.product_service.update_product(product_id, new_data)
            if success:
                print("Product updated successfully.")
            else:
                print("Product not found.")
        except ValueError:
            print("Invalid input. Please enter a valid product ID.")

    def show_all_employees(self):
        employees = self.employee_service.get_all_employees()
        print("\n--- All Employees ---")
        for employee in employees:
            print("\nEmployee ID:", employee.employee_id)
            print("Name:", f"{employee.first_name} {employee.last_name}")
            print("Position:", employee.position)
            print("Email:", employee.email)
            print("Phone Number:", employee.phone_number)

    def show_employee_details(self):
        employee_id = input("Enter employee ID: ")
        try:
            employee_id = int(employee_id)
            employee = self.employee_service.get_employee_by_id(employee_id)
            if employee:
                print("\n--- Employee Details ---")
                print(f"ID: {employee.employee_id}")
                print(f"Name: {employee.first_name} {employee.last_name}")
                print(f"Position: {employee.position}")
                print(f"Email: {employee.email}")
                print(f"Phone Number: {employee.phone_number}")
            else:
                print("Employee not found.")
        except ValueError:
            print("Invalid input. Please enter a valid employee ID.")

    def create_new_employee(self):
        print("\n--- Create a New Employee ---")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        position = input("Enter position: ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")

        employee_id = self.employee_service.add_employee(first_name, last_name, position, email, phone_number)
        print(f"New employee created with ID: {employee_id}")

    def delete_employee(self):
        employee_id = input("Enter employee ID to delete: ")
        try:
            employee_id = int(employee_id)
            success = self.employee_service.delete_employee(employee_id)
            if success:
                print("Employee deleted successfully.")
            else:
                print("Employee not found.")
        except ValueError:
            print("Invalid input. Please enter a valid employee ID.")

    def update_employee(self):
        employee_id = input("Enter employee ID to update: ")
        try:
            employee_id = int(employee_id)
            new_data = {
                'first_name': input("Enter new first name: "),
                'last_name': input("Enter new last name: "),
                'position': input("Enter new position: "),
                'email': input("Enter new email: "),
                'phone_number': input("Enter new phone number: ")
            }
            success = self.employee_service.update_employee(employee_id, new_data)
            if success:
                print("Employee updated successfully.")
            else:
                print("Employee not found.")
        except ValueError:
            print("Invalid input. Please enter a valid employee ID.")

    def show_all_orders(self):
        orders = self.order_service.get_all_orders()
        print("\n--- All Orders ---")
        for order in orders:
            print("\nOrder ID:", order.order_id)
            print("Customer ID:", order.customer_id)
            print("Product ID:", order.product_id)
            print("Employee ID:", order.employee_id)
            print("Order Date:", order.order_date)
            print("Quantity:", order.quantity)

    def show_order_details(self):
        order_id = input("Enter order ID: ")
        try:
            order_id = int(order_id)
            order = self.order_service.get_order_by_id(order_id)
            if order:
                print("\n--- Order Details ---")
                print(f"ID: {order.order_id}")
                print(f"Customer ID: {order.customer_id}")
                print(f"Product ID: {order.product_id}")
                print(f"Employee ID: {order.employee_id}")
                print(f"Order Date: {order.order_date}")
                print(f"Quantity: {order.quantity}")
            else:
                print("Order not found.")
        except ValueError:
            print("Invalid input. Please enter a valid order ID.")

    def create_new_order(self):
        print("\n--- Create a New Order ---")
        customer_id = input("Enter customer ID: ")
        product_id = input("Enter product ID: ")
        employee_id = input("Enter employee ID: ")
        quantity = input("Enter quantity: ")

        order_id = self.order_service.add_order(customer_id, product_id, employee_id, quantity)
        print(f"New order created with ID: {order_id}")

    def delete_order(self):
        order_id = input("Enter order ID to delete: ")
        try:
            order_id = int(order_id)
            success = self.order_service.delete_order(order_id)
            if success:
                print("Order deleted successfully.")
            else:
                print("Order not found.")
        except ValueError:
            print("Invalid input. Please enter a valid order ID.")

    def show_all_purchase_history(self):
        purchase_history_list = self.purchase_history_service.get_all_purchase_history()
        print("\n--- All Purchase History ---")
        for purchase in purchase_history_list:
            print(f"{purchase.purchase_id}. Customer ID: {purchase.customer_id}, Product ID: {purchase.product_id}")

    def show_purchase_history_details(self):
        purchase_id = input("Enter purchase ID: ")
        try:
            purchase_id = int(purchase_id)
            purchase = self.purchase_history_service.get_purchase_history_by_id(purchase_id)
            if purchase:
                print("\n--- Purchase History Details ---")
                print(f"Purchase ID: {purchase.purchase_id}")
                print(f"Customer ID: {purchase.customer_id}")
                print(f"Product ID: {purchase.product_id}")
                print(f"Purchase Date: {purchase.purchase_date}")
                print(f"Price: {purchase.price}")
                print(f"Quantity: {purchase.quantity}")
            else:
                print("Purchase history not found.")
        except ValueError:
            print("Invalid input. Please enter a valid purchase ID.")

    def create_new_purchase_history(self):
        print("\n--- Create New Purchase History ---")
        customer_id = input("Enter customer ID: ")
        product_id = input("Enter product ID: ")
        purchase_date = input("Enter purchase date: ")
        price = input("Enter price: ")
        quantity = input("Enter quantity: ")

        purchase_id = self.purchase_history_service.add_purchase_history(customer_id, product_id, purchase_date, price, quantity)
        print(f"New purchase history created with ID: {purchase_id}")

    def delete_purchase_history(self):
        purchase_id = input("Enter purchase ID to delete: ")
        try:
            purchase_id = int(purchase_id)
            success = self.purchase_history_service.delete_purchase_history(purchase_id)
            if success:
                print("Purchase history deleted successfully.")
            else:
                print("Purchase history not found.")
        except ValueError:
            print("Invalid input. Please enter a valid purchase ID.")

    def show_all_communication_logs(self):
        logs = self.communication_log_service.get_all_communication_logs()
        print("\n--- All Communication Logs ---")
        for log in logs:
            print("\nLog ID:", log.log_id)
            print("Customer ID:", log.customer_id)
            print("Timestamp:", log.timestamp)
            print("Communication Type:", log.communication_type)
            print("Communication Content:", log.communication_content)

    def show_communication_log_details(self):
        log_id = input("Enter communication log ID: ")
        try:
            log_id = int(log_id)
            log = self.communication_log_service.get_communication_log_by_id(log_id)
            if log:
                print("\n--- Communication Log Details ---")
                print(f"ID: {log.log_id}")
                print(f"Customer ID: {log.customer_id}")
                print(f"Timestamp: {log.timestamp}")
                print(f"Communication Type: {log.communication_type}")
                print(f"Communication Content: {log.communication_content}")
            else:
                print("Communication log not found.")
        except ValueError:
            print("Invalid input. Please enter a valid communication log ID.")

    def create_new_communication_log(self):
        print("\n--- Create a New Communication Log ---")
        customer_id = input("Enter customer ID: ")
        timestamp = input("Enter timestamp: ")
        communication_type = input("Enter communication type: ")
        communication_content = input("Enter communication content: ")

        log_id = self.communication_log_service.add_communication_log(
            customer_id, timestamp, communication_type, communication_content
        )
        print(f"New communication log created with ID: {log_id}")

    def update_communication_log(self):
        log_id = input("Enter communication log ID to update: ")
        try:
            log_id = int(log_id)
            new_data = {
                'customer_id': input("Enter new customer ID: "),
                'timestamp': input("Enter new timestamp: "),
                'communication_type': input("Enter new communication type: "),
                'communication_content': input("Enter new communication content: ")
            }
            success = self.communication_log_service.update_communication_log(log_id, new_data)
            if success:
                print("Communication log updated successfully.")
            else:
                print("Communication log not found.")
        except ValueError:
            print("Invalid input. Please enter a valid communication log ID.")

    def delete_communication_log(self):
        log_id = input("Enter communication log ID to delete: ")
        try:
            log_id = int(log_id)
            success = self.communication_log_service.delete_communication_log(log_id)
            if success:
                print("Communication log deleted successfully.")
            else:
                print("Communication log not found.")
        except ValueError:
            print("Invalid input. Please enter a valid communication log ID.")


if __name__ == '__main__':
    console_frontend = ConsoleFrontend()
    console_frontend.run()
