# for intial value
l = 0
num = int(input("enter year: "))
while (l < num):
  #intial value
  j = 0
  k = 0
  total = 0
  while (j < 12):
    print("Enter the rainfall amount of month:", j + 1, "")
    k = int(input())
    # for total rainfall
    total = total + k
    j += 1
  l = l + 1
  #for find out average rainfall of year
avg = total / 12
#for getting total and average value in inches
print("Total rainfall:", total, "","inches")
print("Average monthly rainfall:",avg,"","inches")
