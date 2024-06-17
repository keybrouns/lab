text = "If you need to Link to some research from a website or on social media, We want to encourage you to .Link to a RePEc page instead of directly to the full text."
count = 0
words = text.split(sep=" ")
for word in words:
    if word[0].isupper():
        count += 1
        
# print([word for word in text.split() if word[0].isupper()])
# print(len([word for word in text.split() if word[0].isupper()]))