package module02;

// Here is a class that calculate student loan based on their gpa. It extends the StudentData Class
public class FindGradeLetter extends StudentData {

    public String gradeLetter(double gpa) {
        String gradLetter = " ";
        if (gpa >= 3.7 && gpa <= 4.0)
            gradLetter = "A";
        else if ( gpa >= 2.7 && gpa <= 3.6){
            gradLetter = "B";
            System.out.println();
        }
        else if (gpa >= 1.7 && gpa <= 2.6){
            gradLetter = "C";
            System.out.println();
        }
        else if (gpa >= 0.7 && gpa <= 1.6){
            gradLetter = "D";
            System.out.println();
        }
        else{
            gradLetter = "F";
            System.out.println();
        }
           
        return gradLetter;

    }

    public void schoolDecision(String gradLetter){
        switch (gradLetter) {
            case "B":
                System.out.println("student demostrate a Considerable Understanding");
                break;
            case "C":
                System.out.println("Student demonstrates a Sufficient Understanding");
                break;
            case "D":
                System.out.println("student demostrate a Poor Understanding");
                break;
            case "F":
                System.out.println("Student fails the class");
                break;
            case "A":
                System.out.println("Student demonstrates an Outstanding Understanding");
                break;
            default:
                System.out.println("Error: letter does not match");
        }

    }

    
}


