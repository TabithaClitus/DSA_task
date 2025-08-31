n=int(input())
str_n=str(n)
rev_n=int(str_n[::-1])
if (n==rev_n):
  print('Palindrome')
else:
  print('Not a palindrome')