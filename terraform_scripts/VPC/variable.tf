variable "project_name" {
    description = "difne your project name" 
}
# IPV4 CIDR Block value for VPC
variable "vpc_cidr" {
  description = "cidr Block value for VPC"
  type = string
#   default = "10.0.0.0/16"
}

#CIDR Block value for Public-Subnet   #we need to fill this CIDR range, as per how may subnets we want (Public)
#  variable "pub_sub_1a_cidr" {
#     type = list(string)
# #    default = ["10.0.101.0/24", "10.0.102.0/24"]
#  }
variable pub_sub_1a_cidr {
    default = "1st public subnet"
    type = string
}

#  #CIDR Block value for Private-Subnet   #we need to fill this CIDR range, as per how may subnets we want (Private)
#  variable "cidr_private_sub" {
#     type = list(string)
#     # default = [ "10.0.1.0/24", "10.0.2.0/24" ]
#  }
variable  pub_sub_1b_cidr {
    default = "create 2nd public subnet"
    type = "string"
}

#First Private subet
variable  pri_sub_1st {
    default = "create 1st  Private subnet"
    type = "string"
}

variable  pri_sub_2nd {
    default = "create 2nd  Private subnet"
    type = "string"
}


 