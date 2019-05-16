import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class PasswordStrengthTest {
    private final String line = "abcD1";
    private final Pattern lower = Pattern.compile(".*[a-z].*");
    private final Pattern upper = Pattern.compile(".*[A-Z].*");
    private final Pattern number = Pattern.compile(".*[1-9].*");
    public Matcher m;

    @Test
    void lowerCase(){
        m = lower.matcher(line);
        assertTrue(m.find());
    }

    @Test
    void upperCase(){
        m = upper.matcher(line);
        assertTrue(m.find());
    }

    @Test
    void number(){

        m = number.matcher(line);
        assertTrue(m.find());
    }
}
