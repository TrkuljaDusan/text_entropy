#import Math
def char_frequency(str):

    f = open("reclaimed_wood.txt", "r")
    text = f.read()
    count = 0
    dict = {}
    for c in text:
        if c.isupper(): 
            c = c.lower()

        count = count + 1
        keys = dict.keys()
        if c in keys:
            dict[c] += 1
        else:
            dict[c] = 1
    check = 100
    for c in dict:
        dict[c] = round(dict[c]/count * 100, 2)
        check = check - dict[c]
    print (check)
    return dict

print(char_frequency('google.com'))