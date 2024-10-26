#!/bin/bash

# Build the Docker image
sudo docker build -t gibert-triay-app .

# Update requirements.txt with the latest Poetry export without hashes
poetry export -f requirements.txt --output requirements.txt --without-hashes

echo "Docker image built and requirements.txt updated successfully!"
