string = " Leo , nardo ".split(",")

for i, item in enumerate(string):
    string[i] = item.strip() # cuts " " in the begging and in the end of a string
print(string, "\n")

string = "-".join(string) # joins iterables according to separator "-"
string_ = "-".join("Leo")

print(string, string_, sep="\n")