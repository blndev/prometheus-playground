Prometheus Playground
---------------------

Here is a set of configuration files and a docker composition which allows you
to play around with the latest prometheus version without setting up everything
by hand again and again.

## Requirements
* docker
* docker-compose

## Usage
As it is a playground, all of the configurations are stored outside of the
containers.
The Data restists in the container so that when you throw a container away, data
are lost.

### Start
The following command will check and start the environment:
````bash
#check configuration files
docker-compose config
# start the services
docker-copmpose up
````

### Play
Now you can open your browser and go to http://localhost:3000 to reach a
preconfigured grafana instance.

To see how Prometheus is performing, you can use this Dashboard: http://localhost:3000/d/6skUaNvik/prometheus-2-0-stats?refresh=1m&orgId=1


Additional Services:
* http://localhost:9000/ to reach Prometheus
* http://localhost:9100/metrics to reach Node 1
* http://localhost:9100/metrics to reach Node 2

To reload a Prometheus configuration, please use teh folowing command:
```bash
curl -X POST http://localhost:9090/-/reload
```

To interact with the container use
```bash
$ docker-compose exec -u=$UID grafana bash
```

#### Reference Documentation

#### Prometheus
https://prometheus.io/docs/
https://prometheus.io/docs/prometheus/latest/querying/examples/

##### Grafana
http://docs.grafana.org/

Configuration Values
http://docs.grafana.org/installation/configuration/

### Stop

To set the containers to pause use:
```bash
docker-compose stop
```
Restart can be done by using the "start" command.


### Delete
```bash
# remove a stopped environment
docker-compose rm -f
# stop and remove
docker-compose down
```

## Planned enhancements
Having an SMTP Server for receiving emails / alerts
