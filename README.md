# Deploy.Ai

 This is an AI Deployment Planner. Users can converse with an AI Bot that is specially trained to provide you a personalized plan for your deployment needs. This project is divided into three parts, this is the main repository and there are three other repositories which are the subset of this repository. 

1. Landing Page and Authentication
2. Deployment Plan Created By AI
3. Deployment Performed by Python Automation

## Part 1: Landing Page with Authentication, User Profiles and Chatbot features
For this purpose we are using plain html (index.html),css and javascript, along with Amazon Cognito for authentication. User will use email id and verification to start using the bot. For the Purpose of bot features/frontend we will be using Kommunicate or kore.ai. It will either be a standalone solution or be a frontend for lex or chatgpt. 


## Part 2: Deployment Plan Created by AI

For this purpose we use two AI agents, one is ChatGPT's custom bot creation feature and the other is Amazon Lex. We built these AI agents by feeding various self created custom knowledge base. The bot is designed to interact with the user and ask relevent questions about their deployment requirements. Based upon these requirements the bot generates a deployment plan. It also requests the users if they want to deploy the plan. Upon confirmation, the bot generates file.json that automatically gets stored in json_dumps folder (or possibly in an s3 bucket in the future). It also stores in (deployment_architecture) and sends an architecture drawing to the users slack account. (whimsical maybe used for diagram generation)

Things to do (part 2):
Another file that contains secrets may also get generated by the bot, the details of it will be used by tf scrpits.


## Part 3: Deployment Performed by Python

In part three we created the json_read.py file that looks for any json file from the json_dumps folder. If there is any, then it compares the contents against the contents of all the files in the folder json_library. If it finds a match then that file number becomes the result. We have set conditions the run based on the file number we get on the result. For example, the result is 101, then the programs instructs the os to change directory into the terraform_scripts/101 directory and then applies the corresponding terraform script.

Once the infra is created by terraform, the ansible scripts are used to deploy and ensure the website works.

## Where is this Main Project Deployed?

We are using two ec2 instances in two different availability zones. They are load balanced. Github actions is used to update the local repository. Nginx is set up with a domain name. We are also using cloudflare for this purpose. For SSL we are using certbot. 



## Repository Structure:

Files:

* /json_read.py - main file that reads the contents of the json file and matches with existing deployment json's. Then runs the corresponding infrastructure scripts and other scripts necessary for deployment. 

* /json_read_starter.py - 


* /website/index.html - landing page for the website

Things To Do:

0. S3 bucket instead of dumps folder
1. Compare json against dynamoDB/documentDB instead of other jsons in the library.
2. Create more Json files and store it in spare library of more use cases.
3. 
