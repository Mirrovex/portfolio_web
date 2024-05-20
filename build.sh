#!/bin/bash

# Build the project


echo " -> LIBJPEG"

#echo "Libjpeg settings..."
#find /usr/lib* -name "libjpeg.so.62"
#echo $LD_LIBRARY_PATH


yum update -y
yum install -y libjpeg-turbo libjpeg-turbo-devel gcc python3-devel zlib-devel freetype-devel

export LD_LIBRARY_PATH=/usr/lib64:/usr/local/lib:$LD_LIBRARY_PATH


echo "Building the project..."
python3 -m pip install -r requirements.txt
python3 -m pip install --no-binary :all: --force-reinstall pillow

echo " -> Sprawdzenie dostępności libjpeg w Pillow"
python3 -c "from PIL import Image; print('JPEG support:', 'jpeg' in Image.registered_extensions().values())"


echo "Make Migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear

# cat /etc/os-release
# uname -a
# cat /proc/version

#python3 -m pip install --force-reinstall Pillow
