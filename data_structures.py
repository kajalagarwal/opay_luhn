def square_and_rev(lst):
    n = len(lst)
    return [[el**2 for el in lst[n-1-i]] for i in range(n)]

def above_25(lst):
    output=[]
    for el in lst:
        output += [e for e in el if e>=25]
    return output

if __name__ == "__main__":
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rev_list = square_and_rev(input_list)
    above_25_list = above_25(rev_list)
    print "reversed and squared list is: %s" %(rev_list)
    print "elements above 25 are: %s" %(above_25_list)
    
# intended output is:
#reverse list should be  [[49, 64, 81], [16, 25, 36], [1, 4, 9]]   
#list with above 25 should be [49, 64, 81, 25, 36]
