#!/bin/bash
set -e  # Exit on error

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Collect static files (critical for Whitenoise)
python manage.py collectstatic --noinput

# Verify PORT is available (debugging)
echo "--> Checking if port $PORT is available..."
python -c "import socket; s = socket.socket(); s.bind(('', $PORT))" || echo "Port check failed"