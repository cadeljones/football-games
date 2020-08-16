# Football Games API
> An API that returns NFL events with information about the involved teams 


## View Demo
The API and its interactive docs can be found at [footballgames.cadeljones.com](https://footballgames.cadeljones.com/)

## Technologies
* [Python](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)

## To run the project locally
This project can be run locally using either docker or python

In either scenario you will need to configure environment variables in a .env file alongside the .env.example file.
The important one is the NFL_API_KEY which allows the app to retrieve NFL data from the source API


### Docker
[Install Docker](https://docs.docker.com/get-docker/)

To build the image   
`docker build -t footballgames-image .`

To build and start the container for the first time   
`docker run --name footballgames-container -p 8000:80 footballgames-image`

Open the project in your web browser at   
[localhost:8000](localhost:8000)

To stop the container   
`docker stop footballgames-container`

To re-start the container   
`docker start footballgames-container`

To view logs   
`docker logs -f footballgames-container`

### Python
In order to run this project you need to be running Python 3.6+

It is also recommended that you use one of the many tools that allows you to work in a python virtual
environment.

1. Install the required Python packages   
`pip install -r requirements.txt`

1. Run the server   
`uvicorn app.main:app --reload

1. Open the project in your web browser at   
[localhost:8000](localhost:8000)


## To-do list:
- [ ] Descriptions for `games/` endpoint
- [ ] Test with dummy data
- [ ] Test data validators
- [ ] Add key auth to limit usage

