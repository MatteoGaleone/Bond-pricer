#!/usr/bin/env python
# coding: utf-8

# In[5]:


def CalcolaValoreNormale():
    C=float(input('Inserisci il valore della cedola= '))
    r=float(input('Inserisci lo YTM= '))/100
    N=float(input('Inserisci il numero di anni prima della scadenza= '))
    m=float(input('Inserisci il numero di pagamenti per ogni periodo= '))
    F=float(input('Inserisci il valore nominale= '))
    P= C*(1-(1+r)**(-N*m))/r+F/(1+r)**(N*m)
    print('''Il valore attuale dell'obbligazione è =''', P)


# In[6]:


def CalcolaValoreZCB():
    r=float(input('Inserisci lo YTM= '))/100
    N=float(input('Inserisci il numero di anni prima della scadenza= '))
    F=float(input('Inserisci il valore nominale= '))
    P=F/(1+r)**N
    print('''Il valore attuale dell'obbligazione ZCB è =''', P)


# In[7]:


def Programma():
    while True:
        ZCB=str(input('Inserire se Normale(N) o Zero Coupon (ZCB): '))
        if ZCB == 'ZCB' or 'zcb':
            CalcolaValoreZCB()
        else:
            CalcolaValoreNormale()
        while True:
            risposta = str(input('Vuoi inserire una nuova obbligazione? (si/no): '))
            if risposta in ('si', 'no'):
                break
            print('Input non valido.')
        if risposta == 'si':
            continue
        else:
            print('Ciao')
            break


# In[4]:


Programma()


# In[ ]:




