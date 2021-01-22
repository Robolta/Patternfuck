from patt import *

f = open(input("File Name: ") + ".pf")
#f = open("truth machine.pf")
program = "".join([i for i in f.read() if i in "+-<>[]().,?!@"])
debug = {
    "type":False,
    "memory":False,
    "step":False,
    "finalDump":True,
    "pattern":False,
    "character":False,
    "pointer":False,
    "space":False,
    "newline":True,
    "maxSteps":100000}

memory = [0] # Tape Memory
pointer = 0 # Memory pointer

active = False # True if a pattern is active
pattern = "" # Holds the pattern
depth = 0 # Depth of square brackets
repeat = [False, None]
steps = 0

running = True # True while running
while running:    
    if program == "":
        if repeat[0]:program = repeat[1]
        else:
            running = False
            continue
    
    char, program = program[0], program[1:] # Moving the first character to char
    if debug["character"]:print("Char:", char)
    
    if active: # If the pattern is active
        if char == "]":
            depth -= 1
            if depth == 0:
                if debug["type"]:print("Pattern End")
                active = False
                if debug["pattern"]:print("Pattern In:", pattern, "|", memory[pointer])
                pattern = p(pattern, memory[pointer])
                if debug["pattern"]:print("Pattern Out:", pattern[0], "|", pattern[1])
                if pattern[1] == None:program = pattern[0] + program
                else:
                    repeat = [True, pattern[1]]
                    program = pattern[0] + pattern[1]
                pattern = ""
                
            else:
                if debug["type"]:print("Pattern Active")
                pattern += char
        elif char == "[":
            if debug["type"]:print("Pattern Active")
            depth += 1
            pattern += char
        else:
            if debug["type"]:print("Pattern Active")
            pattern += char

    elif char == "[":
        if debug["type"]:print("Pattern Start")
        depth += 1
        active = True
        
    elif char == "<":
        if debug["type"]:print("Cell Left")
        if pointer == 0:memory.insert(0, 0)
        else:pointer -= 1
        if debug["pointer"]:print("Pointer:", pointer)

    elif char == ">":
        if debug["type"]:print("Cell Right")
        if pointer == len(memory) - 1:memory.append(0)
        pointer += 1
        if debug["pointer"]:print("Pointer:", pointer)

    elif char == "+":
        if debug["type"]:print("Increment")
        memory[pointer] += 1
    elif char == "-":
        if debug["type"]:print("Decrement")
        memory[pointer] -= 1

    elif char == ".":
        if debug["type"]:print("Print Value")
        print(memory[pointer], end = "\n" if debug["newline"] else "")
    elif char == ",":
        if debug["type"]:print("Print Char")
        print(chr(memory[pointer]), end = "\n" if debug["newline"] else "")

    elif char == "?":
        if debug["type"]:print("Store Value")
        memory[pointer] = int(input())
    elif char == "!":
        if debug["type"]:print("Store Char")
        memory[pointer] = ord(input()[0])

    elif char == "@":
        if debug["type"]:print("Halt")
        running = False
        continue

    if debug["memory"]:print(memory)
    if debug["space"]:print("")

    steps += 1
    if steps == debug["maxSteps"]:
        running = False
        print("Maximum steps " + str(steps))

    if debug["step"]:input()

if debug["finalDump"]:print(memory)
