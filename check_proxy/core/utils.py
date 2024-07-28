def partition(lst, n):
    return [lst[i::n] for i in range(n)]

def check_proxies(proxy_list, proxy_checker):
    for line in proxy_list:
        try:
            proxy_checker(line)
        except Exception as e:
            print(e)
            pass