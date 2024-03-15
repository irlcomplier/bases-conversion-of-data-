#A Python Program that has 2 algorithms; a denary to hex and a hex to denary converter
hexs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]  # Array of hexadecimal values
def DhexConversion(user_denValue, hexs):
    if user_denValue >= 16: #If denary inputted is above 16, whole algorithm will be used!
        First_Value = user_denValue // 16
        First_HexValue = hexs[First_Value]
        Second_Value = user_denValue % 16
        Second_HexValue = hexs[int(Second_Value)]
        Complete_HexValue = First_HexValue + Second_HexValue
        print(Complete_HexValue)
    else:
        Complete_HexValue = hexs[user_denValue]
        print(Complete_HexValue)


repeat = int(input("how many times do you want to enter a denary value"))
for x in range(repeat):
    user_denValue = int(input("Please enter a denary value"))
    DhexConversion(user_denValue, hexs)

def hextodecimal(user_hex, hexs):
    resOfMultiple = 0
    initial_counter = len(user_hex) - 1
    for p in range(len(user_hex)):
        print(user_hex[p] + str(" 16^") + str(initial_counter))
        if user_hex[p] > hexs[9]:
            first_val = user_hex[p]
            resOfMultiple += hexs.index(first_val) * 16**int(initial_counter)
        else:
            resOfMultiple += float(user_hex[p]) * (16**initial_counter)
        initial_counter -= 1

    if initial_counter < 0:
        decimalVal = resOfMultiple
        return decimalVal

rep2 = int(input("how many times do you want to want to use the hex to decimal convertor"))
for i in range(rep2):
    user_hex = input("enter your hexadecimal value")
    decimalVal = hextodecimal(user_hex, hexs)
print(decimalVal)
