import textwrap

def merge_the_tools(string, k):
    # your code goes here
    listString = textwrap.wrap(string, k)

    t = ""
    for i in range(0, len(listString)):
        for j in listString[i]:
            if j in t:
                pass
            else:
                t = t + j
        print(t)
        t = ""

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)