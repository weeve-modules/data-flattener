import os
from logging import getLogger

log = getLogger("flattener")

__DELIMITER__ = os.getenv("DELIMITER")

def flattener(data, parent):
    log.debug(f'Parent: {parent}. Data: {data}')
    try:
        base = {}
        if type(data) == dict:
            for k, v in data.items():
                if type(v) == list:
                    for i, e in enumerate(v):
                        base = {**base, **flattener(e, (parent + __DELIMITER__ + k + __DELIMITER__ + str(i)) if parent else k + __DELIMITER__ + str(i))}
                elif type(v) == dict:
                    base = {**base, **flattener(v, (parent + __DELIMITER__ + k) if parent else k)}
                else:
                    newLabel = (parent + __DELIMITER__ + k) if parent else k
                    base[newLabel] = v
        else:
            for i, e in enumerate(data):
                base = {**base, **flattener(e, (parent + __DELIMITER__ + str(i)) if parent else str(i))}

        return base

    except Exception as e:
        return f"Exception when trying to flatten data: {data}. Exception: {e}"


