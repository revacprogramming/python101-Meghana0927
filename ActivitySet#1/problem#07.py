# Strings

fname = input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    l=line.find("0")
    number=float(line[l:])
    count=count+1
    total=total+number
avg=total/count
print ("Average spam confidence:",avg)