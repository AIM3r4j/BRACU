class MyThread extends Thread {
	static int count = 1 ;
    
    public void run()
	{
		try {
            System.out.println(getName()+" Printed:");
			for( int i=0; i<10; i++){
                System.out.println(count);
                count++;
            }
		}
		catch (Exception e) {
			System.out.println("Exception is caught");
		}
	}
}

public class Task1 {
	public static void main(String[] args){
		//Creating two threads
        MyThread thread0 = new MyThread();
        MyThread thread1 = new MyThread();
		//Running first thread, then second thread, then again the first thread
        thread0.run();
	    thread1.run();
        thread0.run();
	}
}
