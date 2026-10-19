# You can remove 'pass' if you written code in the function
# Exercise 1

def save_scores(names, scores, filename):
    file = open(filename,"w")
    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
    file.close()
# Exercise 2
def average_score(filename):
    file = open(filename, "r")
    lst  = file.readlines()
    if not lst:
        return 0 
    else:
        s=0
        c=0
        for i in range(len(lst)):
            line = lst[i].strip()
            if line!="":
                a = lst[i].split(",")
                s += int(a[1])
                c+=1
        s = s/c
        file.close()
        return round(s,1)

# Exercise 3
def filter_passed(source, destination, pass_mark):
    src = open(source, "r")
    des = open(destination, "w")
    lst = src.readlines()
    x=0
    for i in range(len(lst)):
        a = lst[i].split(",")
        if int(a[1])>=pass_mark:
            des.write(f"{a[0]},{a[1]}")
            x += 1
    des.close()
    src.close()
    return x

# Exercise 4
def replace_word(filename, old_word, new_word):
    file = open(filename, "r")
    lst = file.readlines()
    file.close()
    file = open(filename, "w")
    x=0
    for i in range(len(lst)):
        x += lst[i].count(old_word)
        a = lst[i].replace(old_word,new_word)
        file.write(a)
    file.close()
    return x

# Exercise 5
def remove_line(filename, line_number):
    file = open(filename, "r")
    lst = file.readlines()
    file.close()
    if len(lst) < line_number or line_number<1:
        return False
    else:
        file = open(filename, "w")
        for i in range (len(lst)):
            if i+1==line_number:
                continue
            file.write(lst[i])
        file.close()
        return True
