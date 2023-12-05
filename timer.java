import java.util.Timer;
import java.util.TimerTask;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class AlarmApp {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Alarm App!");
        System.out.print("Enter the time for the alarm (HH:mm:ss): ");

        String timeInput = scanner.nextLine();

        try {
            SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
            Date alarmTime = dateFormat.parse(timeInput);

            Timer timer = new Timer();
            timer.schedule(new AlarmTask(), alarmTime);

            System.out.println("Alarm set for: " + timeInput);

        } catch (Exception e) {
            System.out.println("Invalid time format. Please use HH:mm:ss");
        }
    }

    static class AlarmTask extends TimerTask {
        @Override
        public void run() {
            System.out.println("\nAlarm! It's time!");
        }
    }
}
