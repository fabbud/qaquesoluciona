def timeInWords (hour, minutes):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
    if minutes == 0:
        return numbers[hour] + " o' clock"
    elif minutes == 15:
        return "quarter past " + numbers[hour]
    elif minutes == 30:
        return "half past " + numbers[hour]
    elif minutes == 45:
        return "quarter to " + numbers[hour + 1]
    elif minutes < 30:
        if minutes == 1:
            return numbers[minutes] + " minute past " + numbers[hour]
        else:
            return numbers[minutes] + " minutes past " + numbers[hour]
    elif minutes > 30:
        if minutes == 59:
            return numbers[60 - minutes] + " minute to " + numbers[hour + 1]
        else:
            return numbers[60 - minutes] + " minutes to " + numbers[hour + 1]
    
print(timeInWords(5, 0)) # five o' clock
print(timeInWords(5, 1)) # one minute past five
print(timeInWords(5, 10)) # ten minutes past five
print(timeInWords(5, 15)) # quarter past five
print(timeInWords(5, 28)) # twenty eight minutes past five
print(timeInWords(5, 30)) # half past five
print(timeInWords(5, 40)) # twenty minutes to six
print(timeInWords(5, 45)) # quarter to six
print(timeInWords(5, 47)) # thirteen minutes to six
print(timeInWords(10, 59)) # one minute to eleven
