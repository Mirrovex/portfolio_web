#!/bin/bash

# Build the project
echo "Building the project..."
python3 -m pip install -r requirements.txt

echo "Make Migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear

# cat /etc/os-release
# uname -a
# cat /proc/version

echo "Installing libjpeg..."
yum install libjpeg-turbo
yum install libjpeg

echo "Libjpeg settings..."
find /usr/lib* -name "libjpeg.so.62"
echo $LD_LIBRARY_PATH