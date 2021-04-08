import csv
from collections import defaultdict

import os
import argparse

_EXTENTION = '.mp4'

def _reorgKinetics(kinetics_list_path, kinetics_ava_list_path):

    def _creat_label_map():

        lbmap = {}
        with open(_LABEL_MAP_PATH, 'r') as label_file:
            reader = csv.reader(label_file)
            for i, row in enumerate(reader):
                if i == 0: continue
                lbmap[row[1]] = row[0]

        return lbmap

    def _is_valid(vid_path):
        return os.popen('ffmpeg -v error -i  "%s" -f null - 2>&1' % os.path.join(_ROOT_PATH, vid_path)).read()

    def _get_fps(vid_path):
        try:
            fps = eval(os.popen('ffprobe -v 0 -of csv=p=0 -select_streams v:0 -show_entries stream=r_frame_rate "%s" >&1' \
                             % os.path.join(_ROOT_PATH, vid_path)).read().split('\n')[0])
        except Exception:
            fps = None

        return fps

    def _is_belong_to(l, h):
        return lambda x: x[0] >= l and x[0] <=h

    lbMap = _creat_label_map()
    # create kinetics ava list lookup table for reference
    ka_dict = defaultdict(list)
    with open(kinetics_ava_list_path, 'r') as ka_file:
        reader = csv.reader(ka_file)
        for row in reader:
            if len(row) == 7:
                row[1] = round(float(row[1]))
                ka_dict[row[0]].append(row[1:] + [None])

    # reorgnize Kinetics video list based on ava annotation and file completeness
    reorged = []
    _get_relPath = lambda a, b: os.path.join(a, b)
    total_len = len(open(kinetics_list_path, 'r').readlines())
    with open(kinetics_list_path, 'r') as k_file:
        reader = csv.reader(k_file)
        for i, row in enumerate(reader):
            if i == 0: continue

            vid = row[1]
            video_class = lbMap[row[0]]
            time_start, time_end = row[2:4]
            vname = '%s_%s_%s' % (vid,
                                 "%06d" % int(time_start),
                                 "%06d" % int(time_end))
            vid_path = _get_relPath(row[0], vname) + _EXTENTION
            _msg = _is_valid(vid_path)
            if _msg:
                with open('./log.txt', 'a') as log_f:
                    log_f.write("%s : %s \n\r" % (vid_path, _msg))
                continue
            fps = _get_fps(vid_path)
            if not fps:
                continue
            fps = round(fps)

            action_annos = list(filter(_is_belong_to(int(time_start), int(time_end)), ka_dict[vid]))
            if action_annos:
                for anno in action_annos:
                    base = [vname]
                    anno.extend([video_class, time_start, time_end, fps, vid_path])
                    base.extend(anno)
                    reorged.append(base)
            else:
                none_anno = [None] * 7
                base = [vname]
                none_anno.extend([video_class, time_start, time_end, fps, vid_path])
                base.extend(none_anno)
                reorged.append(base)

            with open('./process.txt', 'w') as log_f:
                log_f.write("%dth/%d video clip: process completed" % (i, total_len))

    return reorged


def reorgKinetics(kinetics_list_path, kinetics_ava_list_path, output_path):

    kntReorg = _reorgKinetics(kinetics_list_path, kinetics_ava_list_path)
    with open(output_path, 'w') as csv_f:
        headline = ['video_id', 'time_stamp', 'top', 'left', 'bottom', 'right', 'action_class', 'person_id', 'video_class','clip_time_start', 'clip_time_end', 'fps', 'relative_path']
        writer = csv.DictWriter(csv_f, fieldnames=headline)
        writer.writerow(dict(map(lambda k, v: (k, v), headline, headline)))
        for line in kntReorg:
            writer.writerow(dict(map(lambda k, v: (k, v), headline, line)))


def reorgAVA(ava_list_path, output_path):
    pass


if __name__ == '__main__':
    description = 'Helper script for downloading and trimming kinetics videos.'
    p = argparse.ArgumentParser(description=description)
    p.add_argument('--kinetics_list_path', type=str, default=None,
                   help=('CSV file containing the kinetics list'))
    p.add_argument('--kinetics_ava_list_path', type=str, default=None,
                   help=('CSV file containing the kinetics ava list'))
    p.add_argument('--kinetics_reorg_dir', type=str, default=None,
                   help='Output directory where reorgnized kinetics list will be saved.')
    p.add_argument('--ava_list_path', type=str, default=None,
                   help=('CSV file containing the ava list'))
    p.add_argument('--ava_reorg_dir', type=str, default=None,
                   help='Output directory where reorgnized ava list will be saved.')
    p.add_argument('--kinetics_label_map', type=str, default=None,
                   help='label map dir for kinetics dataset')
    p.add_argument('--root_path', type=str, default=None,
                   help=('Data root path'))

    args = p.parse_args()

    global _LABEL_MAP_PATH
    global _ROOT_PATH

    _ROOT_PATH = args.root_path
    '''
    # for debug
    _ROOT_PATH = '/Users/yizhouzhou/Documents/workspace/projects/spatiotemporal_event_detection/data_acquisition/data_preparation/debug/'
    args.kinetics_list_path = '/Users/yizhouzhou/Documents/workspace/projects/spatiotemporal_event_detection/data_acquisition/data_preparation/debug/validate.csv'
    args.kinetics_ava_list_path = '/Users/yizhouzhou/Documents/workspace/projects/spatiotemporal_event_detection/data_acquisition/data_preparation/debug/kinetics_val_v1.0.csv'
    args.kinetics_reorg_dir = '/Users/yizhouzhou/Documents/workspace/projects/spatiotemporal_event_detection/data_acquisition/data_preparation/debug/kinetics_reorg_debug.csv'
    args.kinetics_label_map = '/Users/yizhouzhou/Documents/workspace/projects/spatiotemporal_event_detection/data_acquisition/data_preparation/debug/kinetics_700_labels.csv'
    '''

    if args.kinetics_list_path:
        _LABEL_MAP_PATH = args.kinetics_label_map
        reorgKinetics(args.kinetics_list_path, args.kinetics_ava_list_path, args.kinetics_reorg_dir)

    if args.ava_list_path:
        reorgAVA(args.ava_list_path, args.ava_reorg_dir)
