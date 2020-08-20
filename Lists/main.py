if __name__ == '__main__':

    N = int(input())
    array = []
    for i in range(N):
        want = input().split()
        cmd = want[0]
        if want[0] != 'print':
            cmd +="("+ ",".join(want[1:]) +")"
            eval("array." + cmd)
        else:
            print(array)