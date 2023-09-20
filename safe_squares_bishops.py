def safe_squares_bishops(n, bishops):
    #creating a value to difine empty squares count
    safe_squares = 0
    #two values for boshops movment probebilits
    diagonal1 = set()
    diagonal2 = set()
    #taking out bishps input values 
    for bishop in bishops:
        #define each value to a and b
        a, b = bishop
        #make changes in current positions of bishops according to posible squares to move
        diagonal1.add(a - b)
        diagonal2.add(a + b)
    #checking for empty squares
    for i in range(n):
        for j in range(n):
            if i - j not in diagonal1 and i + j not in diagonal2:
                safe_squares += 1
    
    return safe_squares

