# Terraform Variables (variables.tf)

variable "key_name" {
    description = "Name of the AWS Key Pair"
    type        = string
    default = "vockey.pem"
}

variable "key_path" {
    description = "Path to the public key file"
    type        = string
    default = "C:\\Users\\chenb\\OneDrive\\שולחן העבודה\\עמותת תפוח\\הגשות\\"
}

variable "region" {
    type = "string"
    default = "us-east-2"
}

variable "vpc_name" {
    type = "string"
    default = "terraform-vpc"
}

# provider "aws" {
#     region = var.region
# }

# resource "aws_vpc" "myvpc" {
#     cidr_block = "10.0.0.0/16"
#     enable_dns_support = true
#     enable_dns_hostnames = true

#     tags = {
#         Name = var.vpc_name
#     }
# }


variable "subnet_name" {
    type = "string"
    default = "terraform-subnet"
}

variable "sshport" {
    type = number
    default = 22
}

variable "httpport" {
    type = number
    default = 80
}

variable "keypair_name" {
    type = string
    default = "vockey" # "terraform-keypair"
}

variable "securitygroup_name" {
    type = string
    default = "terraform-sg"
}

variable "instance_name" {
    type = string
    default = "terraform-instance"
}

variable "instance_type" {
    type = string
    default = "t2.micro"
}
