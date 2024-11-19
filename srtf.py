def srtf(processes, arrival_time, burst_time):
    n = len(processes)
    remaining_burst = burst_time.copy()
    time = 0  # Current time
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    execution_order = []
    completed = 0

    while completed < n:
        # Find the process with the shortest remaining time
        min_remaining = float('inf')
        current_process = None

        for i in range(n):
            if arrival_time[i] <= time and remaining_burst[i] > 0:
                if remaining_burst[i] < min_remaining:
                    min_remaining = remaining_burst[i]
                    current_process = i

        if current_process is None:  # No process available to execute
            time += 1
            continue

        # Execute the process for 1 time unit
        execution_order.append(processes[current_process])
        remaining_burst[current_process] -= 1
        time += 1

        # Check if the process has completed
        if remaining_burst[current_process] == 0:
            completed += 1
            completion_time[current_process] = time
            turnaround_time[current_process] = completion_time[current_process] - arrival_time[current_process]
            waiting_time[current_process] = turnaround_time[current_process] - burst_time[current_process]

    return execution_order, completion_time, turnaround_time, waiting_time


# Input Section
n = int(input("Enter the number of processes: "))
processes = [i + 1 for i in range(n)]
arrival_time = list(map(int, input("Enter arrival times: ").split()))
burst_time = list(map(int, input("Enter burst times: ").split()))

# Calling the SRTF function
execution_order, completion_time, turnaround_time, waiting_time = srtf(processes, arrival_time, burst_time)

# Output Section
print("\nExecution Order:", execution_order)
print("\nProcess\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
for i in range(n):
    print(
        f"P{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t"
        f"{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}"
    )
