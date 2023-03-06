import cfg
import os
from tools.log import logd
from tools import file
import shutil
from tools.utils import exe


def do_filter(path):
    linesw = []
    ext_out = '.f.txt'
    ext_skip = [ext_out, '.docx', '.tgz']
    for skip in ext_skip:
        if path.endswith(skip):
            return
    lines = file.loadlines(path)
    for l in lines:
        for tag in cfg.FILTER_TXT:
            if l.find(tag) >= 0:
                break
        else:
            linesw.append(l)
    file.writelines(path + ext_out, linesw)
    logd('{} out: {}    [OK]'.format(path, len(linesw)))


def do_debug(path):
    logd(path)


def do_move(path):
    shutil.move(path, os.getcwd())


def do_unzip(path):
    for ext in cfg.ZIP_EXT:
        if path.endswith(ext):
            break
    else:
        return
    cmd = '"{}" x -y "{}"'.format(cfg.ZIP_PATH, path)
    logd(cmd)
    exe(cmd)


def do_list(path):
    logd(path)




