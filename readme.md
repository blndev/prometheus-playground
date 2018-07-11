Prometheus Playground
---------------------

Here is a set of configuration files and a docker composition which allows you
to play around with the latest prometheus version without setting up everything
by hand again and again.

## Requirements
* docker
* docker-compose

## General

### Node Exporter
We configured three node exporter. Node0, Node1, Node3. Node0 is connected to your locale filesystem. Node1 and Node2 jsut running in docker and having the text exporter enabled for folder /node1/import and /node2/import.
Every file you put there with the extension .prom will be taken and published to prometheus.

### Prometheus
This service is connected to all node exporters and to the Alertmanager.
Alerts are configured in /etc/prometheus/alertrules/* . The rule - files must be enabled in the prometheus.yml on folder higher.

If an alert goes to a hard state. it will be send to the Alertmanager wich than can group and forward them.

To fire an alert just stop node 2 for some minutes.
``docker-compose stop node2``

### Alertmanager
The Alertmanager is configured to be triggered from prometheus.
The configuration can't be splitted to multiple files by default. To work more efficient in teams it make sense to separate the files and concatinate them in a pipeline or use tools like ansible.

The Script ``./alertmanager/testalerts.sh`` is firing a set of alerts which are handled by the different matchers and routes of the alert manager.

#### Notification templates
The Templates are based on Go Text Templating Engine.
These templates are supporting conditions and loops.

You will find more details here: https://godoc.org/text/template

The default templates are compiled into the sources, but they can be found here https://github.com/prometheus/alertmanager/blob/master/template/default.tmpl


### Grafana
Grafana is configured to load the data from prometheus.
In the existing config database the datasource is already configured.
When you delete the database and start the playground again, an empty db will be created. Then you have to configure prometheus as http://prometheus:9090/ as datasource.

### Mailserver
To check notifications we have installed GreenMail as Mail Server (mailserver) and Roundcube as Frontend (Webmailer). The Mailserver is listen on POrt 3025 (SMTP and 3143 for IMAP). The Webmailer can be reached on Port 9080 via the Browser.
The Login name is the username you specified in the notification.
The Password is anything you type in.

In defaullt configuration you will receive notifications on *admin@playground.local* Please use that for login to see the messages.

## Usage
As it is a playground, all of the configurations are stored outside of the
containers.
The measured data and modified files for plugins etc are mostly stored also in
the in the repository folders, but they are not tracked on git. Just remove them
or make a fresh checkout to reset your playground.

### Start
The following command will check and start the environment:
````bash
#check configuration files
docker-compose config
# before the first start you should export the UID to get write access on fs
export PGUSER=$UID
# start the services
docker-copmpose up
````

As alternate (and simpler) way is to use the ``createPlayground.sh`` script,
which does the same.

### Play
Now you can open your browser and go to http://localhost:3000 to reach a
preconfigured grafana instance.

To see how Prometheus is performing, you can use this Dashboard: http://localhost:3000/d/6skUaNvik/prometheus-2-0-stats?refresh=1m&orgId=1


Additional Services:
* http://localhost:9000/ to reach Prometheus
* http://localhost:9100/metrics to reach Node 0 with local data export
* http://localhost:9093/#/status for the alert manager

To reload a Prometheus configuration, please use teh folowing command:
```bash
curl -X POST http://localhost:9090/-/reload
```

To interact with the container use
```bash
$ docker-compose exec -u=$UID grafana bash
```

#### Simulate alertmanagers

You can simply create an alert by shuting down one of the exporters like node 2
with ```docker-compose stop node2```

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
