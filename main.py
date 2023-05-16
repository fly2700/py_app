"""
作用：遍历目录下每个文件，按照指定参数，执行对应的函数。
"""

import sys
import cfg
import os
from tools.log import logd
import process

EACH_DO = {
    '-d': {'func': process.do_debug, },
    '-l': {'func': process.do_list, 'recur': False},
    '-m': {'func': process.do_move, 'path': cfg.DOWNLOAD_PATH},
    '-u': {'func': process.do_unzip},
}


def eachfile_do(recur=False, path='.', **kwargs):
    for f in os.listdir(path):
        path_sub = os.path.join(path, f)
        if recur and os.path.isdir(path_sub):
            eachfile_do(recur, path_sub, **kwargs)
        if os.path.isfile(path_sub):
            kwargs['func'](path_sub)


def main():
    args = sys.argv
    is_done = False
    for arg in args:
        if arg in EACH_DO.keys():
            logd('--------------------------------------------------------------------')
            eachfile_do(**EACH_DO[arg])
            is_done = True
    if is_done:
        logd('done')
    else:
        logd('unknown arg', args)



if __name__ == '__main__':
    main()
