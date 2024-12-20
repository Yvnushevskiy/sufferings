//ya v axuei
import math
def two_squares(n):
    def find_nearest_minimum(array, target):
        point = target%10
        filtered_array = [number for number in array if number < point]
        if (not filtered_array or point == 0) and y >= 10:
            answer = y - 10 - y % 10 + max(array)
            return answer
        else:
            answer = y - y % 10 + max(filtered_array)
            return answer
    def find_nearest_maximum(array,target):
        point = target%10
        filtered_array=[number for number in array if number> point]
        if not filtered_array or point== 9:
            answer = y + 10 -y%10 + min(array)
            return answer
        else:
            answer = y -y%10 + min(array)
            return answer

    def find_square(n, y, summX):
        if (n - y ** 2) % 4 == 0 or (n - y ** 2) % 4 == 1:
            if math.isqrt(n - y ** 2) ** 2 + y ** 2 == n:
                Yvariations.append(y)
                Xvariations.append(math.isqrt(int((n - y ** 2))))

        return find_nearest_minimum(summX,y)
    y = math.isqrt(n)
    b=y/2
    Yvariations = []
    Xvariations = []
    sumsquar = []
    summ1 = [0, 1, 9, 6, 5, 4]
    summ2 = [1, 9, 4, 6]
    summ3 = [2, 3, 7, 8]
    summ4 = [0, 4, 6, 8]
    summ5 = [5, 0, 2, 1, 9, 8, 7, 3, 6, 4]
    summ6 = [6, 0, 5, 9, 1]
    summ7 = [4, 1, 9, 8]
    summ8 = [3, 7, 2, 8]
    summ9 = [7, 3, 0, 2, 8, 5]
    summ0 = [5, 0, 2, 1, 9, 8, 7, 3, 6, 4]
    z=[1,0,2]
    if n % 4 in z:
        while y > b :
            if n%10==1:
                y=find_square(n,y,summ1)
            elif n%10 == 2:
                y=find_square(n,y,summ2)
            elif n%10 == 3:
                y=find_square(n,y,summ3)
            elif n%10 == 4:
                y=find_square(n,y,summ4)
            elif n%10 == 5:
                y=find_square(n, y, summ5)
            elif n%10 == 6:
                y=find_square(n, y, summ6)
            elif n%10 == 7:
                y=find_square(n, y, summ7)
            elif n%10 == 8:
                y=find_square(n,y,summ8)
            elif n%10 == 9:
                y=find_square(n,y,summ9)
            elif n%10 == 0:
                y=find_square(n,y,summ0)

        for j in range(len(Yvariations)):
                sumsquar.append(Xvariations[j] + Yvariations[j])
        if len(sumsquar) == 0:
                return 0
        else:
            return max(sumsquar)
    else:
        return 0

print(two_squares(369))
