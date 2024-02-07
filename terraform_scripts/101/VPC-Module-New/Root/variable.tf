#AWS Region
variable "region" {
    description = "define the AWS region to create VPC"
    type = string
    # default = "ap-south-1"   # instead of declaring this default value here in variable.tf , we will declare it in variable.tfvars
}

variable project_name {
    description = "name of application"
}

variable "vpc_cidr" {
  description = "cidr Block value for VPC"
  type = string
#   default = "10.0.0.0/16"
}

variable "pub_sub_1a_cidr" {}
variable "pub_sub_1b_cidr" {}
variable "pri_sub_1st" {}
variable "pri_sub_2nd" {}
  
