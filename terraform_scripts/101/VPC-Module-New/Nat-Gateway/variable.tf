variable "pri_sub_1st_id" {
  description = "this is ID of pub_sub_1a, getting from Output.tf of ./VPC folder. this output"
  type = string
}

variable "pri_sub_2nd_id" {
  description = "here we store id od pub_sub_1b, this value we're getting from Output.tf of ./VPC folder."
}

variable "pub_sub_1a_id" {}

variable "pub_sub_1b_id" {}

variable "internet_gateway" {
  description = "storing output of igw from output.tf of ./vpc folder"
}

variable "vpc_id" {
    description = "vpc_id varibale - this varibale defined at output.tf in ./VPC "
}