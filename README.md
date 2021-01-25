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


