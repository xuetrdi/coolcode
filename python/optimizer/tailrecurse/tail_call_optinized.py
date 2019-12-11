import sys


class TailRecurseException(Exception):
  def __init__(self, args, kwargs):
    super().__init__()
    self.args = args
    self.kwargs = kwargs


def tail_call_optimized(g):
  def func(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
      raise TailRecurseException(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except TailRecurseException as e:
          args = e.args
          kwargs = e.kwargs
  func.__doc__ == g.__doc__
  return func

@tail_call_optimized
def factorial(n, acc=1):
  if n == 0:
    return acc
  return factorial(n - 1, n * acc)


print(factorial(10000))


@tail_call_optimized
def fib(i, current=0, next=1):
  if i == 0:
    return current
  else:
    return fib(i - 1, next, current + next)


print(fib(10000))
