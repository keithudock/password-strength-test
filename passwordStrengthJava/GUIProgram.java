import java.awt.*;
import java.awt.event.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class GUIProgram implements ActionListener{
    TextField text;
    Frame f;
    Label l;

    public GUIProgram(){

        //Create Frame
        f = new Frame("Password Strength Tester");

        // Create a blank label
        l = new Label();
        l.setBounds(85,150,200,25);
        f.add(l);

        // Create a check button
        Button btn = new Button("Check");
        btn.setBounds(150,125,50,25);
        btn.addActionListener(this);
        f.add(btn);

        // Create a text field
        text = new TextField();
        text.setBounds(125, 80, 100,25);
        f.add(text);

        // Allow the window to close
        f.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                f.dispose();
            }
        });

        // Set window size and visibility
        f.setSize(350,200);//frame size 300 width and 300 height
        f.setLayout(null);//no layout manager
        f.setVisible(true);//now frame will be visible, by default not visible
    }

    public void actionPerformed(ActionEvent e){
        passwordCheck(text.getText());
    }

    public void passwordCheck(String password) {
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
                        l.setText("Good!");
                        System.out.println("Good!");
                    }
                    else {
                        l.setText("Password is not strong enough");
                        System.out.println("Password is not strong enough | Need at least one number");
                    }
                }
                else {
                    l.setText("Password is not strong enough");
                    System.out.println("Password is not strong enough | Need at least one uppercase letter");
                }
            }
            else {
                l.setText("Password is not strong enough");
                System.out.println("Password is not strong enough | Need at least one lowercase letter");
            }
        }
        else {
            l.setText("Password is not strong enough");
            System.out.println("Password is not strong enough | Need at least eight characters");
        }
    }
}
