#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

# Verify port is accessible (debugging)
echo "Checking port 10000..."
nc -zv 0.0.0.0 10000 || echo "Port check failed"