#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install yt-dlp

echo "Creating requirements.txt..."
pip freeze > requirements.txt

echo "Setup complete!"
echo "To activate the virtual environment in the future, run: source venv/bin/activate"