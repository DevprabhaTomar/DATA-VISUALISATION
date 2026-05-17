print("enter any 10 sentence (hit enter key for new sentence):")
for x in range(10):
    sentence = input()
    #writing the data into the file
    filev . write(sentence)
    print("------------------------------------------------")
    print("data written successfully into the file ")
    filev . close()