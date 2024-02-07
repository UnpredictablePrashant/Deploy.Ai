#Creation Deatils of VPC
module "vpc" {
    source = "../VPC"
    # region = var.region
    # vpc_name= var.vpc.name  #not sure of the variable mentioned here , Double check
    vpc_cidr   = var.vpc_cidr
    project_name = var.project_name
    pub_sub_1a_cidr = var.pub_sub_1a_cidr
    pub_sub_1b_cidr = var.pub_sub_1b_cidr
    pri_sub_1st = var.pri_sub_1st
    pri_sub_2nd = var.pri_sub_2nd 
  
}


#Here module.vpc.<variable> = mean, we are taking vlaues from the output of VPC module & using thoes in NAT-GATEWAY module as input.
# in this module.vpc.<variable> = .<variable> , is the variable declared also in ./Nat-Gateway/variable.tf

# #Create NAT-Gateway
module "Nat_Gateway" {
    source = "../Nat-Gateway"


    vpc_id = module.vpc.vpc_id
    internet_gateway = module.vpc.internet_gateway
    pub_sub_1a_id = module.vpc.pub_sub_1a_id
    pub_sub_1b_id = module.vpc.pub_sub_1b_id
    pri_sub_1st_id = module.vpc.pri_sub_1st_id
    pri_sub_2nd_id = module.vpc.pri_sub_2nd_id
    
}

module "security-group" {
    source = "../security-group"
    vpc_id = module.vpc.vpc_id
    project_name = var.project_name
}

module "EC2-Keypair" {
  
    source = "../EC2-Keypair"
    project_name = var.project_name
}