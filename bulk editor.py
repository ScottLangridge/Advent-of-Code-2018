import os


path = os.getcwd()
for f in os.listdir(path):
    if 'day' in f:
        path = path + '\\' + f
        for f in os.listdir(path):
            if 'day' in f:
                path = path + '\\' + f
                with open(path, 'r') as file:
                    lines = file.readlines()
                for line in lines:
                    if line[:10] == "print('---":
                        line = print("\n--------------------------\nFINISHED\nTIME:', end_time - start_time, '\n---------------------------")
                with open(path, 'w') as file:
                    file.writelines(lines)

