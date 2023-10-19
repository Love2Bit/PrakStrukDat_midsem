class Node:
    def __init__(self, element, n):
        self._element = element
        self._next = n

class Stack: #SLLNC dengan head
    def __init__(self):
        self._head=None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def push(self,e): #sama dengan tambah depan
        baru = Node(e, None)
        if self.isEmpty()==True:
            self._head = baru
            self._tail = baru
            self._tail._next = None
        else:
            baru._next = self._head
            self._head = baru
        self._size += 1
        #print("Data masuk ke stack!")

    def top(self): #tampilkan data di head
        if self.isEmpty == True:
            return "Stack kosong!"
        else:
            return self._head._element

    def pop(self): #hapus depan
        if self.isEmpty()==False:
            d = ""
            if self._head._next==None:
                d = self._head._element
                self._head=None
            else:
                hapus = self._head
                d = hapus._element
                self._head = self._head._next
                hapus._next=None
                del hapus
            self._size -= 1
            #print(d," dihapus!")
        else:
            print("Stack kosong!")
        return d

    def printAll(self): #loop
        if self.isEmpty()==False:
            bantu = self._head
            helper = []
            while(bantu!=None):
                helper.append(bantu._element)
                bantu = bantu._next
            print("isi: ",*helper[::-1], sep=" ")
        else:
            print("Kosong")


if __name__ == "__main__":
    st = Stack()
    start = 0
    while start != 10:
        angka = int(input("Masukkan angka : "))
        masukan = []
        for i in range(len(st)):
            masukan.append(st.pop())
        if angka in masukan:
            masukan.insert(masukan.index(angka), angka)
        else:
            masukan.insert(0, angka)
        for j in range(len(masukan)):
            st.push(masukan.pop())
        start += 1
        st.printAll()