from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Metric(Base):
    __tablename__ = 'metrics'

    id = Column(Integer, primary_key=True)
    application = Column(String(50))
    name = Column(String(50))
    value = Column(String(50))

    def __repr__(self):
       return "<Metric(application='%s'name='%s', value='%s')>" % (
                            self.application, self.name, self.value)