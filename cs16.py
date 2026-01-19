t=tuple()
n=int(input("enter the range of number of elements in the tuple"))
for i in range(n):
    a=int(input("enter a number: "))
    t=t+(a,)
print("input tuples=", t)
Average=sum(t)/n
t=tuple(sorted(t))
print("maximum element of tuple", max(t))
print("minimum element of tuple", min(t))
print("sum of elements in tuple= ", sum(t))
print("average of the elements of the tuple", Average)
print("sorted tuple= ", t)
