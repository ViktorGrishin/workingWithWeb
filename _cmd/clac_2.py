import sys
if len(sys.argv) == 1:
    print('NO PARAMS')
    sys.exit()
try:
    numbers = list(map(int, sys.argv[1:]))
    s = 0
    for i in range(len(numbers)):
        s += numbers[i] * (-1) ** i
    print(s)
except Exception as exc:
    print(type(exc).__name__)
