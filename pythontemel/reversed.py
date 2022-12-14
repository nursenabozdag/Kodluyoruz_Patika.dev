def reverse(lists):
    lists.reverse()
    for i in lists:
        if isinstance(i,list):
            i.reverse()

result = [[1, 2], [3, 4], [5, 6, 7]]

reverse(result)

print(result)
