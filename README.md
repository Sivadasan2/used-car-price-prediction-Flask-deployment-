User Car price prediction using the Python and Sklean lib.

The project is aimed to predict the price of the car using Trained ML module with help of historical data.

Docker commands to build and run in local docker desktop.

# build the Docker image
docker build -t user_car_price_pred:latest .

#Run the Docker image 
docker run -p 8000:8000 -d user_car_price_pred

Steps to push the docker image to Pubilc or private docker repo

Login the Docker hub cred
docker login

Tagging the docker image 
docker tag siva1975/user_car_price_pred
docker push siva1975/user_car_price_pred


