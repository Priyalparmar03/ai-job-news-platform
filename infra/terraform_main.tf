terraform {

  required_version = ">= 1.5"

  required_providers {

    aws = {

      source  = "hashicorp/aws"

      version = "~> 5.0"

    }

  }

}

provider "aws" {

  region = "ap-south-1"

}

##################################################
# VPC
##################################################

resource "aws_vpc" "main" {

  cidr_block = "10.0.0.0/16"

  enable_dns_support = true

  enable_dns_hostnames = true

  tags = {

    Name = "ai-job-news-vpc"

  }

}

##################################################
# Internet Gateway
##################################################

resource "aws_internet_gateway" "gw" {

  vpc_id = aws_vpc.main.id

}

##################################################
# Public Subnet
##################################################

resource "aws_subnet" "public" {

  vpc_id = aws_vpc.main.id

  cidr_block = "10.0.1.0/24"

  availability_zone = "ap-south-1a"

}

##################################################
# Security Group
##################################################

resource "aws_security_group" "web" {

  name = "job-platform-sg"

  vpc_id = aws_vpc.main.id

  ingress {

    from_port = 22

    to_port = 22

    protocol = "tcp"

    cidr_blocks = [

      "0.0.0.0/0"

    ]

  }

  ingress {

    from_port = 8501

    to_port = 8501

    protocol = "tcp"

    cidr_blocks = [

      "0.0.0.0/0"

    ]

  }

  ingress {

    from_port = 80

    to_port = 80

    protocol = "tcp"

    cidr_blocks = [

      "0.0.0.0/0"

    ]

  }

  egress {

    from_port = 0

    to_port = 0

    protocol = "-1"

    cidr_blocks = [

      "0.0.0.0/0"

    ]

  }

}

##################################################
# EC2 Instance
##################################################

resource "aws_instance" "server" {

  ami = "ami-0f58b397bc5c1f2e8"

  instance_type = "t2.micro"

  subnet_id = aws_subnet.public.id

  vpc_security_group_ids = [

    aws_security_group.web.id

  ]

  associate_public_ip_address = true

  tags = {

    Name = "AI-Job-News-Platform"

  }

}

##################################################
# Output
##################################################

output "public_ip" {

  value = aws_instance.server.public_ip

}
