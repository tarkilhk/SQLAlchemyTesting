import models
from persistence_service import PersistenceService

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sqlalchemy:SQL-4lchemy@192.168.1.101:3307/testSqlAlchemy'
persistenceService = PersistenceService(SQLALCHEMY_DATABASE_URI)

metrics = []
for i in range(1,10):
    metrics.append(models.Metric(application='app2', name='metricName-app2'+str(i), value='metricValue-app2'+str(i)))

persistenceService.saveMetrics(metrics)

metrics1 = persistenceService.getAllMetrics()
metrics2 = persistenceService.getAllMetricsWhereNameContains("2")
print(metrics2)