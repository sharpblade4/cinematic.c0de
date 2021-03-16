/**
  Mr. Robot  -  s02e03 57:01
  
  Potential source:
    - https://www.modules.napier.ac.uk/Module.aspx?ID=set07109
*/

void StackLinkedList::push(NODE *n)
{
    if (front == NULL)
    {
        front = n;
        back = n;
    }
    else {
        front->P = n;
        n->N = front; 
        front = n; 
  }
}

NODE* StackLinkedList::pop()
{
    NODE *temp;   
    if (front == NULL )//no nodes
        return NULL; 
    else if (back->P == NULL)//there is only one node
    {
        NODE * temp2 = front; 
        	temp = temp2;
	        front = NULL;
	        delete temp2;
	        return temp;
    }
    else//there are more than one node
    {
        NODE *temp2 = front;
	        temp = temp2; 
	        front = front->P;
	        front->N = NULL;
	        delete temp2;
	        return temp;
    }
}

void StackLinkedList::destroyList()
{
    while(front != NULL) 
    {
        NODE *temp = front; 
        front = front->N;
        delete temp; 
    }
}
