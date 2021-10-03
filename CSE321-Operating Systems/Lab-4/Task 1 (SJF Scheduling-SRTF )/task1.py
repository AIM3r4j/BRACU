# Function to calculate the waiting time of each process
def calculateWaiting(processes, n, waiting):
    process_check = False
    current_time = 0
    completed = 0 #completed process count
    minm = 99999
    shortest_remaining = 0
    

    # Array for remaining times
    remaining = [0] * n
    for i in range(n):
        remaining[i] = processes[i][2]
    
 
    # Loops till the processes get completed/terminated
    while (completed != n):
         
        # Find process with minimum remaining time at the moment
        for j in range(n):
            if ((processes[j][1] <= current_time) and (remaining[j] < minm) and remaining[j] > 0):
                minm = remaining[j]
                shortest_remaining = j
                process_check = True
        if (process_check == False):
            current_time += 1
            continue
        remaining[shortest_remaining] -= 1
        minm = remaining[shortest_remaining]
        if (minm == 0):
            minm = 99999
 
        # Checking if a process is completed
        if (remaining[shortest_remaining] == 0):
 
            completed += 1
            process_check = False
            finish_time = current_time + 1
 
            # Calculate the waiting time
            waiting[shortest_remaining] = (finish_time - proc[shortest_remaining][2] - proc[shortest_remaining][1])
 
            if (waiting[shortest_remaining] < 0):
                waiting[shortest_remaining] = 0
         
        # Increasing the current time by 1
        current_time += 1
 
# Function to calculate the turnaround time of each process
def calculateTurnaround(processes, n, waiting, turnaround):
    for i in range(n):
        #turnaround=burst+waiting
        turnaround[i] = processes[i][2] + waiting[i]
 
# Function to calculate the average waiting time and the average turnaround time and also print the outputs
def calculateTheAvgs(processes, n):
    waiting = [0] * n
    turnaround = [0] * n
 
    calculateWaiting(processes, n, waiting)
    calculateTurnaround(processes, n, waiting, turnaround)
 
    # Printing the CT, WT, TAT of each process
    print("\nProcesses    Arrival Time    Burst Time     Completion Time     Waiting Time     Turn-Around Time")

    for i in range(n):
        print(" P"+str(processes[i][0]), "\t\t",
                processes[i][1], "\t\t",
                processes[i][2], "\t\t",
                processes[i][1]+turnaround[i], "\t\t",
                waiting[i], "\t\t\t", turnaround[i])
    
    # Calculating the total to get the average
    total_waiting = 0
    total_turnaround = 0

    for i in range(n):
        total_waiting = total_waiting + waiting[i]
        total_turnaround = total_turnaround + turnaround[i]
    
    # Printing the avgs
    print("\nAverage waiting time = ",(total_waiting / n) )
    print("Average turn-around time = ",(total_turnaround / n))

# Process count 
process_count = 4

# Each process with their id, burst time and arrival time

proc = [[1, 0, 8], # [process id, arrival time, burst time]
        [2, 1, 4],
        [3, 2, 9],
        [4, 3, 5]] 

calculateTheAvgs(proc, process_count)