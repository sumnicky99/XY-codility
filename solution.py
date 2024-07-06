def solution(S):
    n = len(S)
    
    if n < 2:
        return 0
    
    left_x = left_y = 0
    right_x = S.count('x')
    right_y = S.count('y')
    
    valid_splits = 0
    
    for i in range(n - 1):
        if S[i] == 'x':
            left_x += 1
            right_x -= 1
        elif S[i] == 'y':
            left_y += 1
            right_y -= 1
        
        if left_x == left_y or right_x == right_y:
            valid_splits += 1
    
    return valid_splits