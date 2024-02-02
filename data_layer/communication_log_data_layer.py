from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from create_database import create_database, CommunicationLog


class CommunicationLogDataLayer:
    DBSession = create_database()

    def add_communication_log(self, customer_id, timestamp, communication_type, communication_content):
        session = self.DBSession()
        new_log = CommunicationLog(
            customer_id=customer_id,
            timestamp=timestamp,
            communication_type=communication_type,
            communication_content=communication_content
        )
        session.add(new_log)
        session.commit()
        log_id = new_log.log_id
        session.close()
        return log_id

    def get_communication_log_by_id(self, log_id):
        session = self.DBSession()
        log = session.query(CommunicationLog).filter_by(log_id=log_id).first()
        session.close()
        return log

    def get_all_communication_logs(self):
        session = self.DBSession()
        logs = session.query(CommunicationLog).all()
        session.close()
        return logs

    def update_communication_log(self, log_id, new_data):
        session = self.DBSession()
        log = session.query(CommunicationLog).filter_by(log_id=log_id).first()
        if log:
            for key, value in new_data.items():
                setattr(log, key, value)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False

    def delete_communication_log(self, log_id):
        session = self.DBSession()
        log = session.query(CommunicationLog).filter_by(log_id=log_id).first()
        if log:
            session.delete(log)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False
