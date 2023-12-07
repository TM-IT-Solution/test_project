import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

public class AlarmApp extends JFrame {
    private JTextField timeField;

    public AlarmApp() {
        super("Alarm App");

        // Create components
        JLabel label = new JLabel("Set Alarm Time (HH:mm:ss): ");
        timeField = new JTextField(10);
        JButton setAlarmButton = new JButton("Set Alarm");

        // Set layout
        setLayout(new FlowLayout());

        // Add components to the frame
        add(label);
        add(timeField);
        add(setAlarmButton);

        // Add action listener to the button
        setAlarmButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                setAlarm();
            }
        });

        // Set frame properties
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 120);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private void setAlarm() {
        // Get the alarm time from the text field
        String alarmTimeString = timeField.getText().trim();

        // Parse the time string and schedule the alarm
        try {
            SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
            Date alarmTime = dateFormat.parse(alarmTimeString);

            // Calculate the delay until the alarm
            long delay = alarmTime.getTime() - System.currentTimeMillis();

            // Schedule the alarm using a TimerTask
            Timer timer = new Timer();
            timer.schedule(new TimerTask() {
                @Override
                public void run() {
                    JOptionPane.showMessageDialog(null, "Alarm!");
                }
            }, delay);

            JOptionPane.showMessageDialog(null, "Alarm set for " + alarmTimeString);
        } catch (ParseException e) {
            JOptionPane.showMessageDialog(null, "Invalid time format. Please use HH:mm:ss");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new AlarmApp();
            }
        });
    }
}
