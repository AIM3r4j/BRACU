# Function to calculate the waiting time of each process
def calculateWaiting(processes, n, waiting):
    waiting[0] = 0  # Setting the first one's waiting time to zero
    for i in range(1,n):
        waiting[i] = processes[i - 1][1] + waiting[i - 1]
 
# Function to calculate the turn-around time of each process
def calculateTurnaround(processes, n, waiting, turnaround):
    for i in range(n):
        #turnaround=burst+waiting
        turnaround[i] = processes[i][1] + waiting[i]
 
# Function to calculate the average waiting time and the average turnaround time and also print the outputs
def calculateTheAvgs(processes, n):
    waiting = [0] * n
    turnaround = [0] * n
 
    calculateWaiting(processes, n, waiting)
    calculateTurnaround(processes, n, waiting, turnaround)
 
    # Printing the Priority, WT, TAT of each process
    print("\nProcesses    Burst Time    Priority    Waiting Time    Turn-Around Time")
    for i in range(n):
        print(" P"+str(processes[i][0]), "\t\t",
                   processes[i][1], "\t\t",
                   processes[i][2], "\t\t",
                   waiting[i], "\t\t", turnaround[i])
                   
    # Calculating the total to get the average
    total_waiting = 0
    total_turnaround = 0
    for i in range(n):
        total_waiting = total_waiting + waiting[i]
        total_turnaround = total_turnaround + turnaround[i]
 
    #Printing the avgs
    print("\nAverage waiting time =",(total_waiting /n))
    print("Average turn-around time =",(total_turnaround / n))
       
     
# Process count
process_count = 5
# Processes with their id, burst time and priority
proc = [[1, 10, 3], # [process id, burst time, priority]
        [2, 1, 1],
        [3, 2, 4],
        [4, 1, 5],
        [5, 5, 2]]

# Sorting the processes based on priority
proc = sorted(proc, key = lambda proc:proc[2])
print("\nProcesses sorted by priority/order of execution:")
calculateTheAvgs(proc, process_count)