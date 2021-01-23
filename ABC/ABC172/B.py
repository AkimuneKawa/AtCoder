N = int(input())

ac, wa, tle, re = 0, 0, 0, 0
for i in range(N):
    judge = input()
    if judge == 'AC':
        ac += 1
    elif judge == 'WA':
        wa += 1
    elif judge == 'TLE':
        tle += 1
    elif judge == 'RE':
        re += 1

print('AC x {}'.format(ac))
print('WA x {}'.format(wa))
print('TLE x {}'.format(tle))
print('RE x {}'.format(re))