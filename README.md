# AWS Step Functions
"AWS Step Functions is a web service that enables you to coordinate the components of distributed applications and microservices using visual workflows. You build applications from individual components that each perform a discrete function, or task, allowing you to scale and change applications quickly."

I've learned Step Functions by the following example and I hope it can clear things for you.

# Algorithm
<p align="center">
  <img src="images/algorithm.png"/>
</p>


### Suppose that each process block is an AWS Lambda Function, this how the StepFunction looks like
<p align="center">
  <img src="images/statemachine.png"/>
</p>

# Apply it
* Clone this repo
* Create a python virtualenv inside it, and install pip requirments
```
$ git clone git@github.com:OsamaJBR/teach-me-aws-stepfunctions.git
$ cd teach-me-aws-stepfunctions
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirement.txt
```
* Start deploying functions using [Zappa](https://github.com/Miserlou/Zappa)
```
$ cd sub_numbers_lambda; zappa deploy develop
$ cd greater_than_lambda; zappa deploy develop
$ cd less_than_lambda; zappa deploy develop
$ cd final_state_lambda; zappa deploy develop
```
* Go to Amazon Console (AWS Lambda) page and get all ARN for the above lambda functions
* Edit steps.json file and add ARN inside the related state defenetion
```
...
"SubNumbers": {
    "Type": "Task",
    "Resource": "XXXXXXXXXXXX",
    "Next": "ChoiceState"
},
...
```
