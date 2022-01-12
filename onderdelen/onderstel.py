#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:49 2022

@author: windhoos
"""

import plank as p
import config as cfg

from math import floor

def onderstel():
    Breedtes=[]
    Balken=[]
    
    diepte_kast=cfg.diepte_kast
    breedte_plank=cfg.breedte_plank
    lengte_plank=cfg.lengte_plank
    dikte_plank=cfg.dikte_plank
    breedte_kast=cfg.breedte_kast
    hoogte_voet=cfg.hoogte_voet
    
    d=float(diepte_kast)
    b=float(breedte_plank)
    
    fractie_planken=d/b
    hele_planken=int(floor(fractie_planken))
    over=fractie_planken-hele_planken
    
    if ((over > 0.0) and (hele_planken > 1)):
        hele_planken=hele_planken-1
        for planken in range(hele_planken):
            Breedtes.append(b)
        over=(b*(over+1.)/2.)
        Breedtes.append(over)
        Breedtes.append(over)
    else:
        for planken in range(hele_planken):
            Breedtes.append(b)
    
    uy=diepte_kast/2.-Breedtes[planken]/2.    
    for planken in range(len(Breedtes)):
        plank=p.plank(lengte_plank,breedte_plank,dikte_plank)
        plank.plank_zagen(breedte_kast,Breedtes[planken],dikte_plank)
        rx,ry,rz=0,0,0
        ux=0
        if planken >= 1:
            uy = uy - Breedtes[planken]/2. - Breedtes[planken-1]/2.
        uz=hoogte_voet+dikte_plank/2.
        sx,sy,sz=1,1,1
        plank.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        balk=plank.balk()
        Balken.append(balk)
        
    return Balken