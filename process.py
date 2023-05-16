# Ctrl + Alt + L 自动格式化代码

import cfg
import os
from tools.log import logd
import shutil
from tools import utils


def do_debug(path):
    logd(path)


def do_list(path):
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
    utils.exe(cmd)
