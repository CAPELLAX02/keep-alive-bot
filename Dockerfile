# Use Python 3.9 based Docker image 
FROM python:3.9-slim

# Determine the working directory
WORKDIR /app

# Copy the required files to the image
COPY requirements.txt requirements.txt
COPY bot.py bot.py
COPY .env .env

# Download the required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Start the bot
CMD ["python", "bot.py"]
