from inspect import currentframe, getframeinfo
import time


def logd(msg1, msg2=''):
    _log('D', msg1, msg2)


def logw(msg1, msg2=''):
    _log('W', msg1, msg2)


def loge(msg1, msg2=''):
    _log('E', msg1, msg2)


def _log(level, msg1, msg2=''):
    if msg2 != '':
        msg2 = ": '{}'".format(msg2)
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    f = getframeinfo(currentframe().f_back)
    filename = f.filename.split('\\')[-1]
    stack = '{}:{} {}()'.format(filename, f.lineno, f.function)
    msg = '[{} {} {}] {}{}'.format(now, stack, level, msg1, msg2)
    print(msg)

