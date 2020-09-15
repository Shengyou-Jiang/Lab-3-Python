# Author: Shengyou Jiang sjj5492@psu.edu
# Collaborator: Kyle Domico kdd5262@psu.edu
# Collaborator: Teya Davis tmd5681@psu.edu
# Collaborator: Travis Stauffer tcs5399@psu.edu
# Section: 1
# Breakout: 2

def print_n(s,n):
  if n == 0:
    return 
  else:
    print(s)
    print_n(s, n-1)
    
def sum_n(n):
  if n <= 1:
    return n
  else:
    return n + sum_n(n-1)

def run():
  num1 = int(input("Enter an int: "))
  print(f"sum is {sum_n(num1)}.")
  s = input("Enter a string: ")
  print_n(s, num1)


if __name__ == "__main__"
run ()