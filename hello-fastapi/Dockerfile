# How to run this image:
# - First build an imagem from this specification file : docker build -t hello-world:fastapi .
# - The spawn a container from the image created       : docker run  -p 80:80 hello-world:fastapi
# - Go to the browser on http://localhost:80
# - Open another terminal and list the containers running

# Map the volumes:
# - Add your name to the request response on main.py
# - Reload the page, nothing happened
# - Restart the container, and it changed!
# - Stop the container and run with this command       : docker run  -p 80:80 -v $(pwd):/app hello-world:fastapi

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]