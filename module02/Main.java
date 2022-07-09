package module02;

import java.util.Scanner;
// create a class named main whose purpose is to run all our program. It extends StudentData class
public class Main {

    public static void main(String[] args) {
        //create an instance of FindGradeLetter class called letter
        FindGradeLetter letter = new FindGradeLetter();
        // FinderGraeLetter class is a sub class of StudentData class. So it calls all methods in StudentData class
        letter.selectAll();
        System.out.println("");
        // create a scanner object
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please enter a student gpa please: ");
        Double y = scanner.nextDouble();
        var x = letter.gradeLetter(y);
        System.out.println("Student Grade Letter is: "+ x);
        letter.schoolDecision(x);
        scanner.close();
        System.out.println("");
        System.out.println("++++++++++Thanks++++++++++++");

    }
    
}
