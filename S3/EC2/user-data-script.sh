#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
echo "<h1>Hello world from my ec2 machine $(hostname)</h1>" > /var/www/html/index.html