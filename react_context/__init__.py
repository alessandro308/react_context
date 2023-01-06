from contextlib import contextmanager
import inspect
from collections import defaultdict

CURRENT_CONTEXT = {}
@contextmanager
def use_context(**kwargs):
    global CURRENT_CONTEXT
    caller_frame_id = id(inspect.stack()[2].frame)
    try:
        if not CURRENT_CONTEXT.get(caller_frame_id):
            CURRENT_CONTEXT[caller_frame_id] = defaultdict(lambda : [])
        for key, value in kwargs.items():
            CURRENT_CONTEXT[caller_frame_id][key].append(value)
        yield
    finally:
        for key, value in kwargs.items():
            CURRENT_CONTEXT[caller_frame_id][key].pop()


def get_context(key):
    global CURRENT_CONTEXT
    frames = inspect.stack()
    for frame in frames:
        frame_id = id(frame.frame)
        if CURRENT_CONTEXT.get(frame_id, {}).get(key):
            return CURRENT_CONTEXT[frame_id][key][-1]
    return None

def debug_context(key, logger=print):
    global CURRENT_CONTEXT
    frames = inspect.stack()[1:]
    count = 0
    if not get_context(key):
        logger(f"Context not found for key {key}")
        return
        
    for frame in frames:
        frame_id = id(frame.frame)
        if CURRENT_CONTEXT.get(frame_id, {}).get(key):
            logger(" "*count + f"{frame.filename} (line {frame.lineno}) - {frame.function} <- Found context value defined here" )
            return CURRENT_CONTEXT[frame_id][key][-1]
        else:
            logger(" "*count + f"{frame.filename} (line {frame.lineno}) - {frame.function}" )
        count+=1
    return None
