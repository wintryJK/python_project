
class Tree:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None
    
def sort(list1,list2):
    m,n = len(list1),len(list2)
    out_list = []
    st1 = 0
    st2 = 0
    while st1 < m and st2 < n:
        if list1[st1] < list2[st2]:
            out_list.append(list1[st1])
            st1 += 1
        else:
            out_list.append(list2[st2])
            st2 += 1
    if st1 == m:
        out_list = out_list+list2[st2:]
    else:
        out_list = out_list+list1[st1:]

    return out_list

if __name__ == '__main__':
    list1 = [1,12,22,1111]
    list2 = [2,4,9,10,11]
    print(sort(list1,list2))