# Job Scheduling Problem
profit = [15, 27, 10, 100, 150]
jobs = ["J1", "J2", "J3", "J4", "J5"]
deadline = [2, 3, 3, 3, 4]

#Sorting and Combining (Greedy Step)
profitNjobs = list(zip(profit, jobs, deadline))
profitNjobs = sorted(profitNjobs, key = lambda x: x[0], reverse = True)

#creating a list of slots
max_deadline = max(deadline)
slot = [0] * max_deadline
ans = ['null'] * max_deadline

total_profit = 0


for i in range(len(profitNjobs)):
    (job_profit, job_jobs, job_deadline) = profitNjobs[i]
    for j in range(job_deadline -1,-1,-1):
        if slot[j] ==0:
            slot[j] = 1
            ans[j] = job_jobs
            total_profit += job_profit
            break

print("jobs Scheduled: ", ans)
print("Total Profit: ", total_profit)
