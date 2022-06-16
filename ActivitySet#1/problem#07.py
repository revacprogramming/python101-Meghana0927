# Strings

text = "X-DSPAM-Confidence:    0.8475";
txt = text.find(':')
number = text[txt+1:]
n = float(number)
print(n)