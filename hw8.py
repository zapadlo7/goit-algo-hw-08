import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Створюємо мін-купу з довжин кабелів
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    # Поки в купі більше одного кабелю
    while len(cable_lengths) > 1:
        # Витягуємо дві найменші довжини
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        
        # Витрати на їх з'єднання
        cost = first + second
        total_cost += cost
        
        # Поміщаємо новий кабель назад у купу
        heapq.heappush(cable_lengths, cost)
    
    return total_cost

# Приклад використання
cable_lengths = [4, 6, 3, 8, 11]
print("Мінімальні загальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cable_lengths))
