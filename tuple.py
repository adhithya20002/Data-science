# x=("apple","banana","cherry")
# y=list(x)
# y[1]="kiwi"
# x=tuple(y)
# print(x)

# thistuple=("apple","banana","cherry")
# y=list(thistuple)
# y.append("orange")
# thistuple=tuple(y)
# print(thistuple)

thistuple=("apple","banana","cherry")
y=("orange",)
thistuple+=y
print(thistuple)

thistuple=("apple","banana","cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

# thistuple=("apple","banana","cherry")
# y=list(thistuple)
# y.remove("apple")
# thistuple=tuple(y)
# print(thistuple)

# thistuple=("apple","banana","cherry")
# del thistuple
# print(thistuple)

# fruits=("apple","banana","cherry")
# mytuple=fruits*2
# print(mytuple)