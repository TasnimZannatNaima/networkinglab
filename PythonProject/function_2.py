def print_max(a, b):
 if a > b:
    print(a, 'is maximum')
 elif a == b:
    print(a, 'is equal to', b)
 else:
    print(b, 'is maximum')

 if __name__ == '__main__':
     pass
     print_max(3, 4)
     # directly pass literal values
     x = 5
     y = 7
     # pass variables as arguments
     print_max(x, y)

