import java.awt.*;

public class GUIProgram extends Frame {

    public GUIProgram(){

        // Create a check button
        Button btn = new Button("Check");
        btn.setBounds(120,125,50,25);
        add(btn);

        // Create a text field
        TextField text = new TextField();
        text.setBounds(95, 80, 100,25);
        add(text);

        // Set window size and visibility
        setSize(300,200);//frame size 300 width and 300 height
        setLayout(null);//no layout manager
        setVisible(true);//now frame will be visible, by default not visible
    }
}
