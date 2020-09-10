public class Strings_Refresh {


    //Write a Java program to get the character at the given index within the String.
    public void GivenIndex()
    {
        String str = "Java Exercises!";
        System.out.print("Exercise 1: \nThe character at positions 0 is " + str.charAt(0) + '\n' +
                "The character at position 10 is " + str.charAt(10));

    }

    //Write a Java program to get the character (Unicode code point) at the given index within the String.
    public void UnicodeCodePoint()
    {
        String str = "w3resource.com";
        System.out.println("\n\nExercise 2:\nCharacter (unicode point) = " + str.codePointAt(0) + "\n") ;
    }

    //Write a java program to compare two strings lexicographically.
    public void Lexicocompare()
    {
        String str1 = "This is String 1";
        String str2 = "This is String 2";

        int result = str1.compareTo(str2);

        System.out.println("Exercise 3:");
        if(result > 0)
        {
            System.out.println("String 1 is greater than String 2");

        } else if(result < 0)
        {
            System.out.println("String 1 is less than String 2");
        } else
        {
            System.out.println("String 1 is equal to String 2");
        }

    }





    public static void main(String args[])
    {
       Strings_Refresh sr = new Strings_Refresh();
       sr.GivenIndex();
sr.UnicodeCodePoint();
sr.Lexicocompare();

        //https://www.w3resource.com/java-exercises/string/index.php
    }
}
