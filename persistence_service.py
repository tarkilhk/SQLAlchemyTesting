import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

import models
from models import Metric


class PersistenceService():
    def __init__(self, uri):
        self.engine = db.create_engine(uri, echo=True)
        self.connection = self.engine.connect()
        models.Base.metadata.create_all(self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def saveMetric(self, metric: Metric):
        self.session.add(metric)
        self.session.commit()

    def saveMetrics(self, metrics:list):
        self.session.add_all(metrics)
        self.session.commit()

    def getAllMetrics(self):
        return self.session.query(Metric).all()

    def getAllMetricsWhereNameContains(self, param):
        return self.session.query(Metric).filter(Metric.name.like('%'+param+'%')).all()

