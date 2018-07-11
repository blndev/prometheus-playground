# setting PGUSER to current user is, which allows to write to the local file system
export PGUSER=$UID

# checking configuration
docker-compose config

# concat alertmanager configuration
cd alertmanager/etc/alertmanager
source createConfig.sh
cd ../../..

# create or update containers and network and starting detached
docker-compose up -d
sleep 5

# show important logs
docker-compose logs prometheus
docker-compose logs grafana
docker-compose logs alertmanager
docker-compose logs mailserver


echo "Open browser at http://localhost:3000/"

# show container status
watch docker-compose ps
