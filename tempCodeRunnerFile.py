
import math
import os
import random
import re
import sys

#
# Complete the 'whoIsTheWinner' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def copyCheck(arr):
  for i in range(len(arr)):
    if arr[i] in arr[i+1:]:
      arr.remove(arr[i])
      return True
  return False

def whoIsTheWinner(arr):
  count = 0
  while copyCheck(arr):
    count = count + 1
    
  if count % 2 == 0:
    return "First"
  else: return "Second"
  
    
    # WRITE DOWN YOUR CODE HERE

if __name__ == '__main__':
    

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = whoIsTheWinner(arr)

        

    
