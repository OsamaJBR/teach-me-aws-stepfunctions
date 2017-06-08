# AWS Step Functions
"AWS Step Functions is a web service that enables you to coordinate the components of distributed applications and microservices using visual workflows. You build applications from individual components that each perform a discrete function, or task, allowing you to scale and change applications quickly."
 
I've learned Step Functions by the following example and I hope it can clear things for you.
 
# Algorithm (Example)
<p align="center">
 <img src="images/algorithm.png"/>
</p>
 
In step functions, you can consider that each process block is an AWS Lambda Function, that takes the output of previous as it's input.
 
# Apply it
1- Clone this repo
2- Create a python virtualenv inside it, and install pip requirements
```
$ git clone git@github.com:OsamaJBR/teach-me-aws-stepfunctions.git
$ cd teach-me-aws-stepfunctions
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirement.txt
```
3- Start deploying functions using [Zappa](https://github.com/Miserlou/Zappa)
```
$ cd sub_numbers_lambda; zappa deploy develop
$ cd greater_than_lambda; zappa deploy develop
$ cd less_than_lambda; zappa deploy develop
```
4- Go to Amazon Console (AWS Lambda) page and get all ARN for the above lambda functions
5- Edit steps.json file and add ARN inside the related state definition
```
...
"SubNumbers": {
   "Type": "Task",
   "Resource": "XXXXXXXXXXXX",
   "Next": "ChoiceState"
},
...
```
6- Edit final_state_lambda by adding the SNS Topic ARN in the code, then deploy the function using zappa again
```
$ cd final_state_lambda; vim handle.py
...
response = client.publish(
   TargetArn="XXXXXXXXXXXXXXX",
   Message=json.dumps({'default': json.dumps(message)}),
   MessageStructure='json'
)
...
$ zappa deploy develop
```
7- Go to Amazon Step Function page, the Create State Machine. Past the edited steps.json inside the Code panel. Then you should see this in the Preview section.
<p align="center">
 <img src="images/statemachine.png"/>
</p>
* If everything is ok, create it.
 
# How to test it
1- Go to the new state machine, and press on new execution.
2- Insert the following as input, and start the execution.
```
{
 "key1" : 100,
 "key2" : 300
}
```
<p align="center">
 <img src="images/example.png"/>
</p>
3- The final state suppose to send an SMS to the phone number subscribed in the SNS Topic.
<p align="center">
 <img src="images/sms-rec.png"/>
</p>
