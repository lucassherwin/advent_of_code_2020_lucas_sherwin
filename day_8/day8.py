with open('input.txt', 'r') as file:
    input_lines = file.readlines()

# node class for linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        
    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
        
# Function to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None

# Print the linked list
    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next

    def SearchLList(self, val):
        current = self.head

        while current != None:
            if current.data == val:
                print(current.data)
                return True
            current = current.next
        print('Not found')
        return False

llist = SLinkedList()
# llist.Atbegining("Mon")
# llist.Atbegining("Tue")
# llist.Atbegining("Wed")
# llist.Atbegining("Thu")
# llist.RemoveNode("Tue")
# llist.LListprint()

# create the list
def create_list_from_input(input):
    for i in input:
        # split up input
        i = i.strip().split()
        # obj: {key(instruction): value(argument)}
        inst = i[0]
        arg = i[1]
        inst_obj = {inst: arg}
        # add obj to lined list
        llist.Atbegining(inst_obj)

create_list_from_input(input_lines)
# llist.LListprint()
llist.SearchLList({'acc': '-2'})
# instruction set:
# acc: increase or decrease value in accumulator
    # EX: acc +7 increase acc by 7
    # after an acc instruction, the instruction immediately below is exectued
# jmp: jumps to a new input relative to itself
    # EX: jmp +2 skip the next instruction
    # EX: jmp +1 continue to the instruction immediately below it
    # EX: jmp -20 execute the instruction 20 lines above
# nop: no operation -- does nothing
    # the instruction immediately below it is exectued next