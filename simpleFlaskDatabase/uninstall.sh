#removes containers and network
docker stop postgres-docker flaskapp-docker
docker rm postgres-docker flaskapp-docker
docker network rm userdatabase-net

#uncomment to remove images as well
#docker image rm postgres flaskapp
