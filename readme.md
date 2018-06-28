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
The following command will start the environment:
````bash
docker-copmpose up metrics-stack.yml
````

### Play
Now you can open your browser and go to http://localhost:3000 to reach a
preconfigured grafana instance.

Additional Services:
* http://localhost:9000/ to reach Prometheus
* http://localhost:9100/metrics to reach Node 1
* http://localhost:9100/metrics to reach Node 2

### Stop


### Delete

## Planned enhancements
Having an SMTP Server for receiving emails / alerts 
