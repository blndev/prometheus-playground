from prometheus_client import start_http_server, Summary, Gauge
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

CPU_TEMP = Gauge('cpu_temperature', 'Delivers the current temperature of the cpu', ['cpu', 'core'])
#@CPU_TEMP.set()
# def get_value(t):
#     """A dummy function that takes some time."""
#     CPU_TEMP.set(t)
 

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9100)
    # Generate some requests.
    while True:
        time.sleep(30) #run only every 30 seconds
        process_request(random.random())
        CPU_TEMP.labels(cpu='vCPU-PYthon', core='03').set(random.random()*100)
        CPU_TEMP.labels(cpu='vCPU-PYthon', core='02').set(random.random()*100)
        #get_value(random.random())