# Football Games API
> 


## View Demo
The API can be found here [footballgames.cadeljones.com](https://footballgames.cadeljones.com/)

## Info

## Technologies
* Python
* FastAPI

## To run the project Locally

### Docker
[Install Docker](https://docs.docker.com/get-docker/)

To build the images
`docker build -t footballgames-image .`

To build and start the container for the first time
`docker run --name footballgames-container -p 8000:80 footballgames-image`

To stop the container
`docker stop footballgames-container`

To re-start the container
`docker start footballgames-container`

To view logs
`docker logs -f footballgames-container`

### 

## To-do list:
- [ ] test with dummy data
- [ ] test data validators
- [ ] Todo add key auth to limit usage

