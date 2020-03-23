for n in range(2, 10, 3):
    for m in range(1, 10):
        for k in range(n, n + 3):
            if k == 10:
                break
            print(f'{k} * {m} = {k * m}', end='\t')
        print('\t')
    print('\n')
