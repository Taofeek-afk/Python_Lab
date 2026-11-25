matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30], [10, 20, 30]]

# Row 1 total: 12 | Row 1 average: 4.0
# Row 2 total: 9 | Row 2 average: 3.0
# Row 3 total: 60 | Row 3 average: 20.0
# Column 1 total: 13
# Column 2 total: 27
# Column 3 total: 41

def matrix_sum(nested_list: list[list[int]] = matrix) -> None:
    columns = [0 for _ in range(len(nested_list[0])+1)]

    for i, row in enumerate(nested_list, 1):
        total = 0
    
        for n, col in enumerate(row, 1):
            columns[n] += col
            total += col
        
        print(f"Row {i} total: {total} | Row {i} average: {total/len(row):.1f}")
    
    print()
    for i, n in enumerate(columns[1:], 1):
        print(f"Column {i} total {n}")


matrix_sum()
