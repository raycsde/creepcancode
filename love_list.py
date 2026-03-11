love_list = ['computer', 'tv', 'cs', 'book', 'moive', 'house', 'work', 'city', 'chill']
print(f'There are {len(love_list)} things in my love list.')
#错误写法：print(love_list.sorted())
#不存在.sorted() sorted()是内置功能，不是list函数。
#.sort()永久排序字母顺序 sorted()临时排序字母顺序
print(sorted(love_list))
print(love_list)
love_list.sort()
print(love_list)
love_list.sort(reverse=True)
print(love_list)
love_list.reverse()
print(love_list)
love_list.reverse()
print(love_list)

