#template sourced from https://github.com/prakhar1989/FoodTrucks/blob/master/setup-docker.sh
#pull postgres image from dockerhub
docker pull postgres

#build flask app container
docker build -t flaskapp app/

# create the network
docker network create userdatabase-net

# start the database container
docker run -d --network userdatabase-net --name postgres-docker -e POSTGRES_PASSWORD=docker -p 5432:5432 -v db/ postgres

#start the flask app container
echo "Starting server..."
sleep 10s
docker run -d --network userdatabase-net --name flaskapp-docker -p 5000:5000 flaskapp

#show containers running
docker ps
echo "Use . uninstall.sh to stop all containers and remove them along with the created network."
echo "You can also uncomment the corresponding line to remove the images as well."
