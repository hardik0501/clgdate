#!/usr/bin/env bash
# Build script for Render.com deployment

echo "🚀 Starting build process for Poornimax..."

# Upgrade pip
pip install --upgrade pip

# Install system dependencies for Pillow
apt-get update
apt-get install -y \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    libwebp-dev \
    libtiff5-dev \
    libopenjp2-7-dev \
    liblcms2-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libxcb1-dev

# Install Python packages
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate --noinput

echo "✅ Build completed successfully!"
