# Creating a function for return lyrics of pineapple pen
def apple_pen(first_ingredient, second_ingredient):
    des = ['I have a pen, I have a apple\nUh! Apple-Pen!']
    des.append('I have a pen, I have a pineapple\nUh! Pineapple-Pen!')
    des.append('I have a pen, I have a pen\nUh! Long pen!')
    dic = [['pen', 'apple'], ['pen', 'pineapple'], ['pen', 'pen']]
    inp = [first_ingredient, second_ingredient]
    for i in range(3):
        if dic[i] == inp:
            return des[i]
    raise ValueError('It is not in the lyrics')
