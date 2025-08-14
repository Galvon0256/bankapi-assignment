#!/bin/bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# (Optional) Import initial data
# python manage.py import_banks