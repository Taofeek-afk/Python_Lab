values = [14, 7, 22, 9, 7, 31, 7, 5]


def list_analyser(vals: list[int] = values, target: int= 7) -> str:
    indexes = []
    
    for i, n in enumerate(values):
        if n == target:
            indexes.append(i)
    
    if indexes:
        return f"Found at indices: {indexes} | Count: {len(indexes)} | First: {indexes[0]} | Last: {indexes[-1]}"

    return "Target not found"


print(list_analyser())


# targets = [7, 22, 18]

# for n in targets:
#     print(f"Target {n}.", list_analyser(target=n))