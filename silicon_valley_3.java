/*
	Silicon Valley  -  s06e04 10:51
*/


int index = 0;
while (!element.equals(sortedList.get(index))
	&& sortedList.size() > ++index);
return index < sortedList.size() ? index : -1;
