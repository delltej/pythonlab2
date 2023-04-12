#function and nested loop
num=float(input("Starting number of organism:"))
# average daily percentage of the Amazon rainforest.
per=float(input("Average daily percentage increase:"))
# for getting output for number of days
total=int(input("Enter the number of days to display the final data:"))
print("day approximate","       ","population")
c=num
print(num)
for i in range (1,total):
  #for getting the increase value
 c =num+(num*(per/100))
 print(i,"                ",c,"\n")
 num=c