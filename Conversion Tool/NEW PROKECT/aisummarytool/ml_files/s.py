from nltk.tokenize import sent_tokenize
ss="The indication insaa django. Thei indiad."
s=sent_tokenize(ss)
for e in s:
    if "indicat" in e:
        print("d")
