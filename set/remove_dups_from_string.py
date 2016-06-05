def remove_dups(string):
    seen = set()
    result = list()

    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return result

string = "Khamaj by Shafqat amanat ali"
#print (" ".join(remove_dups(string)))