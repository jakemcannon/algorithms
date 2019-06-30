## Reverse a Singly Linked List



### Erros

- A simple mistake but I forgot to check what class methods were available like <code>.getNext() or .setNext()</code>
- <code>cur = head</code> shoule be <code>cur = **self**.head</code>,  I forgot the **self**. I haven't worked with Python OOP nearly as much as I have with Java so that might be an issue (Maybe make a blog post about this to clear it up). So I did get an error there with the debugger, something about bounding or unbounded.
- It looks like I had my <code>before and after</code> varaibles mixed up. Also, I might have had an extra variable. I'm not entirelly sure what firecode's <code>next</code> varaible is and why it is using a Python *keyword*…. But, essentially it looks like they had the equivilant of my <code>after</code> variable but it was inside the while loop. 
- Also my while checked for a condition on my <code>after</code> variable while theres checks for a condition on the current node.



**My iterative solution**

```python
class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    def reverse(self):
        before = None
        cur = head
        after = head.next
        
        while after is not None:
            before = cur
            cur = after
            head = after
            
            cur.next = after.next
            after.next = before
            after = cur.next
```



**Firecode iterative solution**

```python
class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
        
    def reverse(self):
      last = None
      current = self.head
      
      while(current is not None):
        next = current.getNext()
        current.setNext(last)
        last = current
        current = next
        
     self.head = last
      
```





**Recursive solution**



```

```

