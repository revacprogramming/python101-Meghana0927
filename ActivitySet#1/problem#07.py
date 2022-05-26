# Strings

text = "X-DSPAM-Confidence:    0.8475"
num=text.find("0.8475")
n=text[num:]
print (float(n))