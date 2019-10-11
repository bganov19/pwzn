def task_1(n=9):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end='')
        print('')

task_1()

# def task_1():
#     return '''
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
# '''

assert task_1() == '''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
