
# Set.union() 
n = int(input())
roll_list1 = set(map(int, input().split()))
N = int(input())
roll_list2 =set(map(int, input().split()))

print(len(roll_list1.union(roll_list2)))

# Set.intersection()
n = int(input())
roll_list1 = set(map(int, input().split()))
N = int(input())
roll_list2 =set(map(int, input().split()))

print(len(roll_list1.intersection(roll_list2)))

# Set.difference()
n = int(input())
roll_list1 = set(map(int, input().split()))
N = int(input())
roll_list2 =set(map(int, input().split()))

print(len(roll_list1.difference(roll_list2)))



# Set.symmetric_difference()
n = int(input())
roll_list1 = set(map(int, input().split()))
N = int(input())
roll_list2 =set(map(int, input().split()))

print(len(roll_list1.symmetric_difference(roll_list2)))




# Set Mutations
a_length = int(input())
A = set(map(int, input().split()))
num_oper = int(input())

for _ in range(num_oper):
    oper, N = input().split()
    B = set(map(int, input().split()))
    getattr(A,oper)(B)

print(sum(A))


# Captain's Room
K = int(input())
room_list = input().split()
half = len(room_list)//2
A = set(room_list[0:half])
B = set(room_list[half:])
C = A.difference(B)
D = B.difference(A)
if len(C):
    print(C.pop())
else:
    print(D.pop())

    
#Symmetric Difference
N = int(input())
N_set = set(map(int,input().split()))
M = int(input())
M_set = set(map(int,input().split()))    

Xor = N_set ^ M_set

for x in sorted(Xor):
    print(x)


#Set.add()
Country_stamp =set()
N = int(input())
for i in range(N):
    Country = input()
    Country_stamp.add(Country)

print(len(Country_stamp))


#Set .discard(), .remove() & .pop()
n = int(input())
A = set(map(int,input().split()))
N = int(input())
for i in range(N):
    oper, *para = list(input().split())
    para = list(map(int,para))
    getattr(A,oper)(*para)

print(sum(A))


#Check Subset
T = int(input())
for _ in range(T):
    a = int(input())
    A = set(map(int,input().split()))
    b = int(input())
    B = set(map(int,input().split()))
    test = A.difference(B)
    print(not bool(test))
    

#Check Strict Subset
A = set(map(int,input().split()))
n = int(input())

test = True
while bool(n)&test:
    n = n-1
    B = set(map(int,input().split()))
    test = not bool(A.difference(B))

print(test)


#No Idea!
n, m = list(map(int,input().split()))
arr = set(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))

happiness = 0

for i in arr:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1
    else:
        pass

print(happiness)