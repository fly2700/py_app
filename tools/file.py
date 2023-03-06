from tools.log import logd


def loadlines(path, encoding='utf-8'):
    try:
        with  open(path, 'r', encoding=encoding) as f:
            lines = f.readlines()
            return lines
    except Exception as e:
        logd(path, e)
        return []


def writelines(path, lines, encoding='utf-8'):
    try:
        with open(path, 'w', encoding=encoding) as fw:
            fw.writelines(lines)
    except Exception as e:
        logd(path, e)
