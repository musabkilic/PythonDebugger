import sys
import inspect
import copy
import time
import os
import importlib.util
import json


class Debugger:
    def __init__(self, debugging_file=None):
        self.DEBUGGING = {}
        self.prevVar = {}
        self.history = {}
        self.lineHistory = {}
        self.debugging_started = time.time()
        self.last_exec = time.time() * 10**6
        self.debugging_file = debugging_file
        self.outputs = []
        sys.settrace(self.trace_calls)

    def debug(self, func):
        self.DEBUGGING[func.__name__] = {}
        def debug_wrapper(*args):
            self.DEBUGGING[func.__name__]["started"] = time.time() * 10**6
            self.last_exec = time.time() * 10**6
            func(*args)
        return debug_wrapper

    def printHistory(self):
        total_time = time.time()*10**6 - self.DEBUGGING[list(self.history.values())[-1][0][2].co_name]["started"]
        for k in self.history:
            H = self.history[k]
            t = type(H[-1][0])
            actual_print(f"\nVariable {repr(k)} of type {t}, initiliazed at function {repr(H[0][2].co_name)} at line {H[0][1]}:")
            if t in [int, float]:
                #print(H, H[0][0])
                m, M = min(H, key=lambda x: x[0])[0], max(H, key=lambda x: x[0])[0]
                actual_print(f"* Variable was in range: {m}-{M}")
            else:
                actual_print(f"* Variable was in this list of values: {list(set([repr(x[0]) for x in H]))}")
            actual_print(f"Initial value: {H[0][0]}; Final value: {H[-1][0]}")
            for v, l, f in H:
                actual_print(f"={repr(v)} after line {l}; `" + inspect.getsource(H[0][2]).split("\n")[l-H[0][2].co_firstlineno].strip()+"`")
        for l, lH in sorted(self.lineHistory.items(), key=lambda x:x[0]):
            actual_print(f"Line {'{:03d}'.format(l)}: `" + inspect.getsource(H[0][2]).split('\n')[l-H[0][2].co_firstlineno], end="`")
            actual_print(f"; Executed {len(lH)} times; Time spent avg:{sum(lH)/len(lH)}μs total:{sum(lH)}μs")
        actual_print(f"Total execution time: {total_time}μs")

    def trace_calls(self, frame, event, arg):
        if frame.f_back and frame.f_back.f_code.co_filename == self.debugging_file:
            if len(self.DEBUGGING) == 0:
                self.DEBUGGING[frame.f_code.co_name] = {}
                self.DEBUGGING[frame.f_code.co_name]["started"] = time.time() * 10**6
                self.last_exec = time.time() * 10**6
        if frame.f_code.co_name in self.DEBUGGING:
            if not "started" in self.DEBUGGING[frame.f_code.co_name]:
                self.DEBUGGING[frame.f_code.co_name]["started"] = time.time() * 10**6
            return self.trace_lines
        return

    def trace_lines(self, frame, event, arg):
        line = frame.f_lineno
        frame.f_code.co_argcount
        #print(line-1, event)
        self.lineHistory[line] = self.lineHistory.get(line, []) + [(time.time()*10**6-self.last_exec)*10]
        lH = self.lineHistory[line]
        for name in frame.f_code.co_varnames:
            cur = frame.f_locals.get(name, None)
            prev = self.prevVar.get(name, None)
            if cur != prev:
                self.history[name] = self.history.get(name, []) + [(copy.deepcopy(cur), line-1, frame.f_code)]
                if type(cur) == list and type(prev) == list:
                    actual_print(f"Line {line-1}[Executed {len(lH)} times; Time spent avg:{sum(lH)/len(lH)}μs total:{sum(lH)}μs]: {repr(name)} of type {type(cur)}:")
                    C, P = len(cur), len(prev)
                    for i in range(max(C, P)):
                        a = cur[i] if i < C else None
                        b = prev[i] if i < P else None
                        if a != b:
                            actual_print(f"* {name}[{repr(i)}] changed from {repr(b)} to {repr(a)}")
                elif type(cur) == dict and type(prev) == dict:
                    actual_print(f"Line {line-1}[Executed {len(lH)} times; Time spent avg:{sum(lH)/len(lH)}μs total:{sum(lH)}μs]: {repr(name)} of type {type(cur)}:")
                    K = set(cur.keys()) | set(prev.keys())
                    for k in K:
                        a = cur.get(k)
                        b = prev.get(k)
                        if a != b:
                            actual_print(f"* {name}[{repr(k)}] changed from {repr(b)} to {repr(a)}")
                else:
                    actual_print(f"Line {line-1}[Executed {len(lH)} times; Time spent avg:{sum(lH)/len(lH)}μs total:{sum(lH)}μs]: {repr(name)} of type {type(cur)} changed from {repr(prev)} to {repr(cur)}")
        self.prevVar = copy.deepcopy(frame.f_locals)
        self.outputs.append({"variables":copy.deepcopy(self.prevVar), "step":len(self.outputs)+1, "timestamp":time.time()-self.debugging_started})
        self.last_exec = time.time() * 10**6
        if event == "return":
            self.printHistory()


class Reporter:
    def __init__(self, steps):
        self.steps = steps

    def printSteps(self):
        for step in self.steps:
            if "variables" in step:
                for n, v in step["variables"].items():
                    exec(f"{n}={v}")
            else:
                print("T:"+str(step["timestamp"])+"|", eval(step["print"]))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        p = sys.argv[1]
        if p.endswith(".py"):
            db = Debugger(p)
            if len(sys.argv) > 2:
                db.DEBUGGING[sys.argv[2]] = {}
            else:
                spec = importlib.util.spec_from_file_location("debugging", p)
                debugging = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(debugging)
                if (hasattr(debugging, 'main') and inspect.isfunction(debugging.main)):
                    db.DEBUGGING["main"] = {}

            actual_print = print
            def print(x, end="\n"):
                frame = inspect.currentframe()
                frame = inspect.getouterframes(frame)[1]
                if frame.frame.f_code.co_name in db.DEBUGGING:
                    string = inspect.getframeinfo(frame[0]).code_context[0].strip()
                    args = string[string.find('(') + 1:-1].split(',')

                    names = []
                    for i in args:
                        if i.find('=') != -1:
                            names.append(i.split('=')[1].strip())

                        else:
                            names.append(i)

                    db.outputs.append({"print":"".join(names), "timestamp":time.time()-db.debugging_started})
                    actual_print(x, end=end)

            with open(p) as f:
                code = compile(f.read(), p, 'exec')
                exec(code)

            with open(p+".json", "w") as f:
                json.dump(db.outputs, f)

        elif p.endswith(".json"):
            with open(p) as f:
                rp = Reporter(json.load(f))
            rp.printSteps()
