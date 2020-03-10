##use both the for loop and a while loop
##printing one out and then two and then three and four... up to 10
##you can take advantage of the fact that you can multiply a string by a number
#to print it out multiple times.
##
##Or an alternative:
##nested loops so I'll show you that as a potential option



##for emoji in range(1,11):
##    print("\U0001f600"*emoji)




emoji=1

while emoji<=10:
    print("\U0001f600"*emoji)
    emoji+=1
