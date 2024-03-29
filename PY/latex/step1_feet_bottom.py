#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:49:59 2022

@author: windhoos
"""

from latex import config as cfg
from latex import balk, arrow
from latex import table_builder

def get_feet():
    voeten=cfg.voeten
    rows=len(voeten.index)
    arrowlist=[]
    for row in range(rows):
        x0=voeten.loc[row,'xloc']
        y0=voeten.loc[row,'yloc']
        z0=voeten.loc[row,'zloc']
        l=voeten.loc[row,'lengte']
        w=voeten.loc[row,'breedte']
        h=voeten.loc[row,'dikte']
        xa=voeten.loc[row,'rx']
        ya=voeten.loc[row,'ry']
        za=voeten.loc[row,'rz']
        
        cfg.aantal_voeten = cfg.aantal_voeten + 1
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step1_feet.append(B)
        pa=B[-2]
        pb=B[-1]
        if y0 > 0:
            arrowlist.append([pa,pb,l,w,h])
      
    return arrowlist

def get_bottom():
    onderkant=cfg.onderkant
    cfg.step1_hoogte=cfg.poot_hoogte+cfg.plank_dikte
    
    xmax = onderkant.loc[onderkant['lengte'].idxmax()]
    xmax = xmax[0]
    cfg.step1_breedte=xmax
    
    cfg.step1_diepte= onderkant['breedte'].sum()
    
    cfg.step1_Ox=0.
    cfg.step1_Oy=0.
    cfg.step1_Oz=cfg.step1_hoogte/2.
    
    rows=len(onderkant.index)
    for row in range(rows):
        x0=onderkant.loc[row,'xloc']
        y0=onderkant.loc[row,'yloc']
        z0=onderkant.loc[row,'zloc']
        l=onderkant.loc[row,'lengte']
        w=onderkant.loc[row,'breedte']
        h=onderkant.loc[row,'dikte']
        xa=onderkant.loc[row,'rx']
        ya=onderkant.loc[row,'ry']
        za=onderkant.loc[row,'rz']
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step1_bottom.append(B)
        
def build_arrow(arrowlist):
    for a in range(len(arrowlist)):
        if a != 0:
            x0=arrowlist[0][1][0] 
            y0=arrowlist[0][1][1] + arrowlist[0][0][2]
            z0=arrowlist[0][1][2]
            
            x1=arrowlist[0][1][0] 
            y1=arrowlist[0][1][1] + arrowlist[0][2]*a*2
            z1=arrowlist[0][1][2]
            
            x2=arrowlist[a][1][0] 
            y2=arrowlist[a][1][1] + arrowlist[a][2]*a*2
            z2=arrowlist[a][1][2]
            
            thickness = arrowlist[0][2]/3
            
            A=get_arrow(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness)
            cfg.step1_arrow.append(A)
        
def get_arrow(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness):
    case=1
    A=arrow.build(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case)
    return A

def build(path,lang):
    arrowlist=get_feet()
    get_bottom()
    cfg.step1_arrow=build_arrow(arrowlist)
    table_builder.latex([cfg.voeten,cfg.onderkant],path,lang,1)