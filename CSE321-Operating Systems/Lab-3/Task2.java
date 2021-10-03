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
            //Count if how many numbers to print
            int count=10000;

            //Array for the divisors
            Integer[] divArray= new Integer[count+1];

            //Array for the numbers
            Integer[] numArray= new Integer[count+1];
            
            //Adding numbers to the number array
            numArray[0]=0;
            for(int i=1; i<=count ; i++){
                numArray[i]=start;
                start++;
            }
            
            //Adding divisors to the divisor array
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
            //Getting the max divisor count
            maxDiv=Collections.max(Arrays.asList(divArray));
            
            //Getting the number with the max divisors
            maxNum=numArray[findIndex(divArray,maxDiv)];
            
		}
		catch (Exception e) {
			System.out.println("Exception is caught "+e);
		}
	}
    //Method to get the index of an element
    static Integer findIndex(Integer arr[], Integer t){
        ArrayList<Integer> list = new ArrayList<>();
 
        for (int i : arr)
            list.add(i);
            
        return list.indexOf(t);
    }

    //Getter methods
    Integer getNumber(){
        return maxNum;
    }
    Integer getDivisor(){
        return maxDiv;
    }
}

public class Task2 {
    
	public static void main(String[] args){
        //Array for ten threads
        MyThread2[] threads= new MyThread2[10];
        //Array for max divisors and numbers with max divisors from different ranges
        Integer[] ultimateNum=new Integer[10];
        Integer[] ultimateDiv=new Integer[10];

        //Creating and starting the threads
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

        //Filling up the arrays
        int n=0;
        for(MyThread2 i : threads){
            ultimateNum[n]=i.getNumber();
            ultimateDiv[n]=i.getDivisor();
            ++n;
        }

        //Getting the max divisor count and the number with the max divisor count
        Integer ultimateDivisor=Collections.max(Arrays.asList(ultimateDiv));
        Integer ultimateIndex= MyThread2.findIndex(ultimateDiv,ultimateDivisor);
        Integer ultimateNumber= ultimateNum[ultimateIndex];
        System.out.println("The Integer number "+ultimateNumber+" has the largest number of divisors, which is "+ultimateDivisor+" divisors");

	}
}
