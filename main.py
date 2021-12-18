print("SIROCCO - 2021.")
print("Each row of a SIROCCO cannot contain more than 10 characters. There can not be more than 10 rows. This limits you to 100 characters.\n")

SIROCCO = open(input("SIROCCO File Name.\n>"),mode="r").read()
print("Loading SIROCCO...")
SIROCCOMAP = []
for i in SIROCCO.split("\n"):
    RESULT = []
    for v in i:
        RESULT.append(v)
    SIROCCOMAP.append(RESULT)
print("Loaded...")
Option=input("Encode or Decode (e/d)?\n>")
if Option.lower()=="e":
    # Encode
    Result = ""
    for i in input(">"):
        Line = 0
        for Row in SIROCCOMAP:
            Character = 0
            for Char in Row:
                if Char.lower() == i.lower():
                    Result = Result+str(Line)+str(Character)
                Character = Character+1
            Line=Line+1
    print(Result)
else:
    # Decode.
    Result = ""
    CharSets = []
    CurrentSet = ""
    DB = True
    for i in input(">"):
        DB = not DB
        CurrentSet = CurrentSet+i
        if DB:
            CharSets.append(CurrentSet)
            CurrentSet=""
    for Set in CharSets:
        Line = int(Set[0])
        Character = int(Set[1])
        Result=Result+(SIROCCOMAP[Line][Character])
    print(Result)

input()
             
