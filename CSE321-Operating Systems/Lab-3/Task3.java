import java.util.Arrays;

//Sorting using QuickSort method
class SortingThread extends Thread {

    int low;
    int high;
    int[] arr;

    public SortingThread(int[] arr,int low, int high) {
        this.low = low;
        this.high = high;
        this.arr = arr;
    }

    @Override
    public void run() {
        if(low < high){
            int partitioningIndex = partition(arr, low, high);

            //Sorting left half and right half of partitioning index
            SortingThread leftPartSortingThread = new SortingThread(arr, low, partitioningIndex - 1);
            SortingThread rightPartSortingThread = new SortingThread(arr, partitioningIndex + 1, high);
            leftPartSortingThread.start();
            rightPartSortingThread.start();

            try {
                leftPartSortingThread.join();
                rightPartSortingThread.join();
            } catch (InterruptedException e) {
                System.out.println("Exception is caught "+e);
            }
        }
    }
    //Getter method of the sorted array
    int[] getArray() {
        return arr;
    }

    int partition(int[] arr, int low, int high) {
        //Assigning the pivot
        int pivot = arr[high];
        int i = low-1;

        //Placing the pivot in it's correct position in the array
        for (int j=low; j<high; j++){
            //Swapping if element is smaller than pivot
            if (arr[j] <= pivot){
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int tempo = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = tempo;
        return i+1;
    }
}
public class Task3 {
      
    public static void main(String[] args) {
        //The array to be sorted
        int array[] = {9,6,8,2,5,4};
        System.out.println("The Array to be sorted:");
        System.out.println(Arrays.toString(array));
        //Main sorting thread
        SortingThread thread1 = new SortingThread(array,0,array.length-1);
        thread1.start();
        try {
            thread1.join();
        } catch (InterruptedException e) {
            System.out.println("Exception is caught "+e);
        }
        //Getting and printing the array after sorting
        int[] sortedArray=thread1.getArray();
        System.out.println("\nThe Array after getting sorted:");
        System.out.println(Arrays.toString(sortedArray));

        // System.out.println("Sorted value");
        // for (int i :
        //         arr) {
        //     System.out.print(i + " ");
        // }
        // System.out.println();

    }
}