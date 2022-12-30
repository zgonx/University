#!/usr/bin/env python
# coding: utf-8

# ## IS 2020 Algorytmy i programowanie
# ### Praca domowa 8 [100 pkt]
# 
# ### Programowanie obiektowe - dziedziczenie
# ### IS 2020 Algorytmy i programowanie - Dekoratory

# 
# 

# In[ ]:





# In[ ]:





# ### Zadanie 1 [30]
# 
# Napisz funkcję określającą czy (i ile) funkcja kwadratowa $f(x)=ax^2+bx+c$ ma miejsc zerowych. Napisz następujące dekoratory
# 
# >  uzupełnjający w/w funkjce o wyznaczenie sumy i iloczynu pierwastków funkcji kwatratowej (wzory Viete'a).
# 
# >  wyznaczający współrzędne wierzchołka.
# 
# >  który wypisuje wynik funkcji tylko w godzinach 8-15, w innnych godzinach wypisuje informację ,,Teraz mam przerwę". 
# 
# > wyznaczjący wartość wielomaniu w punkcie $x+3$
# 
# > wyznaczjący wartość bezwzględną otrzymanego wyniku czyli wyznaczjący wartość $\mid W(x)\mid$.
# 
# >  zaproponuj własny dekorator.
# 

# In[48]:


#A
def quadfunc(func):
    
    if len(func)!=3:
        
        raise ValueError("Funkcja musi posiadac 3 argumenty")
    
    a = func[0]
    b = func[1]
    c = func[2]
    
    delta = (b**2) - (4*a*c)
    
    if delta < 0:
        
        return "0"

    if delta == 0:
        
        return "1"
    
    else:
        
        return "2"
        
        
    

print(quadfunc([2,7,3]))


# In[60]:


#B
import math

def dekor(funkcja):
    
    def wrap(func):
        
        if funkcja(func) == "2":
            
            suma = -(func[1]/func[0])
            iloczyn = (func[2]/func[0])
            
            return (f"suma = {suma}, iloczyn = {iloczyn}")
        else:
            return f" Funkcja ma {funkcja(func)} miejsce zerowe"
    
    return wrap

@dekor
def quadfunc(func):
    
    if len(func)!=3:
        
        raise ValueError("Funkcja musi posiadac 3 argumenty")
    
    a = func[0]
    b = func[1]
    c = func[2]
    
    delta = (b**2) - (4*a*c)
    
    if delta < 0:
        
        return "0"

    if delta == 0:
        
        return "1"
    
    else:
        
        return "2"
        
        
    

print(quadfunc([2,7,3]))
    


# In[64]:


#C
import math

def dekor(funkcja):
    
    def wrap(func):
            
            p = - func[1] / (2*func[0])
            delta = ((func[1]**2) - (4*func[0]*func[2])) #????
            q = - delta / (4*func[0])
            
            return (f"wspolrzedne wierzcholka = {p,q}")
    
    return wrap

@dekor
def quadfunc(func):
    
    if len(func)!=3:
        
        raise ValueError("Funkcja musi posiadac 3 argumenty")
    
    a = func[0]
    b = func[1]
    c = func[2]
    
    delta = (b**2) - (4*a*c)
    
    if delta < 0:
        
        return "0"

    if delta == 0:
        
        return "1"
    
    else:
        
        return "2"
        
        
    

print(quadfunc([2,7,3]))
    


# In[20]:


#D
import math
import time

def dekor(f):
    
    def wrap(x):
            
        date = time.localtime()
        hour = date.tm_hour
            
        if hour < 8 and hour > 15:
            return (f(x))
        
        else:
            return "Teraz mam przerwę"
    
    return wrap

@dekor
def quadfunc(func):
    
    if len(func)!=3:
        
        raise ValueError("Funkcja musi posiadac 3 argumenty")
    
    a = func[0]
    b = func[1]
    c = func[2]
    
    delta = (b**2) - (4*a*c)
    
    if delta < 0:
        
        return "0"

    if delta == 0:
        
        return "1"
    
    else:
        
        return "2"
        
        
    

print(quadfunc([2,7,3]))
    


# In[15]:


#F
import math

def dekor(funkcja):
    
    def zero(func):
        
        if funkcja(func) == "0":
            
            return ("Brak miejsc zerowych")
        
        else:
            delta = ((func[1]**2) - (4*func[0]*func[2]))
            
            if funkcja(func) == "1":
                
                zero = -func[1]/(2*func[0])
                return f"Miejsce zerowe to x = {zero}"
            
            else:
                
                zero1 = (-func[1]-math.sqrt(delta))/(2*func[0])
                zero2 = ((-func[1]+math.sqrt(delta))/(2*func[0]))
                return f"Miejsca zerowe to x1 = {zero1}, x2 = {zero2}"
    
    return zero

@dekor
def quadfunc(func):
    
    if len(func)!=3:
        
        raise ValueError("Funkcja musi posiadac 3 argumenty")
    
    a = func[0]
    b = func[1]
    c = func[2]
    
    delta = (b**2) - (4*a*c)
    
    if delta < 0:
        
        return "0"

    if delta == 0:
        
        return "1"
    
    else:
        
        return "2"
        
        
    

print(quadfunc([1,2,1]))
    


# ### Zadanie 2 [30]
# Napisz klasy dekorujące do zaania 1. 

# In[2]:


#B
import math

class dekorklasa:
    def __init__(self,fun):
        #print("init"+str(fun))
        self.fun=fun
    def __call__(self,x):
        suma = -(x[1]/x[0])
        iloczyn = (x[2]/x[0])
        return (f"suma = {suma}, iloczyn = {iloczyn}")


@dekorklasa
def quadfunc(func):
    
    if len(func)!=3:
        
        raise ValueError("Funkcja musi posiadac 3 argumenty")
    
    a = func[0]
    b = func[1]
    c = func[2]
    
    delta = (b**2) - (4*a*c)
    
    if delta < 0:
        
        return "0"

    if delta == 0:
        
        return "1"
    
    else:
        
        return "2"
        
print(quadfunc([2,7,3]))


# In[5]:


#C
import math

class dekorklasa:
    def __init__(self,fun):
        #print("init"+str(fun))
        self.fun=fun
    def __call__(self,x):
        if self.fun(x)=="2":
            p = - x[1] / (2*x[0])
            delta = ((x[1]**2) - (4*x[0]*x[2])) #????
            q = - delta / (4*x[0])   
            return (f"wspolrzedne wierzcholka = {p,q}")
    

@dekorklasa
def quadfunc(func):
    
    if len(func)!=3:
        
        raise ValueError("Funkcja musi posiadac 3 argumenty")
    
    a = func[0]
    b = func[1]
    c = func[2]
    
    delta = (b**2) - (4*a*c)
    
    if delta < 0:
        
        return "0"

    if delta == 0:
        
        return "1"
    
    else:
        
        return "2"
        
        
    

print(quadfunc([2,7,3]))
    


# In[24]:


#D
import math
import time



class dekorklasa:
    def __init__(self,fun):
        #print("init"+str(fun))
        self.fun=fun
    def __call__(self,x):
        date = time.localtime()
        hour = date.tm_hour
        print(hour)
        if hour > 8 and hour < 16:
            return self.fun(x)
        else:
            return "Teraz mam przerwę"

@dekorklasa
def quadfunc(func):
    
    if len(func)!=3:
        
        raise ValueError("Funkcja musi posiadac 3 argumenty")
    
    a = func[0]
    b = func[1]
    c = func[2]
    
    delta = (b**2) - (4*a*c)
    
    if delta < 0:
        
        return "0"

    if delta == 0:
        
        return "1"
    
    else:
        
        return "2"
        
        
    

print(quadfunc([2,7,3]))
    


# In[26]:


#F
import math

def dekor(funkcja):
    
    def zero(func):
        
        if self.fun(x) == "0":
            
            return ("Brak miejsc zerowych")
        
        else:
            delta = ((x[1]**2) - (4*x[0]*x[2]))
            
            if self.fun(x) == "1":
                
                zero = -x[1]/(2*x[0])
                return f"Miejsce zerowe to x = {zero}"
            
            else:
                
                zero1 = (-x[1]-math.sqrt(delta))/(2*x[0])
                zero2 = ((-x[1]+math.sqrt(delta))/(2*x[0]))
                return f"Miejsca zerowe to x1 = {zero1}, x2 = {zero2}"
    
    return zero

class dekorklasa:
    def __init__(self,fun):
        #print("init"+str(fun))
        self.fun=fun
    def __call__(self,x):
        if self.fun(x) == "0":
            
            return ("Brak miejsc zerowych")
        
        else:
            delta = ((x[1]**2) - (4*x[0]*x[2]))
            
            if self.fun(x) == "1":
                zero = -x[1]/(2*x[0])
                
                return f"Miejsce zerowe to x = {zero}"
            
            else:
                zero1 = (-x[1]-math.sqrt(delta))/(2*x[0])
                zero2 = ((-x[1]+math.sqrt(delta))/(2*x[0]))
                
                return f"Miejsca zerowe to x1 = {zero1}, x2 = {zero2}"
@dekorklasa
def quadfunc(func):
    
    if len(func)!=3:
        
        raise ValueError("Funkcja musi posiadac 3 argumenty")
    
    a = func[0]
    b = func[1]
    c = func[2]
    
    delta = (b**2) - (4*a*c)
    
    if delta < 0:
        
        return "0"

    if delta == 0:
        
        return "1"
    
    else:
        
        return "2"
        
        
    

print(quadfunc([1,2,1]))
    


# ### Zadanie 3 [20]
# Przeanalizuj poniższy docstring. Dopisz brakujące w nim fragmenty. 
# Npaisz analogiczny docstring dla funkcji z zadania 1.

# In[ ]:


#bez zadania 3

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.
    WE: 
    WY:
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
    ...
    ValueError: n must be >= 0
    >>> factorial(30.1)
    Traceback (most recent call last):
    ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000
    >>> factorial(1e100)
    Traceback (most recent call last):
    ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


factorial(1)


# In[ ]:


import doctest
doctest.testmod()


# In[ ]:





# In[ ]:





# ### Zadanie 4 [20]
# Klasę  robot uzupełnij o settry i gettery z wykorzystaniem dekoratorów (pamiętaj sprawdzać czy dana wartość jest poprawną wartością pod wzgledem typu i "innych" wymagań klasy).
# 

# In[1]:



class Robot():
    """
      Obiekt robot - obsługa robota
      
      Args:
          nazwa = (str)
          start = (krotka)
          miejsce = (lista)
          moc = (int)
      Attributes:
          nazwa - nazwa robota
          start - wspolrzedne punktu startowego, domyslnie (0,0)
          miejsce - wspolrzedne punktu w ktorym znajduje sie robot
          moc - ilosc energii ktora posiada robot domyślnie  9
      """
    def __init__(self,nazwa,start=(0,0),miejsce=[],moc=9):
        self._nazwa = nazwa
        self._start = start
        self._miejsce = miejsce
        self._moc = moc
    @property    
    def nazwa(self):
            return self._nazwa
    @property
    def start(self):
            return self._start
    @property
    def miejsce(self):
            return self._miejsce
    @property
    def moc(self):
            return self._moc
        
    @nazwa.setter
    def nazwa(self,k):
        if isinstance(k, str):
            self._nazwa = k
        else:
            raise TypeError("Nazwa powinna być str")
    @start.setter
    def start(self,k):
        if isinstance(k, (int,int)):
            self._start = k
        else:
            raise TypeError("Start powinien być krotką")
    @miejsce.setter
    def miejsce(self,k):
        if isinstance(k, [int,int]):
            self._miejsce = k
        else:
            raise TypeError("Miejsce powinno być listą")
    @moc.setter
    def moc(self,k):
        if isinstance(k, int) and k > 0:
            self._moc = k
        else:
            raise TypeError("Moc powinna być int lub jest mniejsza lub rowna 0")
    @nazwa.deleter
    def nazwa(self):
        del self._nazwa
        raise AttributeError("brak nazwy")
    @start.deleter
    def start(self):
        del self._start
        raise AttributeError("brak startu")
    @miejsce.deleter
    def miejsce(self):
        del self._miejsce
        raise AttributeError("brak miejsca")
    @moc.deleter
    def moc(self):
        del self._moc
        raise AttributeError("brak mocy")

    def __str__(self):
        return f'Nazwa: {self.nazwa} \nPozycja: {self.miejsce} \nIlość energii: {self.moc}'
        
    def up(self,arg=1):
        self.moc -= arg
        if self.moc <= 0:
            self.moc = 0
            return "nie wystarczająca moc"
        if self.miejsce == []:
            lista=[]
            lista.append(self.start[0])
            lista.append(self.start[1])
            print(lista)
            self.miejsce = lista
            self.miejsce[1] += arg
            if self.miejsce[1] == 8:
                self.moc += 1
            if self.miejsce[1] > 8:
                self.miejsce[1] = 0
                return "Poruszylem sie w gore"
            return "Poruszylem sie w gore"
        else:
            self.miejsce[1] += arg
            if self.miejsce[1] == 8:
                self.moc += 1
            if self.miejsce[1] > 8:
                self.miejsce[1] = self.miejsce[1] - 8
                return "Poruszylem sie w gore"
            return "Poruszylem sie w gore"
        
    def right(self,arg=1):
        self.moc -= arg
        if self.moc <= 0:
            self.moc = 0
            return "nie wystarczająca moc"
        if self.miejsce == []:
            lista=[]
            lista.append(self.start[0])
            lista.append(self.start[1])
            print(lista)
            self.miejsce = lista
            self.miejsce[0] += arg
            if self.miejsce[1] == 8:
                self.moc += 1
            if self.miejsce[0] > 8:
                self.miejsce[0] = 0
                return "Poruszyłem się w prawo"
            return "Poruszylem sie w prawo"
        else:
            self.miejsce[0] += arg
            if self.miejsce[1] == 8:
                self.moc += 1
            if self.miejsce[0] > 8:
                self.miejsce[0] = self.miejsce[0] - 8
                return "Poruszyłem się w prawo"
            return "Poruszylem sie w prawo"  
    def sprawdz_moc(self):
        if self.moc <= 0 :
            raise ValueError("Zbyt mała moc")
        else:
            return f"Moc wynosi : {self.moc}"
        
robot1=Robot("test",(1,1),[],15)
robot1.nazwa = "k"
print(robot1)
del robot1.moc
print(robot1) 


# In[2]:


class Osoba:
    def __init__(self, imie, nazwisko, adres):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
    @property    
    def imie(self):
            return self._imie
    @property    
    def nazwisko(self):
            return self._nazwisko
    @property    
    def adres(self):
            return self._adres
    @imie.setter
    def imie(self,k):
        if isinstance(k, str):
            self._imie = k
        else:
            raise TypeError("Imie powinno być str")
    @nazwisko.setter
    def nazwisko(self,k):
        if isinstance(k, str):
            self._nazwisko = k
        else:
            raise TypeError("Nazwisko powinno być str")
    @adres.setter
    def adres(self,k):
        if isinstance(k, str):
            self._adres = k
        else:
            raise TypeError("Adres powinien być str")
    @imie.deleter
    def imie(self):
        del self._imie
        raise AttributeError("brak imienia")
    @nazwisko.deleter
    def nawzisko(self):
        del self._nazwisko
        raise AttributeError("brak nazwiska")
    @adres.deleter
    def adres(self):
        del self._adres
        raise AttributeError("brak adresu")
        
        
osoba1=Osoba("Jan","Kowalski","Katowice")
osoba1.imie="Kamil"
print(osoba1.imie)
del osoba1.imie
print(osoba1.imie)

    
    


# In[336]:


# trefl > pik > kier > karo
import random

class Karta:
    
    liczby = [str(el) for el in range(2,15)]
    
    kolory = ["karo","kier","trefl","pik"]
    
    def __init__(self, liczba, kolor):
        self.liczba = liczba
        self.kolor = kolor
    def __str__(self):
        return self.liczba+self.kolor
    
class Gracz:
    def __init__(self, ID_G, nazwa, karta=[["pusto","pusto"]]):
        self.nazwa = nazwa
        self.karta = karta
        self.ID_G = ID_G
    def __str__(self):
        return self.nazwa+" "+str(self.karta[0][0])+" "+self.karta[0][1]+" "+str(self.ID_G)

class Rozgrywka:
    def __init__(self, ilosc_graczy=2, gracze=[], karty=[]):
        self.ilosc_graczy = ilosc_graczy
        self.karty = karty
        self.gracze = gracze
        
    def __str__(self):
        return str(self.ilosc_graczy)
    def get_gracze(self):
        for i in self.gracze:
            print(i)
        return ""
    def talia(self):
        for liczba in Karta.liczby:
            for kolor in Karta.kolory:
                self.karty.append([liczba,kolor])
                
    def dodaj_graczy(self):
        for el in range(1,self.ilosc_graczy+1):
            x=str(f"Gracz {el} ")
            self.gracze.append(Gracz(el,x))
    def tasuj(self):
        random.shuffle(self.karty)
        
    def rozdanie(self):
        for gracz in self.gracze:
            gracz.karta = []
            gracz.karta.append(self.karty[0])
            del self.karty[0]
    def gra(self):
        silniejsza = int(self.gracze[0].karta[0][0])
        zwyciezca = str(self.gracze[0].ID_G)+ " " + self.gracze[0].nazwa
        znak = str(self.gracze[0].karta[0][1])
        for el in range(0,self.ilosc_graczy):
            if int(self.gracze[el].karta[0][0]) > silniejsza:
                silniejsza = int(self.gracze[el].karta[0][0])
                zwyciezca = str(self.gracze[el].ID_G)+ " " + self.gracze[el].nazwa
                znak = str(self.gracze[el].karta[0][1])
            if int(self.gracze[el].karta[0][0]) == silniejsza:
                if ord(self.gracze[el].karta[0][1][0])+ord(self.gracze[el].karta[0][1][1]) > ord(znak[0])+ord(znak[1]):
                    silniejsza = int(self.gracze[el].karta[0][0])
                    zwyciezca = str(self.gracze[el].ID_G)+ " " + self.gracze[el].nazwa
                    znak = str(self.gracze[el].karta[0][1])
                else:
                    print("poprzednia karta jest wyższa")
                
            else:
                print("poprzednia karta jest wyższa")
        return f"Wygral gracz {zwyciezca} z karta {silniejsza , znak}"
            
#klasa rozgrywka, możemy wprowadzić ilość graczy
#rozgrywka.talia tworzy talie kart
#rozgrywka.dodaj_graczy dodaje graczy do rozgrywki
#rozgrywka.tasuj tasuje stworzona wczesniej talie
#rozgrywka.rozdanie rozdaje karty graczom
#rozgrywka.gra przeprowadza rozgrywke, gracz z wyzsza karta wygrywa
        
rozgrywka1 = Rozgrywka(3)
print(rozgrywka1.talia())
print(rozgrywka1.karty)
print(rozgrywka1.tasuj())
print(rozgrywka1.karty)
print(rozgrywka1.dodaj_graczy())
print(rozgrywka1.get_gracze())
print(rozgrywka1.rozdanie())
print(rozgrywka1.get_gracze())
print(rozgrywka1.gra())

