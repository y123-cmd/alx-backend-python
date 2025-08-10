# 1. Create a base Image

FROM python:3.10

# 2. Specify the working directory inside the Docker container.

WORKDIR /app

# 3. Copy project requirements file for shop-kipa project to workdir

COPY requirements.txt /app/

# 4. Run the required commands to update and install project dependencies

RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy all project files from host to workdir

COPY . /app/

# 6. Expose the port that the container will listen on for incoming connections.

EXPOSE 8000

# 7. Create command to run the application

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Build the container then run it:

# 1 Build (within messaging_app dir): docker build -t messaging_app_image .  

# 2 Run: docker run -d -p 8000:8000 --name messaging_app_container messaging_app_image
