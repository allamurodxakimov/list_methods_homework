def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    x=fruits.count("apple")
    a=0
    ls=[]
    while a<len(fruits):
        if fruits[a]=="apple":
            ls.append(a)
        a+=1
    ls.insert(0,x)
    return ls
print(main(fruits = ["apple", "banana", "apple", "pear", "apple"]))