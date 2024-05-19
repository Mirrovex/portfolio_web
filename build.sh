#!/bin/bash

# Build the project


echo " -> LIBJPEG"

#echo "Libjpeg settings..."
#find /usr/lib* -name "libjpeg.so.62"
#echo $LD_LIBRARY_PATH


# Aktualizacja pakietów i instalacja libjpeg-turbo
yun update -y && yun install -y libjpeg-turbo


echo "Building the project..."
python3 -m pip install -r requirements.txt

# Sprawdzenie dostępności libjpeg w Pillow
python -c "from PIL import Image; print('JPEG support:', 'jpeg' in Image.registered_extensions().values())"


echo "Make Migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear

# cat /etc/os-release
# uname -a
# cat /proc/version

#python3 -m pip install --force-reinstall Pillow
