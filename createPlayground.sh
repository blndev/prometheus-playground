# setting PGUSER to current user is, which allows to write to the local file system
export PGUSER=$UID

# create or update containers and network and starting detached
docker-compose up -d
sleep 5

# show important logs
docker-compose logs prometheus
docker-compose logs grafana

# show container status
docker-compose ps

echo "Open browser at http://localhost:3000/"
