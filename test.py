import PythonDebugger

db = PythonDebugger.Debugger()

@db.debug
def sample(a, b):
    x = a + b
    y = x * 2
    r = list(range(a, y))
    r[0] = 9
    r[:3], r[-3:] = r[-3:], r[:3]
    y = x * y
    d = {"alice" : 86, "bob": 79}
    d["alice"] += 8
    d["chloe"] = 98
    for i in range(x):
        j = i ** 2
    print('Sample: ' + str(y))

sample(2, 4)
