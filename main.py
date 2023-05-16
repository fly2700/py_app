import sys
import cfg
import os
from tools.log import logd
import process

EACH_DO = {
    '-d': {'func': process.do_debug, },
    '-l': {'func': process.do_list, 'recur': True},
    '-m': {'func': process.do_move, 'path': cfg.DOWNLOAD_PATH},
    '-u': {'func': process.do_unzip},
}


def eachfile_do(recur=False, path='.', **kwargs):
    for f in os.listdir(path):
        path_sub = os.path.join(path, f)
        if recur and os.path.isdir(path_sub):
            kw_copy = kwargs.copy()
            kw_copy['path'] = path_sub
            eachfile_do(recur, **kw_copy)
        if os.path.isfile(path_sub):
            kwargs['func'](path_sub)


def main():
    args = sys.argv
    for arg in args:
        if arg in EACH_DO.keys():
            eachfile_do(**EACH_DO[arg])
            break
    else:
        logd('unknown arg', args)
    logd('done')


if __name__ == '__main__':
    main()
