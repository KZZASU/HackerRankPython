
#ListComprehension

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


vectors =[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            vector=[i,j,k]
            vectors.append(vector)

res = [vector for  vector in vectors if sum(vector)!=n]
print(res)


#Find the Runner-up Score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr = list(arr)
arr.sort()
while arr[-1]==arr[-2]:
    arr.remove(arr[-1])
print(arr[-2])



#Nested Lists

Scores=[]
name_Scores=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Scores.append(score)
        name_Scores.append([name,score])

Scores = set(Scores)
Scores = list(Scores)
Scores.sort(reverse=True)
a = Scores.pop()
a = Scores.pop()

low = [name_Score for name_Score in name_Scores if name_Score[1]==a]
low.sort()
for name in low:
    print(name[0])


#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_score = student_marks[query_name]
    avg_mark = sum(query_score)/len(query_score)
    
    print("%.2f" %avg_mark)

#Lists
if __name__ == '__main__':
    arr=[]
    N = int(input())
    for _ in range(N):
        func, *para = list(input().split())
        para = list(map(int,para))
        if func=="print":
             print(arr)
        else:
            getattr(arr,func)(*para)


#Tuples
        
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tup = tuple(integer_list)
    print(hash(tup))

