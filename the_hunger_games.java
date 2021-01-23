/**  
 * The Hunger Games: Catching Fire
 * 01:52:31 
 * 
 * Potential sources:
 *    - https://stackoverflow.com/questions/10560295/compiling-and-running-java-code-in-sublime-text-2/13488448#13488448
 *    - https://docs.oracle.com/javase/8/docs/api/java/text/BreakIterator.html
 *
 * Recovered snippets are from top to bottom.
 */
 
// ------------------------------------------------
{
    "cmd": ["javac", "-Xlint", "$file"],
    "file_regex": "^(...*?):([0-9]*):?([0-9]*)",
    "selector": "source.java",
    "variants": [
        { "cmd": ["javac", "-Xlint", "$file"],
          "file_regex": "^(...*?):([0-9]*):?([0-9]*)",
          "selector": "source.java",
          "name": "Java Lintter"
        },  
        { "cmd": ["java", "$file_base_name"],
          "name": "Run Java"
        }
    ]
}

// ------------------------------------------------
 public static void main(String args[]) {
      if (args.length == 1) {
          String stringToExamine = args[0];
          //print each word in order
          BreakIterator boundary = BreakIterator.getWordInstance();
          boundary.setText(stringToExamine);
          printEachForward(boundary, stringToExamine);
          //print each sentence in reverse order
          boundary = BreakIterator.getSentenceInstance(Locale.US);
          boundary.setText(stringToExamine);
          printEachBackward(boundary, stringToExamine);
          printFirst(boundary, stringToExamine);
          printLast(boundary, stringToExamine);
      }
 }

// ------------------------------------------------
 public static void printEachBackward(BreakIterator boundary, String source) {
     int end = boundary.last();
     for (int start = boundary.previous();
          start != BreakIterator.DONE;
          end = start, start = boundary.previous()) {
         System.out.println(source.substring(start,end));
     }
 }
