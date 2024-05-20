FROM ubuntu:22.04

# Aktualizacja pakietów i instalacja zależności
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev libjpeg-dev zlib1g-dev libfreetype6-dev gcc

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie plików projektu
COPY . .

# Instalacja zależności Python
RUN pip3 install --upgrade pip && \
    pip3 install --no-binary :all: --force-reinstall pillow && \
    pip3 install -r requirements.txt

# Sprawdzenie dostępności libjpeg w Pillow
RUN python3 -c "from PIL import Image; print('JPEG support:', 'jpeg' in Image.registered_extensions().values())"

# Komenda startowa
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio_web.wsgi:application"]
