import sys
import inspect

class Debugger:
    def __init__(self):
        self.DEBUGGING = []
        self.prevVar = {}
        sys.settrace(self.trace_calls)

    def debug(self, func):
        self.DEBUGGING.append(func.__name__)
        def debug_wrapper(*args):
            func(*args)
        return debug_wrapper

    def trace_calls(self, frame, event, arg):
        if frame.f_code.co_name in self.DEBUGGING:
            return self.trace_lines
        return

    def trace_lines(self, frame, event, arg):
        line = frame.f_lineno
        frame.f_code.co_argcount
        for name in frame.f_code.co_varnames:
            cur = frame.f_locals.get(name, None)
            prev = self.prevVar.get(name, None)
            if cur != prev:
                print(f"Line {line}: {repr(name)} changed from {repr(prev)} to {repr(cur)}")
        self.prevVar = dict(frame.f_locals)
