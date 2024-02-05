#Creation Deatils of VPC
module "vpc" {
    source = "./VPC"
    # vpc_name= var.vpc.name  #not sure of the variable mentioned here , Double check
    cidr = var.vpc_cidr
    project_name = var.project_name
    pub_sub_1a_cidr = var.pub_sub_1a_cidr
    pub_sub_1b_cidr = var.pub_sub_1b_cidr
    pri_sub_1st = var.pri_sub_1st
    pri_sub_2nd = var.pri_sub_2nd 
  
}



# #Create NAT-Gateway
# module "NAT" {
#     source = "../Nat-Gateway"
  

# }