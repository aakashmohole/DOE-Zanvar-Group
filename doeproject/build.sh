#!/bin/bash
set -e  # Exit on error

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Collect static files (critical for Whitenoise)
python manage.py collectstatic --noinput

echo "ALLOWED_HOSTS: $ALLOWED_HOSTS"
echo "PORT: $PORT"