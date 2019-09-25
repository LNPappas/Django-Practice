def timeConversion(s):
    #
    # Write your code here.
    #
    answer = ''
    if s[-2] == 'A' and s[:2] != '12':
        answer = s[:-2]
    elif s[-2] == 'A' and s[:2] == '12':
        answer = '00' + s[2:-2]
    elif s[-2] == 'P' and s[:2] == '12':
        answer = s[:-2]
    else:
        num = int(s[:2]) + 12
        answer = str(num) + s[2:-2]
    return answer

if __name__ == "__main__":
    print(timeConversion('07:05:45PM'))
    print(timeConversion('07:05:45AM'))
    print(timeConversion('12:05:45PM'))
    print(timeConversion('12:05:45AM'))
