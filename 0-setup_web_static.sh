#!/usr/bin/env bash
# sets up web servers for deployment of web_static
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
hbnb="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sed -r -i "/^\s+server_name .+;/a\ $hbnb" /etc/nginx/sites-available/default
service nginx restart
