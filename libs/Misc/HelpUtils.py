def printHelp():
    print("Usage: check_proxy.py <proxy-list> <output-list> <number-of-threads>")

def partition (lst, n ):
    return [ lst[i::n] for i in range(n) ]
