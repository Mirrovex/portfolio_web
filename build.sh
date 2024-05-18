#!/bin/bash

# Build the project
echo "Building the project..."
python3 -m pip install -r requirements.txt

echo "Make Migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear


if command -v apt-get &> /dev/null; then
    echo "System operacyjny: Debian/Ubuntu"
    # Tutaj użyj komendy apt-get
    # Na przykład:
    # apt-get update
    # apt-get install -y nazwa_pakietu
# Sprawdź, czy apk jest dostępny (Alpine Linux)
elif command -v apk &> /dev/null; then
    echo "System operacyjny: Alpine Linux"
    # Tutaj użyj komendy apk
    # Na przykład:
    # apk update
    # apk add nazwa_pakietu
else
    echo "Nieznany system operacyjny"
fi

apk search libjpeg
apk add libjpeg62