#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
EC2_AZ=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
EC2_REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/region)
echo "<h1>Hello world from my ec2 machine. <br>Hostname = $(hostname) <br>Availability Zone = $EC2_AZ <br>Region = $EC2_REGION </h1>" > /var/www/html/index.html
