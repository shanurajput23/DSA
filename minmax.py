#make a class for min and max value 
class pair:
    def __init_(self):
        self.min=0
        self.max=0

def getminmax(arr:list,n:int) ->pair:
    minmax=pair()

#if there is only one element then it will display as min and max both 
    if n==1:
        minmax.max=arr[0]
        minmax.min=arr[0]
        return minmax

#if there are more than one element then initialize min and max
    if arr[0]>arr[1]:
        minmax.max=arr[0]
        minmax.min=arr[1]
    else:
        minmax.max=arr[1]
        minmax.max=arr[0]
    for i in range(2,n):
        if arr[i]>minmax.max:
            minmax.max=arr[i]
        elif arr[i]<minmax.min:
            minmax.min=arr[i]
    return minmax

#display code

if __name__== "__mian__":
    arr=[1000,734,88,1,53,334]
    arr_size=6
    minmax=getminmax(arr,arr_size)
    print("minmax element:",minmax.min)
    print("minmax element:",minmax.max)

