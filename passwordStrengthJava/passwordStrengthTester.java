import java.util.regex.Matcher;
import java.util.regex.Pattern;

import java.util.Scanner;

class PasswordStrengthTester {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        String input;

        new GUIProgram();

        while(true){
            System.out.println("Enter password (enter 'quit' to exit): ");
            input = scan.nextLine();

            passwordCheck(input);

            if (input.equals("quit")) {
                break;
            }
        }
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