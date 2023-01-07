"""Написать декоратор skip, которым можно декорировать функции.

Если переданное выражение condition истинное, функция не должна выполнятся, а должна вывестись строка reason.

Если выражение condition ложное, функция должна выполнится.


def skip(condition, reason=''):
    pass

Пример использования:

@skip(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
    assert 2 + 2 == 5

test_two_plus_two()  # Skipped because of JIRA-123 bug

"""
def skip(condition = True, reason = ''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(reason)
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

@skip(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
    assert 2 + 2 == 5

test_two_plus_two()