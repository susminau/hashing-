

  #Dr. green, so far i have this but i am trying to make another rehashing function to decrease the collision

def hashing_func(word, size):
    return len(word) % size
 #def rehashing_func(word, size)

        #return hash

a= 12000

data= [None]*a
count = 0
with open ('10000words.txt', 'r') as myFile:
    for line in myFile:
        for word in line.split():
            index=hashing_func(word,a)
            if data [index]:
                print (index)
                count+=1
            #coll
            else:
                data [index]= word



    print (data)
    print ('collision:' + str(count/a *100))
    print (index)


