#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x960 --no-banner ~/output/IMG_$DATE.png
