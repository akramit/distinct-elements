import math
import random

def insert_with_prob(p): 
    rand_len = math.ceil(1/p)
    rand_num = random.randint(1,rand_len)
    if rand_num == 1:
        return True
    return False

def throw_elements_with_prob(elements, p):
    remove_elements_index = []
    for i in range(0, len(elements)):
        curr_el = elements[i]
        rand_len = math.ceil(1/p)
        rand_num = random.randint(1,rand_len)
        if rand_num == 1:
            remove_elements_index.append(i)

    final_elements = [] 
    for i in range(0, len(elements)):
        if i not in remove_elements_index:
            final_elements.append(elements[i])
    return final_elements

def distinct_elements(eps,delta,arr): 
    p=1
    thresh = 1/(eps**2)*12*math.log(len(arr)/delta)
    print("Threshold: ",thresh)
    distinct_elements = []
    for i in range(0,len(arr)):
        if arr[i] in distinct_elements:
            distinct_elements.remove(arr[i])
        # with probability p, remove arr[i]
        if insert_with_prob(p) :
            distinct_elements.append(arr[i])
        if len(distinct_elements) >= thresh:
            #throw each element in distinct_elements with prob p
            distinct_elements = throw_elements_with_prob(distinct_elements, p)
            p = p/2
            if len(distinct_elements) == thresh:
                print("Algorithm Failed")
                return
    return len(distinct_elements)//p        


if __name__ == "__main__":
    eps = 0.1
    delta = 0.1
    arr = [random.randint(1000000,9000000) for i in range(0,1000000)]
    set_arr = set(arr)
    print("Acutal Distinct Elements: ", len(set_arr))
    output = distinct_elements(eps,delta, arr)
    print("Algorithm Distinct Elements: ", output)
