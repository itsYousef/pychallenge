# Serverless Django Rest API

This project is a serverless Django RESTful API that uses Django REST framework, Serverless platform and AWS cloud services ([AWS API Gateway](https://aws.amazon.com/api-gateway/), [AWS Lambda](https://aws.amazon.com/lambda/), [AWS DynamoDB](https://aws.amazon.com/dynamodb/)).

## Installation and Usage

### Install and run locally

* Clone this repository:
```bash
git clone https://github.com/itsYousef/pychallenge.git
```

* Navigate to the project directory:
```bash
cd pychallenge
```

* Install python dependencies using the following command:
```bash
python -m pip install -r requirements.txt
```

* Install and start Dynalite(An implementation of Amazon's DynamoDB built on LevelDB that can be used for local development and testing) using the following two commands:
(or  you can install the actual DynamoDB local using this [official guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html))

```bash
npm install -g dynalite
npm dynalite --port <port-number>
```
* Create a environment variable file according to the following format:
```
STAGE=dev # for testing and running locally it should be 'dev'
DB_TABLE=devices # your table name
DYNAMODB_LOCAL_ENDPOINT=http://localhost:5454 # your local database connection url
REGION=eu-north-1 # your aws region
```

* Run migrations(only for local database):
```bash
python dynamo_migrator.py
```

* Start the development server:
```bash
python manage.py runserver
```

* Visit http://localhost:8000/api/devices in your browser

#### Usage
You can create and retrieve a device by using the following commands:

##### Create a device
```bash
curl -X POST http://127.0.0.1:8000/api/devices/ --data '{ "id": "/devices/id1", "deviceModel": "/devicemodels/id1", "name": "Sensor", "note": "Testing a sensor.", "serial": "A020000102" }'
```

##### Get one device by its ID

```bash
# Replace the <id> part with a real id
curl http://127.0.0.1:8000/api/devices/<id>
```

### Testing
* To run the tests you need to start the dynalite as described before and configure environment variables accordingly and then run the following command:
```bash
python .\manage.py test
```

### Deployment on AWS Cloud

* Configure your aws account using the following command and provide requested information about your AWS account:
```bash
aws configure
```

* Change STAGE environment variable to prod:
```
STAGE=prod
```

* In order to deploy the endpoint simply run

```bash
serverless deploy --verbose
```