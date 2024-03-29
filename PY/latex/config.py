#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:46:52 2022

@author: windhoos
"""

stuklijst = 0
planklijst = 0

voeten=0
onderkant=0
rib_onder=0
ribmax=0
bovenkant=0
achterrib=0
vlonders=0
zeidelinks=0
zeiderechts=0
achterkant=0
voorkant=0
deur=0
deur_volledig=0
stut=0
stut_volledig=0
scharnier=0
slot=0

poot_hoogte=0
plank_dikte=0
balk_dikte=0

plank_opt=0
balk_opt=0

hoek=0
schroef=0 #plank dikte+balk dikte
schroef_kort=0 #balk dikte
schroef_deur=0 #twee planken
scharnier_aantal=0
slot_aantal=0

aantal_voeten=0
aantal_verdiepingen=2
aantal_deur_planken=0
aantal_stut_planken=0

step1_hoogte=0 #- globaal
step1_breedte=0 #- globaal
step1_diepte=0 #- globaal
step1_Ox=0
step1_Oy=0
step1_Oz=0
step1_ycam=[]
step1_feet=[]
step1_bottom=[]
step1_arrow=[]
#step1_camera=[0,0,0]

step2_hoogte=0 #- globaal
step2_breedte=0 #- globaal
step2_diepte=0 #- globaal
step2_Ox=0
step2_Oy=0
step2_Oz=0
step2_xcam=[]
step2_ycam=[]
step2_feet=[]
step2_bottom=[]
step2_rib_onder=[]
step2_arrow=[]
#step2_camera=[0,0,0]

step3_hoogte=0 #- globaal
step3_breedte=0 #- globaal
step3_diepte=0 #- globaal
step3_Ox=0
step3_Oy=0
step3_Oz=0
step3_ycam=[]
step3_ribben_horiz=[]
step3_ribben_vert=[]
step3_hoeken=[]
step3_arrow=[]
step3_pointer=[]
step3_camera=[0,0,0]

step4_hoogte=0 #- globaal
step4_breedte=0 #- globaal
step4_diepte=0 #- globaal
step4_Ox=0
step4_Oy=0
step4_Oz=0
step4_feet=[]
step4_bottom=[]
step4_rib_onder=[]
step4_ribben_vert=[]
step4_ribben_horiz=[]
step4_pointer=[]
step4_hoeken=[]
step4_arrow=[]
#step4_camera=[0,0,0]

step5_hoogte=0 #- globaal
step5_breedte=0 #- globaal
step5_diepte=0 #- globaal
step5_Ox=0
step5_Oy=0
step5_Oz=0
step5_xcam=[]
step5_feet=[]
step5_bottom=[]
step5_rib_onder=[]
step5_ribben_vert=[]
step5_ribben_horiz=[]
step5_achterrib=[]
step5_pointer=[]
step5_hoeken=[]
step5_arrow=[]
step5_zoom=[]

step6_hoogte=0 #- globaal
step6_breedte=0 #- globaal
step6_diepte=0 #- globaal
step6_Ox=0
step6_Oy=0
step6_Oz=0
step6_xcam=[]
step6_feet=[]
step6_bottom=[]
step6_rib_onder=[]
step6_ribben_vert=[]
step6_ribben_horiz=[]
step6_achterrib=[]
step6_vlonders=[]
step6_pointer=[]
step6_hoeken=[]
step6_arrow=[]
step6_zoom=[]

step7_hoogte=0 #- globaal
step7_breedte=0 #- globaal
step7_diepte=0 #- globaal
step7_Ox=0
step7_Oy=0
step7_Oz=0
step7_xcam=[]
step7_feet=[]
step7_bottom=[]
step7_rib_onder=[]
step7_ribben_vert=[]
step7_ribben_horiz=[]
step7_achterrib=[]
step7_vlonders=[]
step7_bovenkant=[]
step7_pointer=[]
step7_hoeken=[]
step7_arrow=[]
step7_zoom=[]

step8_hoogte=0 #- globaal
step8_breedte=0 #- globaal
step8_diepte=0 #- globaal
step9_Ox=0
step8_Oy=0
step8_Oz=0
step8_xcam=[]
step8_feet=[]
step8_bottom=[]
step8_rib_onder=[]
step8_ribben_vert=[]
step8_ribben_horiz=[]
step8_achterrib=[]
step8_vlonders=[]
step8_bovenkant=[]
step8_zeiderechts=[]
step8_zeidelinks=[]
step8_pointer=[]
step8_hoeken=[]
step8_arrow=[]
step8_zoom=[]

step9_hoogte=0 #- globaal
step9_breedte=0 #- globaal
step9_diepte=0 #- globaal
step9_Ox=0
step9_Oy=0
step9_Oz=0
step9_xcam=[]
step9_feet=[]
step9_bottom=[]
step9_rib_onder=[]
step9_ribben_vert=[]
step9_ribben_horiz=[]
step9_achterrib=[]
step9_vlonders=[]
step9_bovenkant=[]
step9_zeiderechts=[]
step9_zeidelinks=[]
step9_achterkant=[]
step9_pointer=[]
step9_hoeken=[]
step9_arrow=[]
step9_zoom=[]

step10_hoogte=0 #- globaal
step10_breedte=0 #- globaal
step10_diepte=0 #- globaal
step10_Ox=0
step10_Oy=0
step10_Oz=0
step10_zcam=[]
step10_feet=[]
step10_bottom=[]
step10_rib_onder=[]
step10_ribben_vert=[]
step10_ribben_horiz=[]
step10_achterrib=[]
step10_vlonders=[]
step10_bovenkant=[]
step10_zeiderechts=[]
step10_zeidelinks=[]
step10_achterkant=[]
step10_deurpost=[]
step10_pointer=[]
step10_hoeken=[]
step10_arrow=[]
step10_zoom=[]

step11_hoogte=0 #- globaal
step11_breedte=0 #- globaal
step11_diepte=0 #- globaal
step11_Ox=0
step11_Oy=0
step11_Oz=0
step11_xcam=[]
step11_zcam=[]
step11_deur=[]
step11_stut=[]
step11_pointer=[]
step11_hoeken=[]
step11_arrow=[]
step11_zoom=[]

step12_hoogte=0 #- globaal
step12_breedte=0 #- globaal
step12_diepte=0 #- globaal
step12_Ox=0
step12_Oy=0
step12_Oz=0
step12_feet=[]
step12_bottom=[]
step12_rib_onder=[]
step12_ribben_vert=[]
step12_ribben_horiz=[]
step12_achterrib=[]
step12_vlonders=[]
step12_bovenkant=[]
step12_zeiderechts=[]
step12_zeidelinks=[]
step12_achterkant=[]
step12_deurpost=[]
step12_deur=[]
step12_stut=[]
step12_scharnier=[]
step12_slot=[]
step12_pointer=[]
step12_hoeken=[]
step12_arrow=[]
step12_zoom=[]