# Pictureediting with Pillow

Small script for editing pictures (sharpness, contrast, rotate). To run the py-file, you need to install "Pillow". Just follow the OS-specific instructions below. "Image_Enhancer.py" uses a predefined folder structure! Open the file in pycharm to change the structure for your needs. If you don't want "Image_Enhancer.py" to rotate your pictures, simply erase ".rotate(-90)".

## Setup (WSL / Linux / macOS)

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python Image_Enhancer.py

Setup WINDOWS

py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
py Image_Enhancer.py
