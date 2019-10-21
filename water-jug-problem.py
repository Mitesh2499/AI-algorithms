def pour(from_capacity,to_capacity,d):
    from_=from_capacity
    to_=0

    print(from_,to_)
    while True: 
        if from_ > to_capacity:
            temp=from_-to_capacity
            to_=to_capacity
            from_=temp
            print(from_,to_)

        if to_ == to_capacity:
            to_=0
            print(from_,to_)       

        if from_ !=0:
            if from_<to_capacity:
                to_=from_
                from_=0
                print(from_,to_)

        if from_ ==0:
            from_=from_capacity
            print(from_,to_)

        if to_ !=0 and to_<to_capacity:
            temp=to_capacity-to_
            to_=to_+temp
            from_=from_ -temp
            print(from_,to_)
            
        if from_ ==d or to_ ==d:
            break
        
        
m=2
n=5
d=4
pour(n,m,d)
