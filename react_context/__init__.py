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
    stacks = inspect.stack()
    for stack in stacks:
        frame_id = id(stack.frame)
        if CURRENT_CONTEXT.get(frame_id, {}).get(key):
            return CURRENT_CONTEXT[frame_id][key][-1]
    return None