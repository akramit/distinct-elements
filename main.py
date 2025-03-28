import math


def distinct_elements(eps,delta,arr): 
    p=1
    thresh = 1/(eps**2)*12*log(len(arr)/delta)
    distinct_elements = []
    for i in range(0,len(arr)):
        distinct_elements.remove(arr[i])
        # with probability p, remove arr[i]




if __name__ == "__main__":
    distinct_elements()