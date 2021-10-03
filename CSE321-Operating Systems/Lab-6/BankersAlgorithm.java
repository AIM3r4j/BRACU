import java.util.*;
import java.io.*;
public class BankersAlgorithm{
  public static void main(String[] args) throws Exception{
    BufferedReader input = new BufferedReader(new FileReader("bankers.txt"));
    
    int processCount=Integer.parseInt(input.readLine());
    int resCount=Integer.parseInt(input.readLine());
    
    String[] processes = new String[processCount];
    int[][] maxRes = new int[processCount][resCount];
    int[][] resAllocation = new int[processCount][resCount];
    int[][] needMatrix = new int[processCount][resCount];
    int[][] availableRes = new int[processCount+1][resCount];
    LinkedList<Integer> safeSeq = new LinkedList<Integer>();
    
    String processNameLine=input.readLine();
    StringTokenizer processName = new StringTokenizer(processNameLine, " ");
    
    int n=0;
    while(processName.hasMoreTokens()){
      processes[n]=processName.nextToken();
      n++;
    }
    
    for(int i=0; i<processCount; i++){
      String resLine=input.readLine();
      StringTokenizer res = new StringTokenizer(resLine, " ");
      
      for(int j=0; j<resCount; j++){
        maxRes[i][j]=Integer.parseInt(res.nextToken());
      }
    }
    
    for(int i=0; i<processCount; i++){
      String resAllocationLine=input.readLine();
      StringTokenizer allocated = new StringTokenizer(resAllocationLine, " ");
      
      for(int j=0; j<resCount; j++){
        resAllocation[i][j]=Integer.parseInt(allocated.nextToken());
        needMatrix[i][j]=maxRes[i][j]-resAllocation[i][j];
      }
    }
    
    System.out.print("Need Matrix :");
    for(int i=0; i<processCount; i++){
      System.out.println();
      
      for(int j=0; j<resCount; j++){
        System.out.print(needMatrix[i][j]+" ");
      }
    }
    
    System.out.println();
    String resAvailableLine=input.readLine();
    StringTokenizer availables = new StringTokenizer(resAvailableLine, " ");
    
    int counter=0;
    while(availables.hasMoreTokens()){
      availableRes[0][counter]=Integer.parseInt(availables.nextToken());
      counter++;
    }
    
    counter=0;
    for(int i=0;;i++){
      i = i % processCount;
      boolean flag=true;
      
      for(int j=0; j<resCount; j++){
        if(needMatrix[i][j]<=availableRes[counter][j]){
          
        }
        
        else{
          flag=false;
          break;
        }
        
        if(flag && j==(resCount-1) && !safeSeq.contains(i)){
          for(int k=0; k<resCount; k++){
            availableRes[counter+1][k]=availableRes[counter][k]+resAllocation[i][k];
          }
          
          safeSeq.addLast(i);
          counter++;
        }
      }
      
      if(safeSeq.size()==processCount){
        break;
      }
    }
    
    System.out.println("\nSafe sequence is :");
    for(int i=0; i<safeSeq.size(); i++){
      System.out.print(processes[safeSeq.get(i)]+" ");
    }
    
    System.out.println("\n");
    
    System.out.print("Change in available resource matrix : ");
    for(int i=1; i<availableRes.length; i++){
      System.out.println();
      
      for(int j=0; j<resCount; j++){
        System.out.print(availableRes[i][j]+" ");
      }
    }
    
    System.out.println("\n");
    input.close();
  }
}
