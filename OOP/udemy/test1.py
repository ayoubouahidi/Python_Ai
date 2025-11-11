try:
    
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("problem of zero ")
finally:
    print("this line will print no mayyer what")