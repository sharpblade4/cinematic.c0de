/*
  Grey's Anatomy - s10e11 00:07
   
  Source: https://www.cs.uic.edu/~sloan/CLASSES/java/KeyboardReaderError.java

*/

    /* Following line triggers the error.  Error will show the type of
       unhandled exception and where the call occurs */
    s1 = br.readLine();

    System.out.println ("The line has " + s1.length() + " characters");

    System.out.println ();
    System.out.println ("Breaking the line into tokens we get:");

    int numTokens = 0;
    StringTokenizer st = new StringTokenizer (s1);

    while (st.hasMoreTokens()) {
	s2 = st.nextToken();
	numTokens++;
	System.out.println ("    Token " + numTokens + " is: " + s2);
    }
  }
}
