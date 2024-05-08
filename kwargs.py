def kwargsFunc(*kwargs):
    sum,count = 0,0
    for i in kwargs:
        print(i,end=", ")
        sum += i
        count += 1
    print("Total sum: ",sum)
    print("Average: ", sum/count) 



kwargsFunc(1,2,3,4,5)