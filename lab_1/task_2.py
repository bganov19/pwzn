def task_2(n):
    for i in range(n+1):
        for j in range(i):
            print('*', end='')
        print('')
    for i in range(n+1, 0, -1):
        for j in range(i):
            print('*', end='')
        print('')


task_2(5)

# assert task_2() == '''
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# '''