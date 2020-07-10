
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
