def median(list_of_numbers):
    list_of_numbers.sort()
    if len(list_of_numbers) % 2 == 0:
        center = len(list_of_numbers) // 2
        num_before = center - 1
        return (list_of_numbers[num_before] + list_of_numbers[center]) / 2
    else:
        return list_of_numbers[len(list_of_numbers) // 2]

def activityNotifications(expenditure, d):
    notifications = 0
    trailing_days = []

    for i in range(len(expenditure)):
        if i >= d:
            current_median = median(trailing_days)
            if expenditure[i] >= 2 * current_median:
                notifications += 1
            trailing_days.pop(0)  # Remove the oldest expenditure
        trailing_days.append(expenditure[i])  # Add the current day's expenditure

    return notifications

print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)) # 2
print(activityNotifications([1, 2, 3, 4, 4], 4)) # 0
print(activityNotifications([10, 20, 30, 40, 50, 60, 70, 80, 90], 5)) # 1
print(activityNotifications([1, 2, 100, 2, 2, 2, 2, 2], 4)) # 0