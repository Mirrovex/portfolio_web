#!/bin/bash

# Build the project

#echo "Installing libjpeg..."
#yum install libjpeg libjpeg-dev libjpeg-devel libpng-devel libjpeg-turbo libjpeg-turbo-devel --assumeyes


echo "Sprawdzanie instalacji libjpeg:"
yum update -y && yum install -y libjpeg-dev libjpeg

ls -l /usr/lib64/libjpeg*
ls -l /usr/lib/libjpeg*

# Tworzenie symbolic linku do libjpeg.so.62
ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so.62 /usr/lib/libjpeg.so.62

#echo "Libjpeg settings..."
find /usr/lib* -name "libjpeg.so.62"
#echo $LD_LIBRARY_PATH


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

#python3 -m pip install --force-reinstall Pillow
