def create_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('X ' * n)
        else:
            print('X ', ' ' * (n - 2), ' X')

create_square(5)