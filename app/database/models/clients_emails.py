from .base import Base

from sqlalchemy import ForeignKey, Column, String, Boolean, Integer


class ClientsEmails(Base):
    __tablename__ = 'clients_emails'
    
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(255))   
    is_primary = Column('isPrimary', Boolean)

    client_pims_id = Column(Integer, ForeignKey('client.pimsId'))