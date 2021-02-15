# The Social Network - 11:49

#!/usr/bin/perl

$wget = "wget -qO- http://bolson:50368410\@www.lowell.harvard.edu/FaceBook/index.html"
$pagenum = 1;
while (true) {
  print "Page $pagenum\n";

  print "$wget\n";
  $page = ` $wget`;

  $page_copy = $page;
  print $page;
  while ($page =~ m/female\/([0-9]+\.jpg/g) {
      $image = $1;
      print "Female! Image: $image\n";
      $wget="wget -qO- facemash/photos/$image --limit-rate=300000 http://bolson:50368410\@www.lowell.harvard.edu/FaceBook/photos/female/$image";
      print "$wget \n" ;
      system($wget);
}
 
