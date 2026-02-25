def multi():
    for i in range(2, 10):
        for j in range(1, 10):
            # print('{0} * {1} = {2}'.format(i, j, i * j))
            print(f'{i} * {j} = {i * j:2d}')
            
if __name__ == '__main__':
    multi()
