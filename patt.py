def lsum (l):
    lens = [len(i) for i in l if i]
    return(sum(lens))

def p (p, count):
    items = [""]
    depth = 0
    for char in p:
        if depth != 0:
            if char == "]":depth -= 1
            elif char == "[":depth += 1
            items[-1] += char
        elif depth == 0:
            if char == "[":
                depth += 1
                items[-1] += char
            elif char == "(":items.append("*")
            elif char == ")":items.append("")
            else:items[-1] += char

    items = [i for i in items if i]
                
    #items = [i for i in p.replace(" ", "").replace("("," *").replace(")", " ").split(" ") if i]
    rep = [(j[1:] if j != " " else None) for j in [(i if i[0] == "*" else " ") for i in items]]
    non = [(i if i[0] != "*" else None) for i in items]

    string = [(i if i else "") for i in non]
    out = ""

    if all(i is None for i in rep) and len(string) < count:
        return([string[0], None])
    elif count < 0:
        for i in string:out += i
        if rep[0] != None:return("", rep[0])
        elif len(items) > 1:return(out, rep[1])
        else:return(out, None)
    elif count <= lsum(non):
        for i in string:out += i
        return(out[0:count], None)
    else:
        remaining = count - lsum(non)
        while remaining > 0:
            for index, i in enumerate(rep):
                if i == None:continue
                if remaining == 0:break
                elif remaining <= len(i):
                    string[index] += i[:remaining]
                    remaining = 0
                else:
                    string[index] += i
                    remaining -= len(i)

        for i in string:
            out += i
        return(out, None)
