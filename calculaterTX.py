n = [3, 5, 7]
def double_list(x):
    for i in range(0, len(n)):
        n[i] = n[i] * 2
        print n[i]
    return x
# Don't forget to return your new list!

print double_list(n)