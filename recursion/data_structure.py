class Node:  # BST
    def __init__(self, value: int):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


root: Node = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)

root.right.left = Node(12)


def preorder(node: Node | None) -> None:
    if node is None:
        return
    
    print(node.value)
    preorder(node.left)
    preorder(node.right)


# preorder(root)


def inorder(node: Node | None):
    if node is None:
        return 
    
    inorder(node.left)
    print(node.value)
    inorder(node.right)


def postorder(node: Node | None):
    if node is None:
        return
    
    postorder(node.left)
    postorder(node.right)
    print(node.value)


# Depth first search
def search(node: Node | None, target: int) -> bool:
    if node is None:
        return False

    if node.value == target:
        return True

    return search(node.left, target) or search(node.right, target)


# print(search(root, 7))


# BST search
def bst_search(node: Node | None, target: int) -> bool:
    if node is None:
        return False

    if node.value == target:
        return True

    if target < node.value:
        return bst_search(node.left, target)

    return bst_search(node.right, target)



graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

def dfs(graph: dict[str, list[str]], node: str, visited: set[str]) -> None:
    if node in visited:
        return

    visited.add(node)

    # print(node)

    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)
        

visited = set()

dfs(graph, "A", visited)
# A, B, D, C


def dfs_search(
    graph: dict[str, list[str]],
    node: str,
    target: str,
    visited: set[str]
) -> bool:

    if node in visited:
        return False

    visited.add(node)

    if node == target:
        return True

    for neighbor in graph[node]:
        if dfs_search(graph, neighbor, target, visited):
            return True

    return False


# print(dfs_search(graph, "A", "D", visited))


def merge(left: list[int], right: list[int]) -> list[int]:
    result: list[int] = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)



def _merge(list_1: list[int], list_2: list[int]):
    result: list[int] = []
    
    i = 0
    j = 0
    
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1
    
    result.extend(list_1[i:])
    result.extend(list_2[j:])
    
    return result


# print(_merge([2, 3, 9, 23], [4, 6, 28]))


def partition_(list_1: list[int]):
    if not list_1:
        return 
    
    left_side = []
    right_side = []
    
    for item in range(1, len(list_1)):
        if list_1[item] > list_1[0]:
            right_side.append(list_1[item])
        else:
            left_side.append(list_1[item])
    
    return left_side , list_1[0], right_side


# print(partition_([3, 9, 1, 6, 7, 23, 12, 0, 3]))


def partition_first_direct(arr: list[int], low: int, high: int) -> int:
    pivot = arr[low]
    i = low + 1  # Boundary pointer for smaller elements

    # Scan every element from low + 1 up to and including high
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Place pivot at index i - 1 (the end of the smaller elements region)
    arr[low], arr[i - 1] = arr[i - 1], arr[low]

    return i - 1

def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            # print(arr[i], arr[j])
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    print(arr[i], arr[high])

    return i

arr = [7, 2, 1, 6, 8, 5, 3, 4]
pivot_index = partition(arr, 0, len(arr) - 1)

print("Partitioned array:", arr)
print("Final pivot index returned:", pivot_index)


def quick_sort(arr: list[int], low: int, high: int) -> None:
    if low >= high:
        return

    pivot_index = partition(arr, low, high)

    quick_sort(arr, low, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, high)


arr = [7, 2, 9, 4, 3, 8]

quick_sort(arr, 0, len(arr) - 1)

print(arr)