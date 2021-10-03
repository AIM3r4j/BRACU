# Function to calculate the waiting time of each process
def calculateWaiting(processes, n, waiting, quantum): 
    current_time = 0
    # Array for remaining burst times
    remaining_burst_time = [0] * n
    for i in range(n): 
        remaining_burst_time[i] = processes[i][1]
  
    # Loops till the processes get completed/terminated
    while(True):

        # Indicates if all the processes are finished
        completed = True
        for i in range(n):
              
            # If there is burst time remaining then it will proceeed
            if (remaining_burst_time[i] > 0) :
                completed = False

                if (remaining_burst_time[i] > quantum) :
                    current_time += quantum
                    remaining_burst_time[i] -= quantum 
                
                else:
                    current_time = current_time + remaining_burst_time[i] 
  
                    # Waiting time=current time-burst time
                    waiting[i] = current_time - processes[i][1] 
                    remaining_burst_time[i] = 0
                  
        # If all the processes are finished then it breaks the loop 
        if (completed == True):
            break
              
# Function to calculate the turn-around time of each process
def calculateTurnaround(processes, n, waiting, turnaround):
    for i in range(n):
        #turnaround=burst+waiting
        turnaround[i] = processes[i][1] + waiting[i] 
  
  
# Function to calculate the average waiting time and the average turnaround time and also print the outputs 
def calculateTheAvgs(processes, n, quantum): 
    waiting = [0] * n
    turnaround = [0] * n 
  
    calculateWaiting(processes, n, waiting, quantum)
    calculateTurnaround(processes, n, waiting, turnaround) 
  
    # Printing the WT, TAT of each process
    print("Processes    Burst Time     Waiting", 
                     "Time    Turn-Around Time")
    for i in range(n):
        print(" P"+str(i+1), 
            "\t\t", processes[i][1], 
            "\t\t", waiting[i],
            "\t\t", turnaround[i])
  
    # Calculating the total to get the average
    total_waiting = 0
    total_turnaround = 0
    for i in range(n):
  
        total_waiting = total_waiting+ waiting[i] 
        total_turnaround = total_turnaround + turnaround[i] 
    
    #Printing the avgs
    print("\nAverage waiting time = %.2F" %(total_waiting /n))
    print("Average turn around time =%.2F" %(total_turnaround / n))


# Time quantum 
quantum = 4
# Process count
process_count = 3  
# Processes with their id and burst time
proc = [[1, 24], # [process id, burst time]
        [2, 3],
        [3, 3]]

calculateTheAvgs(proc, process_count,  quantum)
