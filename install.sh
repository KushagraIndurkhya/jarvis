#!/bin/sh
apt-get update  # To get the latest package lists
apt-get install portaudio19-dev
apt-get install python3-pyaudio
apt-get install espealk
apt install libespeak1
pip3 install -r requirements.txt
python3 jarvis.py