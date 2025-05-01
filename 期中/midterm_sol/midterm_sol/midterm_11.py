def test(func):
    import time
    def wrapper():
        print('start')
        start = time.time()
        func()
        end = time.time()
        print('end')
        print(end - start, 'seconds')
    return wrapper

@test
def func_test():
    for i in range(10000):
        print(i)


func_test()    