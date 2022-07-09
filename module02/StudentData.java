package module02;


import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class StudentData {

    private Connection connect() {
        // SQLite connection string
        String url = "jdbc:sqlite:C:/Users/HP/Desktop/Spring_Semester_2022/Applied_Programming-1/module01/student.db";
        Connection conn = null;
        try {
            conn = DriverManager.getConnection(url);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return conn;
    }

    
    /**
     * select all rows in the warehouses table
     */
    public void selectAll(){
        String sql = "SELECT std.id, std.fname, std.lname, sgpa.GPA  FROM student_info std INNER JOIN student_gpa sgpa ON std.id = sgpa.id";
        
        try (Connection conn = this.connect();
             Statement stmt  = conn.createStatement();
             ResultSet rs    = stmt.executeQuery(sql)){
            
            // loop through the result set
            while (rs.next()) {
                System.out.println(rs.getInt("id") +  "\t" + 
                                   rs.getString("fname") + "\t" +
                                   rs.getString("lname")+ "\t" +
                                   rs.getDouble("GPA")) ;
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
    
    public static void main(String[] args) {
        StudentData  app = new StudentData ();
        app.selectAll();
    }
    
}
