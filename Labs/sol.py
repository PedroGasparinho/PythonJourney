def is_even(n: int) -> bool:
  return n % 2 == 0

def test_even_odd():
  assert is_even(0)
  assert not is_even(1)
  assert is_even(2)
  assert not is_even(3)
  assert is_even(100)
  assert not is_even(101)
  print("test_even_odd ok")

test_even_odd()

def grade_calculator(n: float) -> str:
  if n < 0 or 100 < n:
    return "Invalid grade"

  n = round(n)

  if n < 60:
    return "F"
  elif n < 70:
    return "D"
  elif n < 80:
    return "C"
  elif n < 90:
    return "B"
  else:
    return "A"

def test_grade_calculator():
  assert grade_calculator(-1) == "Invalid grade"
  assert grade_calculator(101) == "Invalid grade"
  assert grade_calculator(40) == "F"
  assert grade_calculator(59.2) == "F"
  assert grade_calculator(59.8) == "D"
  assert grade_calculator(71) == "C"
  assert grade_calculator(81) == "B"
  assert grade_calculator(91) == "A"
  assert grade_calculator(100) == "A"
  print("test_grade_calculator ok")

test_grade_calculator()

def somatorio(l: list[float]) -> float:
  res = 0
  for i in l:
    res += i
  return res

def test_somatorio():
  assert somatorio([]) == 0
  assert somatorio([0]) == 0
  assert somatorio([1]) == 1
  assert somatorio([0,1,2]) == 3
  assert somatorio([2,1,0]) == 3
  assert somatorio([3,3,3]) == 9
  assert somatorio([2, 6.2, 9.1, 30, 10]) == 57.3
  print("test_somatorio ok")

test_somatorio()

def count_vowels(s: str) -> int:
  res = 0
  for c in s:
    c = c.lower()
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
      res += 1
  return res

def test_count_vowels():
  assert count_vowels("") == 0
  assert count_vowels("my") == 0
  assert count_vowels("aeiou") == 5
  assert count_vowels("Hi, John!") == 2
  assert count_vowels("Almonds") == 2
  print("test_count_vowels ok")

test_count_vowels()

def tabuada(n: int) -> None:
  for i in range(1, 11):
    print(str(n) + " * " + str(i) + " = " + str(n*i))

#tabuada(1)
#tabuada(5)

def is_palindrome(s: str) -> bool:
  size = len(s)
  if size == 0:
    return True

  for i in range(size//2 + 1):
    if s[i] != s[size - i - 1]:
      return False
  return True

def test_is_palindrome():
  assert is_palindrome("")
  assert is_palindrome("aa")
  assert not is_palindrome("ab")
  assert is_palindrome("aba")
  assert not is_palindrome("abb")
  assert is_palindrome("stop pots")
  print("test_is_palindrome ok")

test_is_palindrome()

def fib_for(n: int) -> int:
  a = 0
  b = 1
  sum = a+b
  
  for _ in range(n):
    a = b
    b = sum
    sum = a+b

  return a

"""def print_help():
  print("Available operations.")
  print("-1. Quit")
  print("0. Help")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Modulo")"""

"""def calculator():
  print_help()

  is_on = True
  while is_on:
    op = input("Select operation: ")
    if op == "-1":
      is_on = False
    elif op == "0":
      print_help()
    elif op in ("1", "2", "3", "4", "5"):
      arg1 = input("Enter 1st number: ")
      arg2 = input("Enter 2nd number: ")
      if op == "1":
        print(str(arg1) + "+" + str(arg2) + "=" + str(arg1+arg2))
      elif op == "2":
        print(str(arg1) + "-" + str(arg2) + "=" + str(arg1-arg2))
      elif op == "3":
        print(str(arg1) + "*" + str(arg2) + "=" + str(arg1*arg2))
      elif op == "4":
        print(str(arg1) + "/" + str(arg2) + "=" + str(arg1/arg2))
      elif op == "5":
        print(str(arg1) + "%" + str(arg2) + "=" + str(arg1%arg2))
    else:
      print("Invalid operation")

calculator()"""

def maximum(l: list[float]) -> float:
  res = float('-inf')
  for e in l:
    if e > res:
      res = e
  return res

def test_maximum():
  assert maximum([]) == float('-inf')
  assert maximum([0]) == 0
  assert maximum([1]) == 1
  assert maximum([1, 2]) == 2
  assert maximum([2, 1]) == 2
  assert maximum([1, 7, 10, 4, 6, 12, 9]) == 12
  print("test_maximum ok")

test_maximum()

def minimum(l: list[float]) -> float:
  res = float('inf')
  for e in l:
    if e < res:
      res = e
  return res

def test_minimum():
  assert minimum([]) == float('inf')
  assert minimum([0]) == 0
  assert minimum([1]) == 1
  assert minimum([1, 2]) == 1
  assert minimum([2, 1]) == 1
  assert minimum([1, 7, -10, 4, 6, 12, 9]) == -10
  print("test_minimum ok")

test_minimum()

def second_maximum(l: list[float]) -> float:
  if len(l) < 2:
    return float('-inf')
  
  max = l[0]
  res = float('-inf')
  for e in l:
    if e > max:
      res = max
      max = e
    elif max > e and e > res:
      res = e
  return res

def test_second_maximum():
  assert second_maximum([]) == float('-inf')
  assert second_maximum([0]) == float('-inf')
  assert second_maximum([1, 2]) == 1
  assert second_maximum([2, 1]) == 1
  assert second_maximum([1, 7, 10, 4, 6, 12, 9]) == 10
  print("test_second_maximum ok")

test_second_maximum()

def second_minimum(l: list[float]) -> float:
  if len(l) < 2:
    return float('inf')
  
  min = l[0]
  res = float('inf')
  for e in l:
    if e < min:
      res = min
      min = e
    elif min < e and e < res:
      res = e
  return res

def test_second_minimum():
  assert second_minimum([]) == float('inf')
  assert second_minimum([0]) == float('inf')
  assert second_minimum([1, 2]) == 2
  assert second_minimum([2, 1]) == 2
  assert second_minimum([1, 7, 10, 4, 6, 12, 9]) == 4
  print("test_second_minimum ok")

test_second_minimum()

def is_prime(n: int) -> bool:
  if n <= 1:
    return False
  
  for i in range(2, n):
    if n % i == 0:
      return False
    
  return True

def test_is_prime():
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(97)
  print("test_is_prime ok")

test_is_prime()

def invert_list(l: list) -> list:
  res = []
  size = len(l)
  for i in range(size):
    res.append(l[size-i-1])
  return res

def test_invert_list():
  assert invert_list([]) == []
  assert invert_list([1]) == [1]
  assert invert_list([1, 1]) == [1, 1]
  assert invert_list([1, 2]) == [2,1]
  assert invert_list([1,2,3]) == [3,2,1]
  assert invert_list([1, 6, 8, 9, 2, 3, 5, 7]) == [7, 5, 3, 2, 9, 8, 6, 1]
  print("test_invert_list ok")

test_invert_list()

def remove_dups(l: list) -> list:
  res = []
  for e in l:
    if not e in res:
      res.append(e)
  return res

def test_remove_dups():
  assert remove_dups([]) == []
  assert remove_dups([1]) == [1]
  assert remove_dups([1, 1]) == [1]
  assert remove_dups([2, 2, 2]) == [2]
  assert remove_dups([1, 2, 3]) == [1, 2, 3]
  assert remove_dups([1, 3, 2, 3, 4, 1, 2, 5, 5, 2, 1, 3]) == [1, 3, 2, 4, 5]
  print("test_remove_dups ok")

test_remove_dups()

def sum_digits(n: int):
  digits = str(n)
  sum = 0
  for d in digits:
    sum = sum + int(d)
  return sum

def test_sum_digits():
  assert sum_digits(0) == 0
  assert sum_digits(1) == 1
  assert sum_digits(11) == 2
  assert sum_digits(123) == 6
  assert sum_digits(1234) == 10
  assert sum_digits(96) == 15
  assert sum_digits(100) == 1
  assert sum_digits(2718) == 18
  print("test_sum_digits ok")

test_sum_digits()

def digital_root(n: int):
  res = n
  while res >= 10:
    res = sum_digits(res)
  return res

def test_digital_root():
  assert digital_root(0) == 0
  assert digital_root(1) == 1
  assert digital_root(11) == 2
  assert digital_root(123) == 6
  assert digital_root(1234) == 1
  assert digital_root(96) == 6
  assert digital_root(100) == 1
  assert digital_root(2718) == 9
  print("test_digital_root ok")

test_digital_root()

def count_char(c: str, s: str) -> int:
  if len(c) != 1:
    return -1
  
  res = 0
  for e in s:
    if e == c:
      res += 1
  return res

def test_count_char():
  assert count_char("c", "count count count") == 3
  assert count_char("s", "count count count") == 0
  assert count_char("c", "") == 0
  assert count_char("as", "as usual") == -1
  assert count_char("", "count count count") == -1
  print("count_char ok")

test_count_char()

def factorial(n: int) -> int:
  if n < 0:
    return -1

  res = 1
  for e in range(1, n+1):
    res = res * e
  return res

def test_factorial():
  assert factorial(0) == 1
  assert factorial(1) == 1
  assert factorial(2) == 2
  assert factorial(3) == 6
  assert factorial(4) == 24
  assert factorial(5) == 120
  assert factorial(10) == 3628800
  print("test_factorial ok")

test_factorial()

def count_words(s: str) -> int:
  if len(s) == 0:
    return 0

  words = s.split(" ")
  return len(words)

def test_count_words():
  assert count_words("Hello, world!") == 2
  assert count_words("Hello, how are you doing today?") == 6
  assert count_words("") == 0
  assert count_words("Goodbye") == 1
  print("test_count_words ok")

test_count_words()

def sum_even(l: list[int]) -> int:
  res = 0
  for e in l:
    if e % 2 == 0:
      res += e
  return res

def test_sum_even():
  assert sum_even([]) == 0
  assert sum_even([1]) == 0
  assert sum_even([1,3,5]) == 0
  assert sum_even([2]) == 2
  assert sum_even([2,4,6]) == 12
  assert sum_even([1,2,3,4]) == 6
  assert sum_even([5,7,9,6,8,10]) == 24
  print("test_sum_even ok")

test_sum_even()

"""def count_v_c(s: str) -> int:
  res = (0, 0)
  for c in s:
    c = c.lower()
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
      res = (res[0]+1, res[1])
    else:
      res = (res[0], res[1]+1)
  return res

def test_count_v_c():
  assert count_v_c("")

print(count_v_c("Hello"))"""

def count_eq_in_pos(l1, l2: list) -> int:
  size = min(len(l1), len(l2))

  res = 0
  for i in range(size):
    if l1[i] == l2[i]:
      res += 1

  return res


def test_count_eq_in_pos():
  assert count_eq_in_pos([], []) == 0
  assert count_eq_in_pos([2], [2]) == 1
  assert count_eq_in_pos([5], [9]) == 0
  assert count_eq_in_pos([2, 5], [2]) == 1
  assert count_eq_in_pos([1,2,3], [3,2,1]) == 1
  assert count_eq_in_pos([1,2,3], [1,2,3]) == 3
  print("test_count_eq_in_pos ok")

test_count_eq_in_pos()

def remove_elem(l: list[int], n: int) -> list[int]:
  res = []
  for e in l:
    if e != n:
      res.append(e)
  return res

def test_remove_elem():
  assert remove_elem([1,2,3], 1) == [2,3]
  assert remove_elem([], 1) == []
  assert remove_elem([1,2,3], 4) == [1,2,3]
  assert remove_elem([2], 2) == []
  assert remove_elem([1,0,1,0,1,0,1], 0) == [1,1,1,1]
  print("test_remove_elem ok")

test_remove_elem()

def is_sorted(l: list[int]) -> bool:
  for i in range(len(l) - 1):
    if l[i] > l[i+1]:
      return False
  return True

def test_is_sorted():
  assert is_sorted([])
  assert is_sorted([1])
  assert not is_sorted([2,1])
  assert is_sorted([1, 3, 5])
  assert not is_sorted([2, 6, 4, 8])
  assert not is_sorted([2, 2, 3, 2])
  assert is_sorted([1, 1, 1, 1])
  assert is_sorted([-1, -1, 0, 0, 1, 1])
  print("test_is_sorted ok")

test_is_sorted()

def bin_search(l:list[int], n: int) -> bool:
  assert is_sorted(l)

  lower = 0
  upper = len(l) - 1

  while lower <= upper:
    mid = lower + (upper - lower)//2
    if l[mid] == n:
      return True
    elif l[mid] > n:
      upper = mid - 1
    else:
      lower = mid + 1
  
  return False

def test_bin_search():
  assert bin_search([1,2,3], 2)
  assert not bin_search([1,2,3], 4)
  assert not bin_search([0,1,2,3,4,5,6,7,8,9], 10)
  assert bin_search([0,1,2,3,4,5,6,7,8,9], 0)
  print("test_bin_search ok")

test_bin_search()

def is_n_n(mtx: list[list[float]]) -> bool:
  line_num = len(mtx)
  for i in range(line_num):
    if len(mtx[i]) != line_num:
      return False
  return True

def test_is_n_n():
  assert is_n_n([])
  assert is_n_n([[1]])
  assert is_n_n([[1,2], [3,4]])
  assert not is_n_n([[1,2]])
  assert not is_n_n([[1,2], [3]])
  print("test_is_n_n ok")

test_is_n_n()

def matrix_sum(mtx1, mtx2: list[list[float]]) -> list[list[float]]:
  assert is_n_n(mtx1)
  assert is_n_n(mtx2)
  assert len(mtx1) == len(mtx2)

  res = []
  n = len(mtx1)
  for i in range(n):
    line = []
    for j in range(n):
      line.append(mtx1[i][j] + mtx2[i][j])
    res.append(line)

  return res

def test_matrix_sum():
  assert matrix_sum([[15]], [[15]]) == [[30]]
  assert matrix_sum([[1,1], [1,1]], [[2,2], [2,2]]) == [[3,3], [3,3]]
  assert matrix_sum([[1,2], [3,4]], [[5,6], [7,8]]) == [[6,8], [10,12]]
  assert matrix_sum([[1,1], [1,1]], [[0,0], [0,0]]) != [[3,3], [3,3]]
  print("test_matrix_sum ok")

test_matrix_sum()

def is_matrix(mtx: list[list[float]]) -> bool:
  line_num = len(mtx)
  col_num = len(mtx[0])
  for i in range(1, line_num):
    if col_num != len(mtx[i]):
      return False
  return True

def transpose(mtx: list[list[float]]) -> list[list[float]]:
  assert is_matrix(mtx)
  
  num_line = len(mtx)
  num_col = len(mtx[0])

  res = []
  for j in range(num_col):
    line = []
    for i in range(num_line):
      line.append(mtx[i][j])
    res.append(line)

  return res

def test_transpose():
  assert transpose([[1,2], [2,1]]) == [[1,2], [2,1]]
  assert transpose([[1,2], [3,4]]) == [[1,3], [2,4]]
  assert transpose([[1,2], [3,4], [5,6]]) == [[1, 3, 5], [2, 4, 6]]
  print("test_transpose ok")

test_transpose()

def merge_sorted(l1, l2: list[float]) -> list[float]:
  assert is_sorted(l1) and is_sorted(l2)
  size1 = len(l1)
  size2 = len(l2)
  i1 = 0
  i2 = 0
  res = []
  while i1 < size1 or i2 < size2:
    if i1 >= size1 or (i2 < size2 and l1[i1] >= l2[i2]):
      res.append(l2[i2])
      i2 += 1
    elif i2 >= size2 or (i1 < size1 and l1[i1] < l2[i2]):
      res.append(l1[i1])
      i1 += 1
  return res

def test_merge_sorted():
  assert merge_sorted([1], [2]) == [1,2]
  assert merge_sorted([1,3], [2]) == [1,2,3]
  assert merge_sorted([1,2,3], [2,4]) == [1,2,2,3,4]
  assert merge_sorted([0,2,4,5,6,7,10,12,13], [1,3,8,9,11]) == [0,1,2,3,4,5,6,7,8,9,10,11,12,13] 
  print("test_merge_sorted ok")

test_merge_sorted()

def interactive_avg():
  is_on = True
  sum = 0
  count = 0
  while is_on:
    val = input("Write a number: ")
    if val == "end":
      is_on = False
    else:
      try:
        sum += float(val)
        count += 1
        print("Average: ", str(sum/count))
      except ValueError:
        print("Not a number!")

#interactive_avg()

def bank_help():
  print("Available operations:")
  print("1. Get Balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Help")
  print("5. Quit")

def deposit(currBalance):
  amount = None
  while amount == None:
    try:
      amount = float(input("Deposit amount: "))
      if amount <= 0:
        print("Not a positive amount! Operation Cancelled")
        return currBalance
      else:
        return currBalance + amount
    except:
      print("Not a number!")

def withdraw(currBalance):
  amount = None
  while amount == None:
    try:
      amount = float(input("Withdraw amount: "))
      if amount <= 0:
        print("Not a positive amount! Operation Cancelled")
        return currBalance
      elif amount > currBalance:
        print("Insufficient amount! Operation Cancelled")
        return currBalance
      else:
        return currBalance - amount
    except:
      print("Not a number!")

def bank_account():
  is_on = True
  balance = 0
  bank_help()
  while is_on:
    op = input("Choose an operation: ")
    if op == "1":
      print("Balance = " + str(balance))
    elif op == "2":
      balance = deposit(balance)
    elif op == "3":
      balance = withdraw(balance)
    elif op == "4":
      bank_help()
    elif op == "5":
      is_on = False
    else:
      print("Unknown operation!")

#bank_account()