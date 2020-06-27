#program to find intersection of elements from two lists
list1=[1,8,4]
list2=[3,1,4]
intersection_set=set.intersection(set(list1),set(list2))
intersection_list=list(intersection_set)
print(intersection_list)
