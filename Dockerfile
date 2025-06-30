FROM python:3.9

# download this https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx
# copy model to avoid unnecessary download
# COPY u2net.onnx /home/.u2net/u2net.onnx

WORKDIR /app

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5100

CMD ["python", "app.py"]


# Image build
# docker build -t image_name docker_file_path

#Run the container
# docker run -d -p 5100:5100 --name container_name image_name

