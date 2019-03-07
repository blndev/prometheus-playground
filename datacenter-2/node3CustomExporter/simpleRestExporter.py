from prometheus_client import start_http_server, Summary, Gauge
import random
import time

# Create a metric to track time spent for a function and count of requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request', ['method'])

request1 = REQUEST_TIME.labels(method='request1')
# Decorate function with metric.
@request1.time()
def process_request(t):
    """A dummy function that takes some time."""
    # we could also execute an external task liek fetching a url
    time.sleep(t)

# Additional metrics
CPU_TEMP = Gauge('cpu_temperature', 'Delivers the current temperature of the cpu', ['cpu', 'core'])
CPU_FANSPEED = Gauge('cpu_fanspeed', 'Delivers the rotation per minute of the cpu fan', ['cpu', 'core'])

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9100)
    # Generate some requests.
    while True:
        time.sleep(30) # update our data every 30 seconds
        process_request(random.random())
        CPU_TEMP.labels(cpu='vCPU-PYthon', core='01').set(random.random()*100)
        CPU_TEMP.labels(cpu='vCPU-PYthon', core='02').set(random.random()*100)
        CPU_FANSPEED.labels(cpu='vCPU-PYthon', core='01').set(random.random()*3000)
        CPU_FANSPEED.labels(cpu='vCPU-PYthon', core='02').set(random.random()*3000)
