import os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def calc(dep_sum, percent, cap, dep_len, add, current_month):
    print('Start sum =', dep_sum, ' % =', percent, 'deposit len =', dep_len, 'add every mon =', add)
    for i in range(int(dep_len / cap)):
        dep_sum = dep_sum + (dep_sum / 100 * percent / 12 * cap) + add
        current_month = current_month + cap
        print('Iteration', i, '   Month', current_month, '   Sum', dep_sum)

print('Start sum - ', end='')
deposit_sum = float(input())
print('Annual percent ', end='')
percent = float(input())
print('Capitalization every month? ', end='')
capitalization = int(input())
print('Length of deposit in months ', end='')
deposit_lenght = int(input())
print('Add sum to deposit on every capitalization iteration ', end='')
add = float(input())

clear()
calc(deposit_sum, percent, capitalization, deposit_lenght, add, 0)
while True:
    menu = {}
    menu['1'] = "Start sum"
    menu['2'] = "Percent"
    menu['3'] = "Deposit length"
    menu['4'] = "Add every iter"
    menu['5'] = "Capitalization every month?"
    menu['0'] = "Exit"

    print('Change parameter')
    options = menu.keys()
    for entry in options:
        print(entry, menu[entry])
    selection = input("Please Select: ")
    if selection == '1':
        print('Start sum - ', end='')
        deposit_sum = float(input())
    elif selection == '2':
        print('% ', end='')
        percent = float(input())
    elif selection == '3':
        print('dep len? ', end='')
        deposit_lenght = int(input())
    elif selection == '4':
        print('Add every iter ')
        add = float(input())
    elif selection == '5':
        print('Capitalization every month? ', end='')
        capitalization = int(input())
    elif selection == '0':
        break
    else:
        print("Unknown Option Selected:", selection)

    clear()
    calc(deposit_sum, percent, capitalization, deposit_lenght, add, 0)
