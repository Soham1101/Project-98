data_a = 0
data_b = 0

def swapFileData():
#Reading both files and assigning them to data_a and data_b
    with open('sample1.txt', 'r') as a:
        data_a = a.read()
        
    with open('sample2.txt', 'r') as b:
        data_b = b.read()

#Opening files in write mode and swapping data
    with open('sample1.txt', 'w') as a:
        a.write(data_b)

    with open('sample2.txt', 'w') as b:
        b.write(data_a)

swapFileData()
