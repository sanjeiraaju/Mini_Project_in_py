import time
a=int(input("Enter a number in Seconds: "))
for i in range(a,0,-1):
   a=i%60
   b=int(i/60)%60
   c=int(i/3600)
   print(f"{c:02d}:{b:02d}:{a:02d}")
   time.sleep(1)

print("Happy New Year!!!")