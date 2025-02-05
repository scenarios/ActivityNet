#!/bin/bash
python gpu_occupation.py &
for i in {1..10}
do
  python download.py \
  ./data/kinetics-700_validation_split$i.csv \
  /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
  -n 1 -s 256 -t buffer_tmp \
  --download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-val_download-report_split$i.json &
done
wait