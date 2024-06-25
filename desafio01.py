def escadaria_direita(n):
    for i in range(1, n+1):
        number_of_blank_spaces = n-1
        n = number_of_blank_spaces
        print((' ' * number_of_blank_spaces) + ('#' * i))

escadaria_direita(20)
