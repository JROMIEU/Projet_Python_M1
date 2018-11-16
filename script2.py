#!/usr/bin/env python3

#/mnt/c/Users/romie/Desktop/Fac/Master_1_BCD/HMIN113M (ordi baraque)
#/mnt/c/Users/romie/Desktop/Fac/HMIN113 (ordi portabe)

import os, sys, re, numpy
file=sys.argv[1]
dicoChro={}
dicoNm={}
list1=[]
list2=[]
list3=[]
n=1
t=0
with open(file,"r") as vcf :
	for ligne in vcf :
		
		
		info1=re.search("^#(\w*)\s(\w*)\s(\w*)\s(\w*)\t(\w*)\s(\w*)\s(\w*)\s(\w*)\s",ligne)
		info2=re.search("(^#)*.",ligne)
		
		
		
			
			
		if info1 :
			Chro=str(info1.group(1))
			list2.append(Chro)
				
			Pos=str(info1.group(2))
			list2.append(Pos)
				
			Id=str(info1.group(3))
			list2.append(Id)
				
			Ref=str(info1.group(4))
			list2.append(Ref)
				
			Alt=str(info1.group(5))
			list2.append(Alt)
				
			Qual=str(info1.group(6))
			list2.append(Qual)
				
			Fil=str(info1.group(7))
			list2.append(Fil)
				
			Inf=str(info1.group(8))
			list2.append(Inf)
			
		if not info2.group(1) :
			
			list1=ligne.split("\t")
			
			
			
		
			if Chro in dicoChro:
				
				if list1[0] in dicoChro[Chro]:
						
					while n<7 :
						if list1[n] in dicoChro[Chro][list1[0]] :
							print("ca marche")
							
							#else :
								#dicoChro[Chro][list1[0]][list2[n]]=[]
							#n+=1
								
							#if list1[7] in dicoChro[Chro][list1[0]] :
								#print("ca marche")
							
						else :
							
							print(dicoChro[1].values())
							dicoChro[Chro][list1[0]][list2[n]]={}
						
						n+=1
				else :
					dicoChro[Chro][list1[0]]={}
				
			else :
				dicoChro[Chro]={}
		

				
		
		
				
print(list1[1])			
print(dicoChro) 	