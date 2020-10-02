def fib(n):
  return "Incorrect input" if n <= 0 else (0 if n == 1 else(1 if n == 2 else fib(n - 1) + fib(n - 2)))
  
 if __name__ == '__main__':
  print(fib(int(input("Enter number : "))))
