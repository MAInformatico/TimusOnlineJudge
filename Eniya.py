import sys;

def calc():
    param = sys.stdin.readline()
    args = param.split(' ')
    N = int(args[0])
    A = int(args[1])
    B = int(args[2])
    result = N * A * B * 2
    print (result)

if __name__ == '__main__':
    calc()
