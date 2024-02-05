#AWS Region
variable "region" {
    description = "define the AWS region to create VPC"
    type = "string"
    # default = "ap-south-1"   # instead of declaring this default value here in variable.tf , we will declare it in variable.tfvars
}

# variable project_name {
#     description = "name of application"
# }