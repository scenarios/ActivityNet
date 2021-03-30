#!/bin/bash
python gpu_occupation.py &
for i in {11..20}
do
  python download.py \
  ./data/kinetics-700_train_split$i.csv \
  /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
  -n 1 -s 256 -t buffer_tmp \
  --download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-train_download-report_split$i.json &
done
wait