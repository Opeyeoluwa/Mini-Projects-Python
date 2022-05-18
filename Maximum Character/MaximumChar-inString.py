def countchar(text):
    x = {}
    for i in set(text):
        x[i]= text.count(i)
    maxi = max(x, key=x.get)
    print(x)
    print(maxi)

countchar("Hellooa")