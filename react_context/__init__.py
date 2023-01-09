from contextlib import contextmanager
import inspect
from collections import defaultdict
import sys

CURRENT_CONTEXT = defaultdict(lambda: {})

@contextmanager
def create_context(**kwargs):
    global CURRENT_CONTEXT
    caller_frame_id = id(sys._getframe(2))
    try:
        if CURRENT_CONTEXT[caller_frame_id]:
            raise Exception('Cannot run use_context twice in the same function')
        CURRENT_CONTEXT[caller_frame_id] = kwargs
        yield
    finally:
        for key, value in kwargs.items():
            del CURRENT_CONTEXT[caller_frame_id]
      

def get_context(key, default=None):
    global CURRENT_CONTEXT
    frame = sys._getframe(0)
    while frame:
        frame_id = id(frame)
        if CURRENT_CONTEXT.get(frame_id, {}).get(key):
            return CURRENT_CONTEXT[frame_id][key]
        frame = frame.f_back
    return default


def debug_context(key, default=None, logger=print):
    global CURRENT_CONTEXT
    frames = inspect.stack()[1:]
    count = 0
    if not get_context(key):
        logger(f"Context not found for key {key}")
        return default
        
    for frame in frames:
        frame_id = id(frame.frame)
        if CURRENT_CONTEXT.get(frame_id, {}).get(key):
            logger(" "*count + f"{frame.filename} (line {frame.lineno}) - {frame.function} <- Found context value defined here" )
            return CURRENT_CONTEXT[frame_id][key]
        else:
            logger(" "*count + f"{frame.filename} (line {frame.lineno}) - {frame.function}" )
        count+=1
    return None
