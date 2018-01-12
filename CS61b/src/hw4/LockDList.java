package hw4;

public class LockDList extends DList1 {
public void lockNode(DListNode1 node){
	LockDListNode lnode=(LockDListNode)node;
	lnode.status=1;
}
public void removefront(){
	if(size==0){
		head=tail=null;
		size=0;
	}
	else if(size==1){
		LockDListNode lhead=(LockDListNode)head;
		if(lhead.status==1)
			return;
		else{
			head=tail=null;
			size--;
		}
	}
	else{
		
	}
}
}
