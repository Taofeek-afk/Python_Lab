# cols_n_rows = [[2, 4, 6], 9, [1, 3, 5], [10, 20, 30]]

# def matrix_row_sums(arr):
#     # Inner helper function to track the index recursively
#     def helper(sub_arr, index):
#         if not sub_arr:
#             return
        
#         current = sub_arr[0]
#         if isinstance(current, list):
#             total = sum(current)
#             print(f"Row {index + 1}; total: {total}")
        
#         helper(sub_arr[1:], index + 1)

#     # Kick off the recursion starting at index 0
#     helper(arr, 0)

# matrix_row_sums(cols_n_rows)

