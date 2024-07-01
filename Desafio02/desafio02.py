def countingValleys (string):
    altitude = 0
    valleys = 0

    for i in string:
        if altitude == 0 and i == 'D':
            valleys += 1
            altitude -= 1
            print('altitude: ', altitude)

        elif i == 'U':
            altitude += 1
            print('altitude: ', altitude)

        else:
            altitude -= 1
            print('altitude: ', altitude)

    print('Number of valleys: ', valleys)
    return valleys

countingValleys('DDUUDDUDUUUD')

countingValleys('UDUUUDUDDD')

countingValleys('DUDUDUDUDUDUDU')

countingValleys('DDUUUUDDDUUUDDDU')