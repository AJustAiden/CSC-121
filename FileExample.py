with open("Numbers.txt", "r") as filename:
    content = filename.readlines()
    #print(content)
    new_list = []
    for i in content:
        var = i.rstrip("\n")
        var = var.split(",")
        new_list.append(var)

    for item in range(len(new_list)):
        new_list[item] = list(map(int,new_list[item]))
    #iterate through lists and sum up the values
    line = 1
    for item in new_list:
        print(f"line {line} values add up to {sum(item)}")
        line += 1
