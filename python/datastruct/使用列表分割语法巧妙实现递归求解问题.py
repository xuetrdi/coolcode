def to_sum(items):
  head, *tail = items
  return head + to_sum(tail) if tail else head
"""
[1, 10, 7, 4, 5, 9]
head : 1
tail : 10, 7, 4, 5, 9 作为items传入sum
---------------------
head : 10
tail : 7, 4, 5, 9     作为items传入sum
---------------------
head : 7
tail : 4, 5, 9        作为items传入sum
---------------------
head : 4
tail : 5, 9           作为items传入sum
---------------------
head : 5
tail : 9              作为items传入sum
---------------------
head : 9
tail : None           作为items传入sum
---------------------
=============================
9 + sum([])
5 + sum([9])
4 + sum([5, 9])
7 + sum([4, 5, 9])
10 + sum([7, 4, 5, 9])
1 + sum([10, 7, 4, 5, 9])
"""

def to_mul(items):
  head, *tail = items
  return head * to_mul(tail) if tail else head

if __name__ == '__main__':
  test_list = [1, 10, 7, 4, 5, 9]
  print("Test of List:", test_list)
  print("The Sum of  :", to_sum(test_list))
  print("The Mul of  :", to_mul(test_list))
