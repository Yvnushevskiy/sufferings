
summ1 = [0,1,9,6,5,4]
summ2 = [1,9,4,6]
summ3 = [2,3,7,8]
summ4 =[0,4,6,8]
summ5 = [5,0,2,1,9,8,7,3,6,4]
summ6 = [6,0,5,9,1]
summ7 = [4,1,9,8]
summ8 = [3,7,2,8]
summ9 = [7,3,0,2,8,5]
summ0 = [5,0,2,1,9,8,7,3,6,4]


def find_nearest_minimum(array, target):
    filtered_array = [number for number in array if number < target]

    if (not filtered_array or max(filtered_array)==0) and y>10:
       answer = y-10-y%10+max(array)
       return answer
    else:
        answer = y-y%10+max(filtered_array)
        return answer
