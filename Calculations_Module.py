import math
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num):
    return num * num

def sqrt(num):
    return math.sqrt(num)

def cube(num):
    return num * num * num

def cbrt(num):
    return math.cbrt(num)

def sin(num):
    return math.sin(num)

def cos(num):
    return math.cos(num)

def tan(num):
    return math.tan(num)

def log(num):
    return math.log(num)

def abs(num):
    return abs(num)

def factorial(num):
    return math.factorial(num)

def sin-1(num):
    return math.asin(num)

def cos-1(num):
    return math.acos(num)

def tan-1(num):
    return math.atan(num)

def log-1(num)
    return math.exp(num)

def percent(num):
    return num / 100

def pi():
    return math.pi

def -pi():
    return -math.pi

def tau():
    return math.tau

def -tau():
    return -math.tau

def e():
    return math.e

def -e():
    return -math.e

def i():
    return 1j

def -i():
    return -1j

def infinity():
    return math.inf

def -infinity():
    return -math.inf

def NaN():
    return math.nan

def remainder(num1, num2):
    return num1 % num2

def power(num1, num2):
    return num1 ** num2

def GCF(num1, num2):
    return math.gcf(num1, num2)

def LCM(num1, num2):
    return math.lcm(num1, num2)

def mean(nums):
    data = list(nums.split())
    sum = 0
    for i in data:
        sum += i
    return sum / len(data)

def mode(nums)
    data = list(nums.split())
    counts = []
    for i in data:
        counts.append(data.count(i))
    counts.sort()
    return counts[len(counts) - 1]

def median(nums):
    data = list(nums.split())
    sorted_data = sorted([int(x) for x in data])
    sorted_data.sort()
    if len(sorted_data) % 2 == 0:
        mid = len(sorted_data) // 2
        return sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        mid = len(sorted_data) // 2
        return sorted_data[mid]

def max(nums):
    data = list(num.split())
    return max(data)

def min(nums):
    data = list(nums.split()))
    return min(data)

def range(nums):
    data = list(nums,split())
    return max(data) - min(data)

def mad(nums):
    data = list(nums.split())
    for i in data:
    differences = []
    for i in data:
        differences.append(i - mean(data))
    return mean(differences)

def combs(num1, num2):
    return math.comb(num1, num2)

def perms(num1, num2):
    return math.perm(num1, num2)

#one stands for only once
def Rand_num_1(nums, num):
    data = list(nums.split())
    return str((data.count(num) / len(data)) * 100) + "%" 

def Rand_nums_1(nums, nums2):
    data = list(nums.split())
    data2= list(nums2.split())
    sum = 0
    for i in data2:
        sum += data.count(i)
    return str((sum / len(data) * 100)) + "%"

#more than once
def Rand_num_2(nums, num, x):
    data = list(nums.split())
    return str((data.count(num) / len(data)**x) * 100) + "%"

def Rand_nums_2(nums, nums2, x):
    data = list(nums.split())
    data = list(nums2.split())
    sum = 0
    for i in data2:
        sum += data.count(i)
    return str((((sum / len(data)) ** x) * 100)) + "%"

#without replacement
def Rand_num_3(nums, num, x):
    data = list(nums.split())
    retrurn str((math.factorial(data.count(num)) / math.factorial(x) /math.factorial(data.count(num) - x)) * 100) + "%"

def Rand_nums_3(nums, nums2, x):
    data = list(nums.split())
    data2 = list(nums2.split())
    sum = 0
    data2 = list(q32.split())
    for i in data2:
        sum += data.count(i)
    return str((math.factorial(sum) / math.factorial(q33) / math.factorial(sum - q33)) * 100) + "%"

#Info:
'''
Name: Ilam
Age: 12 yrs old
This is the Calculator module I made as an inspiration from my calculator
I made this so you guys could use it as an easy way for calculations like mean and mode
Hopefully you guys like this!
'''

    






    
    

