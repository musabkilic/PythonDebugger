import sys
import inspect
import copy

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
                if type(cur) == list and type(prev) == list:
                    print(f"Line {line-1}: {repr(name)} of type {type(cur)}:")
                    C, P = len(cur), len(prev)
                    for i in range(max(C, P)):
                        a = cur[i] if i < C else None
                        b = prev[i] if i < P else None
                        if a != b:
                            print(f"* {name}[{repr(i)}] changed from {repr(b)} to {repr(a)}")
                elif type(cur) == dict and type(prev) == dict:
                    print(f"Line {line-1}: {repr(name)} of type {type(cur)}:")
                    K = set(cur.keys()) | set(prev.keys())
                    for k in K:
                        a = cur.get(k)
                        b = prev.get(k)
                        if a != b:
                            print(f"* {name}[{repr(k)}] changed from {repr(b)} to {repr(a)}")
                else:
                    print(f"Line {line-1}: {repr(name)} of type {type(cur)} changed from {repr(prev)} to {repr(cur)}")
        self.prevVar = copy.deepcopy(frame.f_locals)
