from data_layer.communication_log_data_layer import CommunicationLogDataLayer

class CommunicationLogService:
    def __init__(self):
        self.data_layer = CommunicationLogDataLayer()

    def add_communication_log(self, customer_id, timestamp, communication_type, communication_content):
        return self.data_layer.add_communication_log(customer_id, timestamp, communication_type, communication_content)

    def get_communication_log_by_id(self, log_id):
        return self.data_layer.get_communication_log_by_id(log_id)

    def get_all_communication_logs(self):
        return self.data_layer.get_all_communication_logs()

    def update_communication_log(self, log_id, new_data):
        return self.data_layer.update_communication_log(log_id, new_data)

    def delete_communication_log(self, log_id):
        return self.data_layer.delete_communication_log(log_id)
