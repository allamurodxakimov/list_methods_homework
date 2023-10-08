def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    ls=[]
    k=list1.count(1)
    l=list1.count(0)
    ls.append(k)
    ls.append(l)
    return ls
print(main(list1 = [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1]))
