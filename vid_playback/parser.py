def res_input(str):
    str = str.split('x')
    
    try: 
        str = [int(s) for s in str]
    except ValueError: 
        print('Cannot convert string to int')
        
    if len(str) != 2:
        raise ValueError('Need two numbers')
        
    return tuple(str)