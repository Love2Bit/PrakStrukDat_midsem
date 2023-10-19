class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        node_baru = Node(data)
        if not self.head:
            self.head = node_baru
        else:
            node_sekarang = self.head
            while node_sekarang.next:
                node_sekarang = node_sekarang.next
            node_sekarang.next = node_baru

    def get_index(self, index):
        node_sekarang = self.head
        count = 0
        while node_sekarang:
            if count == index:
                return node_sekarang.data
            count += 1
            node_sekarang = node_sekarang.next
        return None
    
if __name__ == "__main__":
    LinkedList = LinkedList()

    kata_kata = input("Masukkan kata-kata: ").split()
    for kata in kata_kata:
        LinkedList.insert(kata)
    no_urut = input("Masukkan no urut: ").split()
    hasil = []
    for urut in no_urut:
        index = int(urut) - 1
        kata = LinkedList.get_index(index)
        if kata:
            hasil.append(kata)
    print("Hasil:", " ".join(hasil))