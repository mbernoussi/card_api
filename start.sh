#!/bin/bash
. .env 
echo "Please enter the MONGO DB ROOT Password"
read -sp "MONGO DB ROOT PASSWORD": mongo_db_root_password

echo "Please enter the MONGO DB DATABASE Password"
read -sp "MONGO DB PASSWORD": mongo_db_database_password

docker-compose build

function launch_container() {
    container_name="$1"
    container_port="$2"
    if [ "$(docker ps -aq -f status=exited -f name=${container_name})" ]; then
        docker rm ${container_name}
        echo 1234
    fi
    if [ ! -z $container_port ]; then
        echo${container_name}
        docker-compose run -d --name ${container_name} -e MONGO_INITDB_ROOT_PASSWORD=${mongo_db_root_password} -e MONGO_PASSWORD=${mongo_db_database_password} -p ${container_port}:${container_port} ${container_name}
    else 
        docker-compose run -d --name ${container_name} -e MONGO_INITDB_ROOT_PASSWORD=${mongo_db_root_password} -e MONGO_PASSWORD=${mongo_db_database_password} ${container_name}
    fi
}

launch_container "${API_CONTAINER_NAME}" "${API_CONTAINER_PORT}" && launch_container "${MONGO_CONTAINER_NAME}"