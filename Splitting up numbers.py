def num_split(num):
    values = []
    text = str(abs(num))
    index = len(text)-1
    sign = 1
    
    if num < 0:
        sign = -1
    
    for a in text:
        values.append(int(a)*10**index*sign)
        index -=1
    return values