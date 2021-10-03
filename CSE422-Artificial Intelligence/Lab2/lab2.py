import numpy as np
def fitness(population, n):

  '''calculates the fitness score of each
     of the individuals in the population
     
     returns a 1D numpy array: index referring to 
     ith individual in population, and value referring 
     to the fitness score.'''
  import math

  #list of fitness function which will be converted to numpy array
  fit=[]

  #total possible non-attacking pairs
  TNAP=int((n*(n-1))/2)
  #list of Non-attcking pairs of each individual in population
  LNAP=[]

  for p in population:
    #count of horizontal attacking pairs
    HAP=0
    #count of diagonal attcaking pairs
    DAP=0
    #count of non-attacking pairs
    NAP=0

    #calculating horizontal attacks
    if len(set(p))<len(p):
      HAP+=(len(p)-len(set(p)))
    #calculating diagonal attacks
    for j in range(len(p)):
      for k in range(j):
        diff=j-k
        if p[k]==(p[j]-diff):
          DAP+=1
        elif p[k]==(p[j]+diff):
          DAP+=1
    #calculating non-attacking pairs and adding to the list
    NAP=TNAP-(HAP+DAP)
    LNAP.append(NAP)

  #sum of all Non-attacking pairs of the individuals
  summ=0
  for l in range(len(LNAP)):  
    summ+=LNAP[l]
  #fitness calculation
  for l in range(len(LNAP)): 
    f=LNAP[l]/summ
    fit.append(f)
  fitness=np.array(fit,dtype=float)
  return fitness
def select(population, fit):
  ''' take input:  population and fit
  fit contains fitness values of each of the individuals 
  in the population  

  return:  one individual randomly giving
  more weight to ones which have high fitness score'''
  m=int(len(population))
  a=np.empty(m,int)
  for i in range(m):
    a[i]=i
  print("A",a)
  print(fit)
  size = 1
  replace=True
  choice=int(np.random.choice(a, size, replace, fit))
  
  selection=population[choice]
  return selection
def crossover(x, y):
  '''take input: 2 parents - x, y. 
     Generate a random crossover point. 
     Append first half of x with second 
     half of y to create the child
     
     returns: a child chromosome'''
  #getting first half of parent X
  slice1shape=int((n/2)-1)
  slice1=[]
  s1=0
  while s1<slice1shape:
    slice1.append(s1)
    s1+=1
  slice1=np.array(x[slice1])

  #getting second half of parent Y
  slice2shape=int((n/2)+1)
  slice2=[]
  s2=slice1shape
  while s2<len(y):
    slice2.append(s2)
    s2+=1
  slice2=np.array(y[slice2])

  #child created from the crossover
  child=np.concatenate((slice1,slice2))
     
  return child
def mutate(child):
  '''take input: a child
     mutates a random 
     gene into another random gene
     
     returns: mutated child'''

  random1=np.random.randint(0,n-1)
  random2=np.random.randint(0,n-1)
  child[random1]=random2

  return child
def GA(population, n, mutation_threshold = 0.3):
  '''implement the pseudocode here by
     calling the necessary functions- Fitness, 
     Selection, Crossover and Mutation
     
     print: the max fitness value and the 
     chromosome that generated it which is ultimately 
     the solution board'''

  new_population=[]
  nmax=10000
  goal_fit=0.9

  fit=fitness(population,n)

  while nmax>0:
    if goal_fit in fit:
      index=np.where(fit>=goal_fit)
      print("Solution:",population[index])
      break
    else:
      for i in range(len(population)):
        x=select(population,fit)
        y=select(population,fit)
        child=crossover(x,y)
        if np.random.uniform(0,1)<mutation_threshold:
          child=mutate(child)
        new_population.append(child)
        population=new_population
        # print(population)
    nmax-=1

  return
'''for 8 queen problem, n = 8'''
n = 4

'''start_population denotes how many individuals/chromosomes are there
  in the initial population n = 8'''
start_population = 10 

'''if you want you can set mutation_threshold to a higher value,
   to increase the chances of mutation'''
mutation_threshold = 0.3

'''creating the population with random integers between 0 to 7 inclusive
   for n = 8 queen problem'''
population = np.random.randint(0, n, (start_population, n))
print(population)
'''calling the GA function'''
GA(population, n, mutation_threshold)