from time import sleep
print('Os Fogos de artificio vão estourar em:')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[41mKabum\033[m')
