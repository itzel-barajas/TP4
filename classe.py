import random

class Polynome:

    def __init__(self,listecoef):
        self.coeff= listecoef


    def afficherPolynome(self):
        n = len(self.coeff) - 1 #list lenght -1 to get the maximum degree of the polynomial
    
        for a in range(n, -1, -1): #from higher to lower degree
            c = self.coeff[a] #to get the current coefficient
        
            if c != 0:
                if a == 0:#constant, last term without x
                    print(c, end="")
                elif a == 1: #term with x without power 
                    print(f"{c}x", end="")
                else: #to any term a > 1 so it writes 'x^a'
                    print(f"{c}x^{a}", end="")
           
                if a>0:
                    print(" + ", end="")
