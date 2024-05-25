class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None

class Singly:
    def __init__(self):
        self.head=None
    def create(self):
        temp=Node()
        temp=self.head
        val=int(input("Enter value: "))
        l1=Node(val)
        if self.head is None:
            self.head=l1
        else:
            while(temp.next!=None):
                temp=temp.next
            temp.next=l1
    def display(self):
        temp=Node()
        temp=self.head
        if(self.head==None):
            print("No elements found")
        else:
            while(temp!=None):
                print(temp.val,end=" ")
                temp=temp.next
            print("\n")
    def addinthebeig(self):
        val=int(input("Enter value: "))
        l1=Node(val)
        if self.head is None:
            self.head=l1
        else:
            l1.next=self.head
            self.head=l1
    def addintheend(self):
        val=int(input("Enter value: "))
        l1=Node(val)
        temp=self.head
        if self.head is None:
            self.head=l1
        else:
            while(temp.next!=None):
                temp=temp.next
            temp.next=l1
    def addatanypos(self):
        pos=int(input("Enter position to be added: "))
        count=l.countnodes()
        if self.head is None:
            val=int(input("Enter value:"))
            l1=Node(val)
            self.head=l1
        elif(pos<=count+1):
            if(pos==1):
                l.addinthebeig()
            elif(pos==count+1):
                l.addintheend()
            else:
                val=int(input("Enter value:"))
                l1=Node(val)
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                l1.next=temp.next
                temp.next=l1
        else:
            print("Enter correct position")

    def delfromthebeig(self):
        if self.head is None:
            print("NOTHING TO DELETE")
        else:
            self.head=self.head.next
            print("Successfully deleted")
            print("Nodes are: ")
            l.display()
    def delfromtheend(self):
        temp=self.head
        if self.head is None:
            print("NOTHING TO DELETE")
        else:
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
            print("Successfully deleted")
            print("Nodes are: ")
            l.display()
    def delfromanypos(self):
        pos=int(input("Enter position to be added: "))
        count=l.countnodes()
        if self.head is None:
            print("NOTHING TO DELETE")
        elif(pos<=count+1):
            if(pos==1):
                l.delfromthebeig()
            elif(pos==count+1):
                l.delfromtheend()
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                temp.next=temp.next.next
                print("successfully deleted")
        else:
            print("Enter correct position")

    def countnodes(self):
        b=0
        temp=self.head
        if self.head is None:
            return b
        else:
            while(temp!=None):
                b+=1
                temp=temp.next
            return b
    
if __name__ == "__main__": 
    l=Singly()
    while(True): 
        print("1. Creation of node")
        print("2. display of node")
        print("3. Add in the beginning")
        print("4. Add at the end")
        print("5. add at any pos")
        print("6. Delete from the beginning")
        print("7. delete from the end")
        print("8. Delete from any position")
        print("9. Number of nodes")
        print("10. exit")
        ch=int(input("Enter choice: "))
        if(ch==1):
            n=int(input("Enter number of elemnts to be added: "))
            for i in range(n):
                l.create()
        elif(ch==2):
            l.display()
        elif(ch==3):
            l.addinthebeig()
        elif(ch==4):
            l.addintheend()
        elif(ch==5):
            l.addatanypos()
        elif(ch==6):
            l.delfromthebeig()
        elif(ch==7):
            l.delfromtheend()
        elif(ch==8):
            l.delfromanypos()
        elif(ch==9):
            a=l.countnodes()
            print("No. of nodes are: ",a)
        elif(ch==10):
            print("EXITING PROGRAM")
            break
        else:
            print("Enter correct choice")


        