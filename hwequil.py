#!/usr/bin/python

import math

def pop_calcs(p, q):

    dom_pop = p*p
    het_pop = 2*p*q # heterozygote population
    rec_pop = q*q
    
    return [dom_pop, het_pop, rec_pop]

def by_recessive_pop(pop_rec, pop):
    # calculate figures by the recessive allele population
    
    q2 = pop_rec / (pop)
    
    ''' The Hardy-Weinberg equation is as follows:
    
    p^2 + 2pq + q^2 == 1
    p + q == 1 '''
    
    q = math.sqrt(q2) # recessive allele frequency
    p = 1 - q # dominant allele frequency
    
    return pop_calcs(p, q)
    
def by_dominant_pop(pop_dom, pop):
    # calculate figures by the dominant allele population
    
    q2 = (pop - pop_dom) / (pop)
    
    ''' The Hardy-Weinberg equation is as follows:
    
    p^2 + 2pq + q^2 == 1
    p + q == 1 '''
    
    q = math.sqrt(q2) # recessive allele frequency
    p = 1 - q # dominant allele frequency
    
    return pop_calcs(p, q)
    
def by_p(p):
    # Calculate figures based on dominant allele frequency
    
    q = 1 - p
    
    return pop_calcs(p, q)
    
def by_q(q):
    # Calculate figures based on recessive allele frequency

    p = 1 - q
    
    return pop_calcs(p, q)
