def Rail(p, k):
    c = ""
    num = (2 * k - 2)
    r = [[] for i in range(num/2+1)]

    for i in range(len(p)):
        for h in range(0, (num / 2)+1):
            if i % num == h or i % num == num - h:
                r[h].append(p[i])
                break

    print(r)

    #return c


pt = raw_input("Enter text")
key = input("Enter key")
ct = ""
ct = Rail(pt, key)
print ct
