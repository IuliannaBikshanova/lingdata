import sys

source = open(sys.argv[1], 'r', encoding="utf-8")
dest = open(sys.argv[2], 'w')
for line in source.readlines():
    cols = line.split('\t')
    organ = ""
    if "пальц" in cols[3]:
        organ += "finger" + ", "
    if "ладон" in cols[3] or "кист" in cols[3]:
        organ += "hand" + ", "
    if "глаз" in cols[3] or "бров" in cols[3] or "голов" in cols[3] or "губ" in cols[3]:
        organ += "head" + ", "
    if "корпус" in cols[3]:
        organ += "body" + ", "
    dest.write("gestActiveOrgan@iab2005f\t{}\t{}\t{}\n".format(cols[1], cols[2], organ[: -2]))
dest.close()
source.close()