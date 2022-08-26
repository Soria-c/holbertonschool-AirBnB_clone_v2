#!/usr/bin/env bash
# Setting up for deployment

sudo apt update -y
sudo apt upgrade -y
sudo apt install nginx -y

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared

echo "test" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data


find_str="^\t\}$"
replace_str="\t\}\n\n\tlocation \/hbnb_static\/ \{\n\t\talias \/data\/web_static\/current\/;\n\t\}"

sudo sed -i "0,/$find_str/s//$replace_str/" /etc/nginx/sites-available/default

sudo service nginx restart
