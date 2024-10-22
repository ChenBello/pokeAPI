# Terraform Configuration (main.tf)

provider "aws" {
    region = var.region # Replace with your region
}

# Define Key Pair (make sure it exists already or create it manually)
resource "aws_key_pair" "deployer_key" {
    key_name   = var.key_name # Use the same name as in your GitHub Actions script
    public_key = file(var.key_path) # Path to the public key file on your local system
}

# Security Group for EC2 instance
resource "aws_security_group" "pokeapi_sg" {
    name        = "PokeAPI-SG"
    description = "Allow HTTP, SSH and Flask ports"

    ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    }
}

# Find Amazon Linux 2 AMI
data "aws_ami" "amazon_linux_2" {
    most_recent = true
    owners      = ["amazon"]

    filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
    }
}

# EC2 instance
resource "aws_instance" "pokeapi_instance" {
    ami           = data.aws_ami.amazon_linux_2.id
    instance_type = var.instance_type
    key_name      = aws_key_pair.deployer_key.key_name
    security_groups = [aws_security_group.pokeapi_sg.name]

    tags = {
    Name = "PokeAPI"
    }

    user_data = <<-EOF
    #!/bin/bash
    # Update the system and install required packages
    sudo yum update -y
    sudo amazon-linux-extras install nginx1 -y
    sudo yum install -y python3 python3-pip git
    
    # Clone the repository
    git clone https://github.com/ChenBello/pokeAPI.git /home/ec2-user/PokeAPI

    # Install Python packages
    sudo pip3 install -r /home/ec2-user/PokeAPI/requirements.txt

    # Set up Gunicorn service
    sudo tee /etc/systemd/system/pokeapi.service <<EOL
    [Unit]
    Description=PokeAPI service
    After=network.target

    [Service]
    User=ec2-user
    WorkingDirectory=/home/ec2-user/PokeAPI/flask_app
    ExecStart=/usr/local/bin/gunicorn --workers 3 --bind unix:/home/ec2-user/PokeAPI/PokeAPI.sock app:app
    Restart=always

    [Install]
    WantedBy=multi-user.target
    EOL

    sudo systemctl daemon-reload
    sudo systemctl start pokeapi
    sudo systemctl enable pokeapi

    # Configure Nginx
    sudo tee /etc/nginx/conf.d/pokeapi.conf <<EOL
    server {
        listen 80;
        server_name _;

        location / {
            proxy_pass http://unix:/home/ec2-user/PokeAPI/PokeAPI.sock;
            proxy_set_header Host \$host;
            proxy_set_header X-Real-IP \$remote_addr;
            proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto \$scheme;
        }
    }
    EOL

    sudo nginx -t
    sudo systemctl restart nginx
    EOF
}

# Output EC2 instance Public DNS
output "public_dns" {
    value = aws_instance.pokeapi_instance.public_dns
}
