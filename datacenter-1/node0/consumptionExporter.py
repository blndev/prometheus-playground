#!python2
 
from prometheus_client import CollectorRegistry, Gauge, Counter, write_to_textfile

registry = CollectorRegistry()
consumption_service = Gauge('consumption_service', 'current consumption of a service', ['cluster', 'service', 'pod', 'project', 'period'], registry=registry)
consumption_service.labels(cluster='ocp1317', service='mariaDB', pod='maria78', project='default', period='5').set(17)
consumption_service.labels(cluster='ocp1317', service='JBoss', pod='maria78', project='default', period='5').set(5)
consumption_service.labels(cluster='ocp1317', service='NgniX', pod='ng1725', project='frontend', period='5').set(7)


consumption_total = Counter('consumption_total', 'total consumption per month', ['cluster', 'month'], registry=registry)
consumption_total.labels(cluster='ocp1317', month='18-08').inc(5)


write_to_textfile('./import/consumption.prom', registry)


'''
from prometheus_client import Gauge

g = Gauge('my_inprogress_requests', 'Description of gauge')
g.inc()      # Increment by 1
g.dec(10)    # Decrement by given value
g.set(4.2)   # Set to a given value
g.set_to_current_time()
'''

