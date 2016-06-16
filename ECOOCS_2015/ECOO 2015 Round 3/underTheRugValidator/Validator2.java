import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Validates solution files for the ECOO 2015 provincial finals, problem 4.
 * 
 * Solution must be in a file called "solution.txt" in the same folder
 * as this program.
 * 
 * Requires DATA41.txt, DATA42.txt, targets41.txt and targets42.txt to run
 * as well.
 * 
 * @author Sam Scott (sam.scott@sheridancollege.ca)
 *
 */
public class Validator2 {
 public static int numTCs = 10;

 public static void main(String[] args) throws FileNotFoundException {
  Scanner std = new Scanner(System.in);
  System.out.print("Data Set 1 or 2? ");
  int DATASET = std.nextInt();
  std.close();
  
  Scanner sc_solution = new Scanner(new File("solution.txt"));

  System.out.println("----- START OF PRE-CHECK -----");

  // precheck solutions
  ArrayList<Integer> lines = new ArrayList<Integer>(); // stores the number of ints on each line or -1 if bad formatting
  ArrayList<String[]> raw = new ArrayList<String[]>();
  while(sc_solution.hasNext()) {
   String[] tokens = sc_solution.nextLine().trim().split("\\s+");
   raw.add(tokens);
   try {
    if (tokens[0].length() != 0) {
     for (int i=0; i<tokens.length; i++)
      Integer.parseInt(tokens[i]);
     lines.add(tokens.length);
    } else {
     lines.add(0);
    }
   } catch (Exception e) {
    lines.add(-1);
    System.out.println("Non-integer or blank line found on line "+lines.size());
   }
  }
  sc_solution.close();

  // identify good tcs and their starting points
  int[] testCaseLocations = new int[numTCs];
  for (int i=0; i<numTCs; i++)
   testCaseLocations[i] = -1;

  int current = 0;
  for (int i=0; i<lines.size(); i++) {
   if (lines.get(i) == 1) {
    if (current >= numTCs) {
     testCaseLocations[current-1] = -1;
     System.out.println("Extra Test Cases - Last Test Case Marked as Bad.");
     break;
    }
    testCaseLocations[current] = i;
    current += 1;
    // if too many TCs, consider the last test case bad
   }
  }

  // check each TC has the right number of rugs
  for (int i=0; i<numTCs; i++) {
   if (testCaseLocations[i] != -1) {
    int rugs = Integer.parseInt(raw.get(testCaseLocations[i])[0]);
    if (rugs < 0)
     System.out.println("Negative number of rugs in test case "+(i+1));
    for (int j=0; j<rugs; j++) {
     try {
      if (lines.get(testCaseLocations[i]+j+1) < 0) {
       System.out.println("Non-integer in test case "+(i+1));
       testCaseLocations[i] = -1;
       break;
      } else if (lines.get(testCaseLocations[i]+j+1) == 0) {
       System.out.println("Blank line in test case "+(i+1));
       testCaseLocations[i] = -1;
       break;
      }else if (lines.get(testCaseLocations[i]+j+1) == 1) {
       System.out.println("Fewer rugs than specified in test case "+(i+1));
       testCaseLocations[i] = -1;
       break;
      } else if (lines.get(testCaseLocations[i]+j+1) > 3 || lines.get(testCaseLocations[i]+j+1) == 2) {
       System.out.println("Wrong number of ints on a line in test case "+(i+1));
       testCaseLocations[i] = -1;
       break;
      }
     } catch (IndexOutOfBoundsException e) {
      System.out.println("Fewer rugs than specified in test case "+(i+1));
      testCaseLocations[i] = -1;
     }
    }
    try {
     if (testCaseLocations[i] != -1 && i < numTCs-1 && rugs >= 0 && lines.get(testCaseLocations[i]+rugs+1) != 1 || 
       testCaseLocations[i] != -1 && i == numTCs-1 && testCaseLocations[i]+rugs+1 < raw.size()) {
      System.out.println("Test case "+(i+1)+" has extra stuff after the last rug");
      testCaseLocations[i] = -1;
     }
    } catch (IndexOutOfBoundsException e) {
     // possible exception if too few TCs
    }
   }
  }

  System.out.println("----- END OF PRE-CHECK -----\n");

  System.out.println("----- START OF SCORING -----");
  // score solutions
  Scanner sc_data = new Scanner(new File("DATA4"+DATASET+".txt"));
  Scanner sc_targets = new Scanner(new File("targets4"+DATASET+".txt"));
  int score = 0;
  for (int tc = 0; tc<numTCs; tc++) {
   //GET GRIDS
   String s = sc_data.next();
   char[][] grid = new char[s.length()][];
   char[][] vgrid = new char[s.length()][];
   grid[0] = s.toCharArray();
   vgrid[0] = s.toCharArray();
   for (int i=1; i<grid.length; i++) {
    String line = sc_data.next();
    grid[i] = line.toCharArray();
    vgrid[i] = line.toCharArray();
   }

   // get target
   int target = sc_targets.nextInt();

   // APPLY RUGS
   boolean valid = true;
   int n=0;

   if (testCaseLocations[tc] != -1) {
    try {
     n = Integer.parseInt(raw.get(testCaseLocations[tc])[0]);
    } catch (Exception e) {
     System.out.println("BAD M VALUE: "+raw.get(testCaseLocations[tc])[0]); // shouldn't happen any more
    }
    //   System.out.println(n);

    for (int i=0; i<n; i++) {
     int top=-1, left=-1, size=-1;
     try {
      top = Integer.parseInt(raw.get(testCaseLocations[tc]+i+1)[0]);
      left = Integer.parseInt(raw.get(testCaseLocations[tc]+i+1)[1]);
      size = Integer.parseInt(raw.get(testCaseLocations[tc]+i+1)[2]);
     } catch (java.util.InputMismatchException e) {
      System.out.println("BAD RUG VALUE"); // shouldn't happen any more
      valid = false;
     } catch (Exception e) {
      System.out.println("Something else went wrong"); // also shouldn't happen
      System.out.println(e);
     }

     try {
      // System.out.println(i+" "+top+" "+left+" "+size);
      for (int r=top; r<top+size; r++) {
       for (int c=left; c<left+size; c++) {
        vgrid[r][c] = 'R';
       }
      }
     } catch (java.util.InputMismatchException e) {
      System.out.println("BAD RUG VALUE"); // shouldn't happen any more
      valid = false;
     } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("BAD RUG: "+top+" "+left+" "+size);
      valid = false;
     }
    }
    for (int r=0; r<grid.length; r++) {
     for (int c=0; c<grid.length; c++) {
      if (vgrid[r][c] == 'R' && grid[r][c] != '*') {
       valid = false;
      }
      if (vgrid[r][c] == '*') {
       valid = false;
      }
     }
    }
   } else
    valid = false;

   if (valid) {
    System.out.println("TC "+(tc+1)+" solution is valid:  5 points");
    score += 5;
    int scoreinc = n / 10;
    System.out.println("Solution: "+n+" rugs, Target: "+target+" rugs");
    if (n <= target) {
     System.out.println("Extra points: 5");
     score += 5;
    } else if (n <= target + scoreinc) {
     System.out.println("Extra points: 4");
     score += 4;

    } else if (n <= target + scoreinc*2) {
     System.out.println("Extra points: 3");
     score += 3;

    } else if (n <= target + scoreinc*3) {
     System.out.println("Extra points: 2");
     score += 2;

    } else if (n <= target + scoreinc*4) {
     System.out.println("Extra points: 1");
     score += 1;

    } else {
     System.out.println("Extra points: 0");     
    }
   }
   else
    System.out.println("**** TC "+(tc+1)+" solution is NOT valid");   
   System.out.println();
  }
  if (DATASET == 1 && score == 100) {
   System.out.println("BONUS: 10");
   score += 10;
  }
  System.out.println("FINAL SCORE: "+score);
  System.out.println("----- END OF SCORING -----");

  sc_data.close();
  sc_targets.close();
 }
}
