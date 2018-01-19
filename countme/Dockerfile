# Use a nice, small python image
FROM python:3-alpine

# Add our application
COPY . /app

# After this, command execute in this directory
WORKDIR /app

# Install the requirements
RUN pip install -r requirements.txt

# Run our application
CMD [ "python", "app.py"]