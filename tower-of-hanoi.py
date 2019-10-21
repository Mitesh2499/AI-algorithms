def toh(size,start,aux,des):
    if size ==1:
        print("move disk {} from {} to {} ".format(size,start,des))
        return 
    toh(size-1,start,des,aux)
    print("move disk {} from {} to {} ".format(size,start,des))
    toh(size-1,aux,start,des)

size=int(input("Enter Number of Disk :-  "))
toh(size,'A','B','C')
