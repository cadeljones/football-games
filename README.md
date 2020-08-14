# docker
docker build -t footballgames-image .

run
docker run --name footballgames-container -p 80:80 footballgames-image


start
docker start footballgames-container

stop 
docker stop footballgames-container