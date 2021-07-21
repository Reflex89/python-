numbers = ['1','2','3','4','5','6','7','8','9']
for number in numbers:
    if number == '1':
        end = 'st'
    elif number == '2':
        end = 'nd'
    else:
        end = 'th'
    print(f"{number}{end}")