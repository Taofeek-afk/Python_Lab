# nums = [x for x in random.randrange()]
# print(random.randint(0, 1)) # includes 1. must collect 2 args, randrange(start(optional), stop(not included), steps())

stmt = "Remember Red Hope is a good thing and no good thing ever dies"
# c_list = stmt.lower().split()
# print(c_list)
# print(c_list.count("red"))

from collections import Counter, namedtuple

stmt = stmt.lower().split()
res = Counter(stmt)

# print(res)
# print(res.most_common())
# print(res.most_common(3))

position = namedtuple("position", ("first", "second"))
p = position(1, 2)

p_2 = position(second=8, first=4)

# print(dir(dict))
# print(dir(tuple))

unordered_items = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 0:"0", "apple": ("green_apple", "red_apple"), "color": ("yellow", "green", "red", "purple"), frozenset({}):7, 98: "98", "122":122}

# for key, value in unordered_items.items():
#     # print(f"{key} : {value}")
# print(help(items))
# print("Ordered items: ", ordered_items)
# print("Unordered items: ", unordered_items)
