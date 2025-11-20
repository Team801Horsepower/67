import math

current_height = 0
for i in range(1, 100):
    height = int(math.tan(math.radians(i)) * 0.1)
    if height > 10:
        height = 10
    height = abs(height)
    slope = height - current_height
    current_height = height
    match slope:
        case 0:
            pass
        case 1:
            print(" O" * (height // 2), end = "")
            if height % 2 == 1:
                print(" \\")
        case -1:
            if height % 2 == 1:
                print(" /")
        case 2:
            print(" O" * (height // 2), end = "")
            if height % 2 == 1:
                print(" \\")
            print("O " * (height // 2))
        case -2:
            print(" O" * (height // 2), end = "")
            if height % 2 == 1:
                print(" /")
        case _:
            if(slope > 0):
                for i in range(slope):
                    if i % 3 == 0 and current_height > 4:
                        print (" __ " * (height // 4), end = "")
                        if height % 4 > 0:
                            print(" " * ((height % 4) - 1) + "\\")
                        else:
                            print("\\")
                    elif i % 3 == 1 and current_height > 5:
                        print("/  \\" * (height // 4), end = "")
                        if height % 4 > 0:
                            print(" " * ((height % 4) - 1) + "\\")
                        else:
                            print("\\")
                    elif i % 3 == 2 and current_height > 6:
                        print("\\__/" * (height // 4), end = "")
                        if height % 4 > 0:
                            print(" " * ((height % 4) - 1) + "\\")
                        else:
                            print("\\")
                    height += 1
            else:
                slope = abs(slope)
                for i in range(slope):
                    height -= 1
                    if i % 3 == 0 and current_height > 4:
                        print (" __ " * (height // 4), end = "")
                        if height % 4 > 0:
                            print(" " * ((height % 4) - 1) + "/")
                        else:
                            print("/")
                    elif i % 3 == 1 and current_height > 5:
                        print("/  \\" * (height // 4), end = "")
                        if height % 4 > 0:
                            print(" " * ((height % 4) - 1) + "/")
                        else:
                            print("/")
                    elif i % 3 == 2 and current_height > 6:
                        print("\\__/" * (height // 4), end = "")
                        if height % 4 > 0:
                            print(" " * ((height % 4) - 1) + "/")
                        else:
                            print("/")
    
    print (" " * height + "|")