def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if details['cost'] <= budget:
            selected_items.append(item)
            budget -= details['cost']
            total_calories += details['calories']

    return selected_items, total_calories

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100
selected_items, total_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:", selected_items, "Калорії:", total_calories)


def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= items[item_names[i - 1]]["cost"]

    total_calories = dp[n][budget]
    return selected_items, total_calories

# Приклад використання
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("Динамічне програмування:", selected_items_dp, "Калорії:", total_calories_dp)
