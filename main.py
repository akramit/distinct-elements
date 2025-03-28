import math


def distinct_elements(eps,delta,arr): 
    p=1
    thresh = 1/(eps**2)*12*log(len(arr)/delta)
    distinct_elements = []
    for i in range(0,len(arr)):
        distinct_elements.remove(arr[i])
        # with probability p, remove arr[i]
        if insert_with_prob(p) :
            distinct_elements.insert(arr[i])
        if len(distinct_elements) >= thresh:
            distinct_elements = distinct_elements[:thresh]



if __name__ == "__main__":
    distinct_elements()