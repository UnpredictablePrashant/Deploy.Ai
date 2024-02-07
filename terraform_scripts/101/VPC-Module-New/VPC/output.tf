output "vpc_id" {
    value = aws_vpc.vpc.id
}

output "internet_gateway" {
    value = aws_internet_gateway.internet_gateway
  
}
output "pub_sub_1a_id" {
    value = aws_subnet.pub_sub_1a.id
}

output "pub_sub_1b_id" {
    value = aws_subnet.pub_sub_1b.id
}

output "pri_sub_1st_id" {
    value = aws_subnet.pri_sub_1st.id
  
}

output "pri_sub_2nd_id" {
    value = aws_subnet.pri_sub_2nd.id
  
}