import time
s=0
s1=0
s2=0
s3=0
ansIntegral=0
a=float(input("下界a:"))
b=float(input("上界b:"))
n=int(input("分割次數n(必須為偶數):"))
i=int(input("最高次冪:"))
def c(x):
    fx=0
    for o in range(0,i+1):
        fx += (x**o)*f[o][1]
    return fx
f=[[0]*2 for j in range(0,i+1)]
for k in range(i,-1,-1):
    f[k][0]=k
    f[k][1]=float(input(f"x{k}次的係數:"))
dx = (b-a)/n

start_time_s = time.perf_counter()
for m in range(1,n):
    s += 2*c(a+dx*m)
end_time_s = time.perf_counter()
execution_time_s = end_time_s - start_time_s

start_time_s3 = time.perf_counter()
for p in range(1,n-1,2):
    s3 += 2*c(a+dx*p)
s3=s+s3
s3=s3+c(a)+c(b)
s3=s3*dx*(1/3)
end_time_s3 = time.perf_counter()
execution_time_s3 = end_time_s3 - start_time_s3 + execution_time_s

start_time_s1 = time.perf_counter()
s1=0.5*s
s1 += c(a+dx*m)
s1=s1*dx
end_time_s1 = time.perf_counter()
execution_time_s1 = end_time_s1 - start_time_s1 + execution_time_s

start_time_s2 = time.perf_counter()
s2=s
s2 += c(a)
s2 += c(b+dx)
s2=s2*dx
s2 = s2/2
end_time_s2 = time.perf_counter()
execution_time_s2 = end_time_s2 - start_time_s2 + execution_time_s

for g in range(0,i+1):
    f[g][1]=f[g][1]*(1/(g+1))
    f[g][0]+=1
ansIntegral=c(b)-c(a)

print("Riemann Sum積分後結果:",s1)
print("梯形法積分結果",s2)
print("拋物線法積分結果",s3)
print(f"積分結果:{ansIntegral}\n與Riemann Sum之誤差:{abs(ansIntegral-s1)}\n與梯形法之誤差{abs(ansIntegral-s2)}\n與拋物線法之誤差{abs(ansIntegral-s3)}")
print(f"Riemann Sum之時間:{execution_time_s1}\n與梯形法之時間{execution_time_s2}\n與拋物線法之時間{execution_time_s3}")   