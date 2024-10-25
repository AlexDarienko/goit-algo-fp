import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_trials):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        results[total] += 1

    probabilities = {key: value / num_trials * 100 for key, value in results.items()}
    return probabilities

# Симуляція
num_trials = 100000
probabilities = monte_carlo_simulation(num_trials)

# Виведення результатів
print("Імовірності сум за методом Монте-Карло:", probabilities)

# Графік
plt.bar(probabilities.keys(), probabilities.values(), color='blue')
plt.xlabel('Сума')
plt.ylabel('Імовірність (%)')
plt.title('Імовірності сум при киданні двох кубиків')
plt.show()
