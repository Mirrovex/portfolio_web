#!/bin/bash

# Build the project


echo " -> LIBJPEG"

#yum update -y
#yum install -y libjpeg-turbo libjpeg-turbo-devel gcc python3-devel zlib-devel freetype-devel

#find /usr/lib* -name "libjpeg.so.62"

#export LD_LIBRARY_PATH=/usr/lib64:/usr/local/lib:$LD_LIBRARY_PATH
#echo $LD_LIBRARY_PATH

yum install libjpeg62


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
