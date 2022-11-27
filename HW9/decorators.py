

def call_times(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            wrapper.count += 1
            with open(filename, 'a') as f:
                f.write(f'{func.__name__} была вызвана {wrapper.count} разa\n')
            return result
        wrapper.count = 0
        return wrapper
    return decorator


@call_times('foo.txt')
def foo():
    pass

@call_times('foo.txt')
def boo():
    pass

@call_times('calls.txt')
def doo():
    pass

foo()
boo()
foo()
foo()
boo()
doo()