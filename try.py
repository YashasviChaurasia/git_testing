def BSearch(start,end,nth,a,b):#s is start l in last p is to find a is arr 
    mid=int((start+end)/2);
    if(start<end):
        k=((mid//a)+(mid//b)-(mid//(a*b)));
        if (k==nth):
            if(mid%a==0 or mid%b==0): 
                return mid;
            else:
                end=mid;
                return BSearch(start,end,nth,a,b)
            
        elif (k>nth):
            end=mid-1;
            return BSearch(start,end,nth,a,b);
        else:
            start=mid+1;
            return BSearch(start,end,nth,a,b)
    #print("Nahi mila")    
    return -1;
    
a=17
b=11
n=9
#print(min(a,b))
print(BSearch(min(a,b),(min(a,b))*n,n,a,b))