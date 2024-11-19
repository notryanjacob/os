def round_robin(processes, arrival_time, burst_time, time_quantum):
    n = len(processes)
    remaining_burst = burst_time.copy()  # Copy burst times for processing
    time = 0  # Current time
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    execution_order = []
    
    # Create a queue for round-robin processing
    queue = []
    visited = [False] * n
    
    # Add the processes which arrive at time 0 to the queue
    for i in range(n):
        if arrival_time[i] == 0:
            queue.append(i)
            visited[i] = True

    while queue:
        process_idx = queue.pop(0)
        execution_order.append(processes[process_idx])
        
        # Execute the process for time_quantum or the remaining burst time
        exec_time = min(time_quantum, remaining_burst[process_idx])
        time += exec_time
        remaining_burst[process_idx] -= exec_time

        # Check if the process has finished
        if remaining_burst[process_idx] == 0:
            completion_time[process_idx] = time
            turnaround_time[process_idx] = completion_time[process_idx] - arrival_time[process_idx]
            waiting_time[process_idx] = turnaround_time[process_idx] - burst_time[process_idx]
        
        # Add newly arrived processes to the queue
        for i in range(n):
            if arrival_time[i] <= time and not visited[i] and remaining_burst[i] > 0:
                queue.append(i)
                visited[i] = True
        
        # If the process is not finished, add it back to the queue
        if remaining_burst[process_idx] > 0:
            queue.append(process_idx)
    
    return execution_order, completion_time, turnaround_time, waiting_time


# Input Section
n = int(input("Enter the number of processes: "))
processes = [i + 1 for i in range(n)]
arrival_time = list(map(int, input("Enter arrival times: ").split()))
burst_time = list(map(int, input("Enter burst times: ").split()))
time_quantum = int(input("Enter the time quantum: "))

# Calling the Round Robin function
execution_order, completion_time, turnaround_time, waiting_time = round_robin(
    processes, arrival_time, burst_time, time_quantum
)

# Output Section
print("\nExecution Order:", execution_order)
print("\nProcess\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
for i in range(n):
    print(
        f"P{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t"
        f"{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}"
    )