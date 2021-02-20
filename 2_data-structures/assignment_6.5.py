text = "X-DSPAM-Confidence:    0.8475";
ppost = text.find("0")
#print(ppost)
num = float(text[ppost:])
print(num)
