

# The Allocation ID of the Elastic IP address for the NAT Gateway. Required for connectivity_type of public.
# Connectivity type for the NAT Gateway. Valid values are private and public. Defaults to public.

# allocate elastic ip. this eip will be used for the nat-gateway in the public subnet pub-sub-1a
resource "aws_eip" "eip-nat-gateway-1a" {
  domain = "vpc"
  tags   = {
    Name = "eip-nat-gateway-1a"
  }
}

# allocate elastic ip. this eip will be used for the nat-gateway in the public subnet pub-sub-2b
resource "aws_eip" "eip-nat-gateway-1b" {
  domain = "vpc"

  tags   = {
    Name = "eip-nat-gateway-1b"
  }
}



#Create 2 NAT-Gateways  inside 2 Public subnet created <pub_sub_1a, pub_sub_1b>
resource "aws_nat_gateway" "nat-gateway-1a" {
    allocation_id = aws_eip.eip-nat-gateway-1a.id
    subnet_id = var.pub_sub_1a_id #pub_sub_1a_id is the variable mentioned in ./VPC/output.tf - it is Output of main.tf file present in ./VPC

    tags = {
        Name = "nat-gateway-1a"
    }

  # To ensure proper ordering, it is recommended to add an explicit dependency
  # on the Internet Gateway for the VPC.
  depends_on = [ var.internet_gateway]
}

resource "aws_nat_gateway" "nat-gateway-1b" {
  allocation_id = aws_eip.eip-nat-gateway-1b.id
  subnet_id = var.pub_sub_1b_id
  
    tags = {
        Name = "nat-gateway-1b"
    }

    depends_on = [ var.internet_gateway ]
}

#Create 1 Private-Route-Table for 2 Private-subnets, and routes Destination of traffic to the NAT gateway- for private subnet.
# Add 2 NAT-GATEWAYS to this 1 private route table .
#to create pri-RT,use the same code as "aws_route_table" , only use NAT-Gateway instead of Internet-Gateway , in route {} section.

resource "aws_route_table" "private_RT" {
    vpc_id = var.vpc_id

    route {
        cidr_block = "0.0.0.0/0"
        nat_gateway_id = aws_nat_gateway.nat-gateway-1a.id
    }

    route {
        cidr_block = "0.0.0.0/0"
        nat_gateway_id = aws_nat_gateway.nat-gateway-1b.id
    }

    tags = {
      Name = "private_RT"
    }
  
}

# associate private subnet pri-sub- with private route table private_RT
resource "aws_route_table_association" "pri_sub_1st_with_private_RT" {
  subnet_id         = var.pri_sub_1st_id
  route_table_id    = aws_route_table.private_RT.id
}

# associate private subnet pri-sub-4b with private route table Pri-rt-b
resource "aws_route_table_association" "pri_sub_2nd_with_public_RT" {
  subnet_id         = var.pri_sub_2nd_id
  route_table_id    = aws_route_table.private_RT.id
}

