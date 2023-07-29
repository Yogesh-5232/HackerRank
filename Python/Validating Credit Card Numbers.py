def isValid(x):
    if len(x) not in [16,19]:
        return False
    if len(x)==19:
        if x[4]!='-' or x[9]!='-' or x[14]!='-':
            return False
    if x[0] not in ['4','5','6']:
        return False
    if '-' in x:
        x=''.join(x.split('-'))
    if any(ord(x[i]) not in range(ord('0'),ord('9')+1) for i in range(16)):
        return False
    if any(str(i)*4 in x for i in range(10)):
        return False
    return True
for _ in range(int(input())):
    x=input()
    if isValid(x):
        print("Valid")
    else:
        print("Invalid")
