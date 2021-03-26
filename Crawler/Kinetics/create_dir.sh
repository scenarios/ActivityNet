#!/bin/bash

python download.py \
./data/kinetics-700_validation.csv \
/mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
-n 1 -s 256 -t buffer_tmp \
--download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-val_download-report_create_dir_only.json \
--create_dir_only True