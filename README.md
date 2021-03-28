Tema 1 Marketplace
334CC Sima Nicoleta-Lavinia

Am ales o solutie care foloseste lock-uri pentru generarea id-ului si pentru cazurile in care exista mai multe operatii de adaugare, stergere si atribuire din dictionar in zona de cod. 

Am folosit structuri de date de tip dictionar cu valori ca liste pentru a retine produsele pentru fiecare producator si produsele care se afla in fiecare cart: self.products_dict = {} si self.carts = {}. De asemenea, dictionarul reserved = {} are drept cheie produsul nou adaugat in cart-ul consumatorului si drept valoarea producatorul caruia apartine pentru a sti de unde l-am luat in cazul in care consumatorul apeleaza remove. Am folosit lock-uri in cazul functiilor new_cart si regiser_producer deoarece operatie de incrementare a id-ului nu este atomica.In cazul functiei de publish operatia de append pe liste este thread safe si de aceea nu am folost niciun alt element de sincronizare. Pentru functiile add_to_cart si remove_from_cart am adaugat lock-uri deoarece aveam atat operatii de append, remove si atribuiri si am considerat ca sunt necesare pentru a asigura sincronizarea si a pastra ideea ca un singur thread are acces la acea zona de cod la un moment dat. Am adaugat comentarii in cod care sunt relevante pentru intelegerea codului.
Am implementat toate cerintele din enunt. Cu aceasta tema am parofundat mai bine structurile de date in python si cateva dintre elementele de sincronizare. Dificulatati am avut in intelegerea enuntului in prima faza.

Surse: https://ocw.cs.pub.ro/courses/asc/laboratoare/01
       https://ocw.cs.pub.ro/courses/asc/laboratoare/02
       https://docs.python.org/3/tutorial/datastructures.html
       
