def maxSum(arr, N, k):
    # MS[i] is going to store maximum sum
    # subsequence in subarray from arr[i]
    # to arr[n-1]
    MS = [0 for i in range(N)]
    # We fill MS from right to left.
    MS[N - 1] = arr[N - 1]
    for i in range(N - 2, -1, -1):
        if (i + k + 1 >= N):
            MS[i] = max(arr[i], MS[i + 1])



        else:
            MS[i] = max(arr[i] + MS[i + k + 1],
                        MS[i + 1])


    curr = MS[0]
    counter = 1
    list = []
    sum = 0
    for i in range(1,N):
        if(curr == MS[i]):
            counter += 1
        else:
            if(counter >= 2):
                list.append(i-1)
            curr = MS[i]
            counter = 1

    for i in list:
        sum += arr[i]

    if sum != MS[0]:
        list.append(N)
    return list

array = [3,4,7,1,7]
print(maxSum(array,5,2))