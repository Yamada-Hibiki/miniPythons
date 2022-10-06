# aWESOME is cODING ==> Coding IS Awesome
text = "aWESOME is cODING"
print(text.split())


def reverse_swap(string):
    new_s = ""
    for i in string.split()[::-1]:
        new_s += i + " "
    
    swap = ""
    for char in new_s:
        if char.isupper():
            swap += char.lower()
        else:
            swap += char.upper()
    
    return swap


print(reverse_swap(text))
