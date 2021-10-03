import java.util.Arrays;
import java.util.Collections;
import java.lang.reflect.Array;
import java.util.ArrayList;


class MyThread2 extends Thread {
    int start;
    Integer maxDiv=0;
    Integer maxNum=0;
    
    public MyThread2(int s){
        this.start=s;
    }
    
    @Override
    public void run(){
		try {
            //Same thread from task-2
            int count=10000;
            Integer[] divArray= new Integer[count+1];
            Integer[] numArray= new Integer[count+1];
            numArray[0]=0;
            for(int i=1; i<=count ; i++){
                numArray[i]=start;
                start++;
            }
            divArray[0]=0;
            for (int i=1; i<=count ; i++){
                Integer num = numArray[i];
                Integer divisors =1;
                for (int d = 2; d <= num; d++) {
                    if (num % d == 0) 
                    {
                        divisors++;
                    }  
                }
                divArray[i]= divisors;
        	}
            maxDiv=Collections.max(Arrays.asList(divArray));
            maxNum=numArray[findIndex(divArray,maxDiv)];
            
		}
		catch (Exception e) {
			System.out.println("Exception is caught "+e);
		}
	}
    static Integer findIndex(Integer arr[], Integer t){
        ArrayList<Integer> list = new ArrayList<>();
 
        for (int i : arr)
            list.add(i);
            
        return list.indexOf(t);
    }
    Integer getNumber(){
        return maxNum;
    }
    Integer getDivisor(){
        return maxDiv;
    }
}

public class Task2Bonus {
    
	public static void main(String[] args){
        // Multi-threaded program start
        long startTime=System.currentTimeMillis();
        MyThread2[] threads= new MyThread2[10];
        Integer[] ultimateNum=new Integer[10];
        Integer[] ultimateDiv=new Integer[10];
        Integer threadCount=1;
        for( int i=0; i<10; i++){
            MyThread2 thread = new MyThread2(threadCount);
            thread.start();
            threads[i]=thread;
            threadCount+=10000;
        }

        for(MyThread2 i : threads){
            try {
                i.join();
            } catch (Exception e) {
                System.out.println(e);
            }
        }
        int n=0;
        for(MyThread2 i : threads){
            ultimateNum[n]=i.getNumber();
            ultimateDiv[n]=i.getDivisor();
            ++n;
        }

        Integer ultimateDivisor=Collections.max(Arrays.asList(ultimateDiv));
        Integer ultimateIndex= MyThread2.findIndex(ultimateDiv,ultimateDivisor);
        Integer ultimateNumber= ultimateNum[ultimateIndex];
        long endTime=System.currentTimeMillis();
        System.out.println("Multi-Threaded has taken "+(endTime-startTime)+" ms");
        // Multi-threaded program end

        // Single-threaded program start
        startTime=System.currentTimeMillis();
        threads= new MyThread2[10];
        ultimateNum=new Integer[10];
        ultimateDiv=new Integer[10];
        threadCount=1;
        for( int i=0; i<10; i++){
            MyThread2 thread = new MyThread2(threadCount);
            thread.run();
            threads[i]=thread;
            threadCount+=10000;
        }

        n=0;
        for(MyThread2 i : threads){
            ultimateNum[n]=i.getNumber();
            ultimateDiv[n]=i.getDivisor();
            ++n;
        }

        ultimateDivisor=Collections.max(Arrays.asList(ultimateDiv));
        ultimateIndex= MyThread2.findIndex(ultimateDiv,ultimateDivisor);
        ultimateNumber= ultimateNum[ultimateIndex];
        endTime=System.currentTimeMillis();
        System.out.println("Single-Threaded has taken "+(endTime-startTime)+" ms");
        // Single-threaded program end
	}
}
