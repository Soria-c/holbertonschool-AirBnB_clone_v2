#!/usr/bin/env bash
# Setting up for deployment

sudo apt update -y
sudo apt upgrade -y
sudo apt install nginx -y

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared

echo "test" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data


sudo sed -i "/{/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

sudo service nginx restart
