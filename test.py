import PythonDebugger

db = PythonDebugger.Debugger()

@db.debug
def sample(a, b):
    x = a + b
    y = x * 2
    r = list(range(a, y))
    r[0] = 9
    y = x * y
    print('Sample: ' + str(y))

sample(2, 4)
