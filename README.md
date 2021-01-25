# predict-job-transition
Job transition success predictor model deployment and testing

This project deploys an ML model([model.pkl](https://github.com/shriadke/predict-job-transition/blob/main/model.pkl)) for predicting successful job transition. The model's prediction meethods are exposed over a REST API with Flask. The entire app is deployed using Docker container.

[app.py](https://github.com/shriadke/predict-job-transition/blob/main/app.py) contains the main application with 2 POST methods: model.predict() and model.predict_proba() This can be run locally by simply running this file as:

```
python3 app.py
```

The 2 methods are separately provided over POST along with Http request. The request json must contain data from [candidates.json](https://github.com/shriadke/predict-job-transition/blob/main/candidates.json) in order to predict the job transition success. 

We can test the API by running [test_app.py](https://github.com/shriadke/predict-job-transition/blob/main/test_app.py) (provided the app is running on server).

This model and app can be deployed using a docker container. For this, the deployment instructions are in [Dockerfile](https://github.com/shriadke/predict-job-transition/blob/main/Dockerfile) and [requirements.txt](https://github.com/shriadke/predict-job-transition/blob/main/requirements.txt) contains the necessary packages to be installed. Follow the below steps to build and run the given model using the container in the current project directory:

```
docker build -t  job_transition_app .
```

```
docker run -p <port>:<port> job_transition_app
```


## Load Testing of API

The API can be load tested using [Locust](https://locust.io/) which is an open-source load testing tool. Install locust using `pip install locust`. This is a very useful tool that lets you simulate number of users and the concurrent requests for the API.

[locustfile.py]() defines the task to be tested and it allows the tool to test the API with the help of interactive web UI. `locust --host=http://localhost:9000  --locustfile locustfile.py` will run the web UI on [http://localhost:9000](http://localhost:9000) where we can specify the required load parameters such as No. of concurrent users, spawn rate.

Following are the screenshots for the test tool and the corresponding results for 120 seconds with 100 concurrent users.

![test paramaters](https://github.com/shriadke/predict-job-transition/blob/main/imgs/test_start.JPG)

![Overall Statistics](https://github.com/shriadke/predict-job-transition/blob/main/imgs/locust_home.JPG)

![Requests served per second](https://github.com/shriadke/predict-job-transition/blob/main/imgs/total_rps.JPG)

![Response Time](https://github.com/shriadke/predict-job-transition/blob/main/imgs/resp_time.JPG)

From the results it can be seen that, there was a initial failure due to a delay of 10 sec that the request could not be processed. The other metrics such as peak/average response times can be observed in the given charts and the overall stats. These results are obviously a bit average as the model was deployed on a local machine/server with many other (system started) processes affecting the performance.

In future, to deploy this model in production the latency should be handled. This can be done with the help of AWS's API gateways or similar platforms that serves a larger load at lower costs. 
