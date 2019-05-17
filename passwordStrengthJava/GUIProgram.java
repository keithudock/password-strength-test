import java.awt.*;
import java.awt.event.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class GUIProgram extends Frame implements ActionListener{
    TextField text;

    public GUIProgram(){

        //Create Frame
        Frame f = new Frame("Password Strength Tester");

        // Create a check button
        Button btn = new Button("Check");
        btn.setBounds(150,125,50,25);
        btn.addActionListener(this);
        f.add(btn);

        // Create a text field
        text = new TextField();
        text.setBounds(125, 80, 100,25);
        f.add(text);

        // Set window size and visibility
        f.setSize(350,200);//frame size 300 width and 300 height
        f.setLayout(null);//no layout manager
        f.setVisible(true);//now frame will be visible, by default not visible
    }

    public void actionPerformed(ActionEvent e){
        passwordCheck(text.getText());
    }

    public static void passwordCheck(String password) {
        Pattern lower = Pattern.compile(".*[a-z].*");
        Pattern upper = Pattern.compile(".*[A-Z].*");
        Pattern number = Pattern.compile(".*[1-9].*");

        Matcher lowerMatch = lower.matcher(password);
        Matcher upperMatch = upper.matcher(password);
        Matcher numberMatch = number.matcher(password);

        if (password.length() >= 8) {
            if (lowerMatch.find()) {
                if (upperMatch.find()) {
                    if (numberMatch.find()){
                        System.out.println("Good!");
                    }
                    else {
                        System.out.println("Password is not strong enough | Need at least one number");
                    }
                }
                else {
                    System.out.println("Password is not strong enough | Need at least one uppercase letter");
                }
            }
            else {
                System.out.println("Password is not strong enough | Need at least one lowercase letter");
            }
        }
        else {
            System.out.println("Password is not strong enough | Need at least eight characters");
        }
    }
}
