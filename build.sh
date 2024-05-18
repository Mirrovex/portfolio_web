#!/bin/bash

# Build the project
echo "Building the project..."
python3 -m pip install -r requirements.txt

echo "Make Migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear


if [[ $(uname) == 'Linux' ]]; then
    echo "System operacyjny: Linux"
elif [[ $(uname) == 'Darwin' ]]; then
    echo "System operacyjny: macOS"
elif [[ $(uname) == 'MINGW'* ]]; then
    echo "System operacyjny: Windows"
else
    echo "Nieznany system operacyjny"
fi


apt-get install libjpeg62