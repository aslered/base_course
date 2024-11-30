import time

m = 5 
n = 3  

start_time = time.time()  

for i in range(m):
    print(i)
    time.sleep(1)  
    for j in range(n):
        print(j)
        time.sleep(1)  

end_time = time.time()  
total_time = end_time - start_time

print(total_time)