#!/bin/bash
python gpu_occupation.py &
python download.py \
./data/kinetics-700_validation_split1.csv \
/mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
-n 1 -s 256 -t buffer_tmp \
--download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-val_download-report_split1.json &
python download.py \
./data/kinetics-700_validation_split2.csv \
/mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
-n 1 -s 256 -t buffer_tmp \
--download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-val_download-report_split2.json &
python download.py \
./data/kinetics-700_validation_split3.csv \
/mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
-n 1 -s 256 -t buffer_tmp \
--download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-val_download-report_split3.json &
python download.py \
./data/kinetics-700_validation_split4.csv \
/mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
-n 1 -s 256 -t buffer_tmp \
--download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-val_download-report_split4.json &
python download.py \
./data/kinetics-700_validation_split5.csv \
/mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
-n 1 -s 256 -t buffer_tmp \
--download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-val_download-report_split5.json &
python download.py \
./data/kinetics-700_validation_split6.csv \
/mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
-n 1 -s 256 -t buffer_tmp \
--download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-val_download-report_split6.json &
python download.py \
./data/kinetics-700_validation_split7.csv \
/mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
-n 1 -s 256 -t buffer_tmp \
--download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-val_download-report_split7.json &
python download.py \
./data/kinetics-700_validation_split8.csv \
/mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
-n 1 -s 256 -t buffer_tmp \
--download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-val_download-report_split8.json &
python download.py \
./data/kinetics-700_validation_split9.csv \
/mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
-n 1 -s 256 -t buffer_tmp \
--download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-val_download-report_split9.json &
python download.py \
./data/kinetics-700_validation_split10.csv \
/mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics-700-2020 \
-n 1 -s 256 -t buffer_tmp \
--download-report /mnt/wfs/mmcommwfssz/project_mm-base-vision/harryizzhou/projects/video_understanding/data/kinetics700-2020-val_download-report_split10.json