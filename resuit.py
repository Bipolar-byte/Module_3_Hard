def calculate_structure_sum(data):
    number_count = 0
    string_count = 0

    def count_items(item):
        nonlocal number_count, string_count
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(key, (int, float)):
                    number_count += 1
                elif isinstance(key, str):
                    string_count += 1
                count_items(value)
        elif isinstance(item, (list, tuple, set)):
            for sub_item in item:
                count_items(sub_item)
        elif isinstance(item, (int, float)):
            number_count += 1
        elif isinstance(item, str):
            string_count += 1

    for elem in data:
        count_items(elem)

    return number_count, string_count


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

