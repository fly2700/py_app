import os


def exe(cmd):
    p = os.popen(cmd)
    return p.read()
