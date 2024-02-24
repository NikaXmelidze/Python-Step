# vqmnit node class - s, romelsac gadaecema raime monacemi da shemdeg init metodit data cvlads adzlevs am monacemis mnishvnelobas, xolo next cvlads adzelvs none mnishvnelobas, 
#radgan am node is shemdegi wevri tavidan ar vicit
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #gadacemul monacems agdebs nodeshi da amatebs listis bolo wevrad
    def append(self, data):
        new_node = Node(data)

        #tu listshi ar arsebobs monacemi, am listis pirvel monacemad amatebs gadacemul nodes
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        #Tuki listshi iyo aqamde arsebuli monacemi, pirveli node dan miyveba da amowmebs tu mas aqvs shemdegi node, sanam ar miva isettan, romelsac ar aqvs, 
        #mxolod mashin amatebs axal nodes listshi
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    #amatebs gadacemuli monacemis nodes, mititebul indexze
    def insert(self, data, index):
        new_node = Node(data)

        #tu indexi aris 0(anu unda chajdes pirvel poziciaze) axali node is shemdeg monacems adzlevs aqamde arsebuli pivrveli node is mnishvnelobas
        #xolo listis pirvel(head) nodes, adzlevs axali node is mnishvnelobas
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        current_index = 0

        while current_node.next and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        new_node.next = current_node.next
        current_node.next = new_node

    #litshi edzebs gadacemuli monacemis pirvel gamochenas da shemdeg shlis mas listidan
    def remove(self, data):

        #tu listi carielia, mtavrdeba metodi
        if self.head is None:
            return

        #tu gadacemuli monacemi, listis pirvelive wevria, listshi arsebul me2 wevrs svams pirvelis adgilas
        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head

        #iwyebs pirveli nodedan da sanam ar gamochndeba iseti node romlis monacemi gadacemuli monacemis tolia, manamde amowmebs yvela arsebul nodes
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        #rodesac ipovis shesabamis nodes, am nodeis adgilas dgams mis shemdeg indexze mjdom nodes, xolo bolos naxsenebi node is adgilas, washlili nodeisgan 2 indexit shemdeg arsebul nodes svams
        if current_node.next:
            current_node.next = current_node.next.next

    #bechdavs chvens lists
    def display_info(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(2)
linked_list.append(5)
linked_list.append(4)
linked_list.append(4)
linked_list.append(4)
linked_list.append(11)
linked_list.append(25)
linked_list.display_info()
linked_list.insert("Irakli", 3)
linked_list.insert(10.1, 5)
linked_list.display_info()
linked_list.remove("Irakli")
linked_list.remove(4)
linked_list.display_info()


#vqmnit Stack class da shignit vadefinebt metodebs
class Stack:
    #tavidan monacemi ar gvaq, amitom bolo monacemis mnishvneloba iqneba none xolo stackis sigrdze 0
    def __init__(self):
        self.top_node = None
        self.length = 0

    #amowmebs aris tu ara stacki carieli, misi sigrdzis shemowmebit
    def empty(self):
        return self.length == 0

    #gvibrunebs stackis sigrdzes
    def size(self):
        return self.length

    #tu steki araa carieli, abrunebs bolos damatebuli node is mnishvnelobas, xolo tu carielia abrunebs indexerrors da mesijs
    def top(self):
        if not self.empty():
            return self.top_node.data
        else:
            raise IndexError("Stack Is Empty")

    #stekis tavshi amatebs axal nodes node klasis gamoyenebit, shemdeg top_node cvlads adzlevs am axali nodes is mnishvnelobas,
    # xolo mis damatebamde romelic iyo top node imas adzlevs axlis shemdegi node is mnishvnelobas da zrdis stekis sigrdzes 1 it
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top_node
        self.top_node = new_node
        self.length += 1

    #tu steki araa carieli, am stekidan agdebs bolo damatebul nodes da abrunebs mis mnishvnelobas. amistvis amogdebuli monacemis cvlads anichebs bolos damatebuli node is mnishvnelobas
    #shemdeg, stack klasis top_node cvlads anichebs amogdebamde me2 node is mnishvnelobas da amcirebs sigrdzes 1 it 
    def pop(self):
        if not self.empty():
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.length -= 1
            return popped_item
        else:
            raise IndexError("Stack Is Empty")


stack = Stack()
stack.push(1)
stack.push(5)
stack.push(2)
stack.push(8)
stack.push(10)
print(stack.size())
print(stack.pop())
print(stack.size())
print(stack.pop())
print(stack.size())
print(stack.pop())
print(stack.size())
print(stack.pop())
print(stack.size())
print(stack.pop())