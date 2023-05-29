#  Job Array= [['a', 2, 80],
        # ['b', 1, 19],
        # ['c', 2, 27],
        # ['d', 1, 25],
        # ['e', 3, 15]]

def printJobScheduling(arr, t):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    result = [False] * t
    job = ['-1'] * t
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
    print(job)

if __name__ == '__main__':
    arr = []
    n = int(input("Enter the number of jobs: "))
    t = 0
    for i in range(n):
        job_id = input("Enter job ID: ")
        deadline = int(input("Enter deadline: "))
        profit = int(input("Enter profit: "))
        arr.append([job_id, deadline, profit])
        t = max(t, deadline)

    print("Following is the maximum profit sequence of jobs:")
    printJobScheduling(arr, t)