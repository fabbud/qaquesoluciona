def beautifulDays (i, j, k):
    beautifuldays = 0
    for day in range(i, j+1):
        reversed_day = int(str(day)[::-1])
        diff = day - reversed_day
        if diff % k == 0:
            beautifuldays += 1
    print(beautifuldays)
    return beautifuldays

beautifulDays(20, 23, 6)
beautifulDays(13, 45, 3)
beautifulDays(1, 2000000, 2000000)
beautifulDays(1, 2000000, 23047885)
