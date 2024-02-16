# Stepupsage.ai

 Introducing Stepupsage.ai - Your AI-driven Cloud Deployment Companion! Leveraging the power of AI, Deploy.ai transforms the way you estimate costs, plan, and migrate applications to the AWS Cloud. 
 This project is divided into three parts, this is the main repository and there are three other repositories which are the subset of this repository. 

1.	Landing Page and Authentication
2.	AWS services Cost Estimation & generate a Deployment Planner By AI-Driven ChatBot
3.	Provision AWS infrastructure & Deploy the user app code on cloud services using Python Automation
4.	Monitor logs and send completion emails to users using Slack.


## Features

    AI-Powered Interactions: Integrated with OpenAI API, Deploy.ai converses with users to gather specific application requirements.
    Cost Estimation: Connects with the AWS Cost Calculator API to furnish detailed monthly or yearly cost estimates for the desired AWS services.
    Deployment Planning: Generates a JSON-based deployment plan (file.json), tailored to user-provided specifications.
    AWS Architecture Visualization: Automatically creates and shares a comprehensive AWS architecture diagram, visualizing the planned services.
    Terraform Automation: Utilizes file.json to provision infrastructure on AWS, tapping into powerful Terraform modules for infrastructure as code.
    Ansible Configuration: Employs Ansible for meticulous environment setup and application deployment, ensuring consistency across AWS services.
    Health Monitoring: Post-deployment, Deploy.ai conducts health checks and establishes a monitoring dashboard using Grafana for real-time application insights.
    Progress Tracking: Offers the ability to save progress and issues Jira tickets to track deployment stages.

## Workflow

    Initial Setup: Users land on the homepage and register via AWS Cognito.
    Engagement: The AI ChatBot engages users, querying about application specifics and desired AWS resources.
    Planning & Costing: A JSON deployment plan is generated, and a cost estimation is provided, alongside an AWS architecture diagram.
    User Decision Point: Users decide whether to proceed with the deployment.
        Yes: Users provide AWS credentials, and Deploy.ai begins infrastructure provisioning with Terraform, followed by Ansible for deployment.
        No: Progress is saved, and the ChatBot offers to restart the conversation or save the session for later.
    Deployment & Monitoring: Once deployed, application health is checked, and a monitoring dashboard is set up.
    Completion Notification: A comprehensive notification is sent to the user via Slack and email, detailing the deployment and next steps.

## Architecture Overview

    Multi-AZ Deployment: Ensures high availability by spanning across multiple Availability Zones.
    Secure Authentication: Leverages AWS Cognito for secure user sign-in.
    CI/CD Integration: Integrates with GitHub Actions and Docker Hub for continuous integration and deployment.
    Centralized Monitoring: Utilizes CloudWatch and SNS for detailed monitoring and alerts.

## Flowchart
![Flowchart-deploy ai](https://github.com/UnpredictablePrashant/Deploy.Ai/assets/139486876/e32f9163-f9fa-4503-a699-8715745d122a)

## Architecture
![Architecture-Setupsage ai](https://github.com/UnpredictablePrashant/Deploy.Ai/assets/139486876/abd504df-2e4f-4314-b065-113fc499475a)


## Where is this Main Project Deployed?

We are using an ec2 instance with an elastic IP attached to it. Github actions is used to update the local repository. Nginx is set up with a domain name. We are also using cloudflare for this purpose. For SSL we are using certbot. 

### Are you well architected?

We are using the AWS's Well Architected Framework to create this project which ensures operational excellence, performance efficency, reliability, sustainability, security and cost optimization. 



## Repository Structure:

Files:

* /json_read.py - main file that reads the contents of the json file and matches with existing deployment json's. Then runs the corresponding infrastructure scripts and other scripts necessary for deployment. 

* /json_read_starter.py - 


* /website/index.html - landing page for the website

Things To Do:

0. S3 bucket instead of dumps folder
1. Compare json against dynamoDB/documentDB instead of other jsons in the library.
2. Create more Json files and store it in spare library of more use cases.
3. Make json_read file more classy with functions and classes.
After the infra is created and the application is deployed, users get to see the evidence with either system manager or resource explorer. 

Future Plans:
Currently in the json_read.py file, we are creating infrastructure and config based on conditions written for each json deployment case.

But later, we would like to create an AI model that will be used to automatically figure out the corresponding codes to run by reading the Terraform scripts.

Or even better, we would build the AI model by training it on various TF scripts so that it would automatically create the Terraform scripts.

With the input provided by the user, this AI model will detect the type of deployment.

1. By analyzing the JSON file, this AI model would be able to identify patterns and dependencies within the infrastructure and configuration requirements. This would eliminate the need for manual coding and reduce human errors, resulting in a more efficient and accurate deployment process. Additionally, the AI model could continuously learn and adapt to new deployment scenarios, enhancing its capabilities over time. 

2. The AI model would then translate these natural language inputs into the appropriate Terraform scripts, further simplifying the deployment process for users. deployment case in the json_read.py file.

3. Discussing the future vision: Explain how there is a plan to develop an AI model that can automatically determine the corresponding codes to run by reading Terraform scripts, which would eliminate the need for manual intervention.

4. Highlighting improved efficiency: Elaborate on how building an AI model by training it on various TF scripts would lead to greater automation and efficiency in creating Terraform scripts, as it would be able to generate them automatically.

5. Describing user interaction: Write about how this proposed AI model could incorporate user input to detect different types of deployments accurately, making it more versatile and adaptable for various scenarios.

6. Addressing potential benefits: Explore the potential advantages of implementing such an AI-driven system, including reduced human error, a faster script generation process, scalability, and better resource allocation based on specific deployment requirements.




