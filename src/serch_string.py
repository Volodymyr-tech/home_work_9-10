import re
from collections import Counter


def filter_by_description(data: list, pattern: str) -> list:
    result = []
    for item in data:
        # Проверяем поле 'description' на вхождение слова по регулярному выражению
        if re.search(pattern, item['description'], re.IGNORECASE):  # re.IGNORECASE для игнорирования регистра
            result.append(item)
    return result



def count_operations_by_category(data_list: list, categories: list) -> dict:

    category_count = Counter() #{category: 0 for category in categories}

    for operation in data_list:
        description = operation.get('description','')

        for category in categories:
            if re.search(category, description, re.IGNORECASE):
                category_count[category] += 1

    return dict(category_count)


