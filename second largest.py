def second_largest(lst):
    if len(lst)<2:
        return None
    first,second=lst[0],lst[1]
    for i in lst[2:]:
        if i>first:
            first,second=i,first
        elif i>second:
            second=i
    return second
print(second_largest([11,2,32,1,5,6]))  