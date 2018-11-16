#!/usr/bin/env python3

#/mnt/c/Users/romie/Desktop/Fac/Master_1_BCD/HMIN113M (ordi baraque)
#/mnt/c/Users/romie/Desktop/Fac/HMIN113 (ordi portabe)

import os, sys, re
file=sys.argv[1]
dicoChro={}
dicoNm={}
list1=[]
list2=[]
with open(file,"r") as vcf :
	for ligne in vcf :
		
		#print(ligne)
		info1=re.search("^#(\w*)\s(\w*)\s(\w*)\s(\w*)\t(\w*)\s(\w*)\s(\w*)\s(\w*)\s",ligne)
		info2=re.search("(^#)*.",ligne)
		
		
		
			
			#print(ligne)
		if info1 :
			Chro=str(info1.group(1))
			list2.append(Chro)
				#print(Chro)
			Pos=str(info1.group(2))
			list2.append(Pos)
				#print(Pos)
			Id=str(info1.group(3))
			list2.append(Id)
				#print(Id)
			Ref=str(info1.group(4))
			list2.append(Ref)
				#print(Ref)
			Alt=str(info1.group(5))
			list2.append(Alt)
				#print(Alt)
			Qual=str(info1.group(6))
			list2.append(Qual)
				#print(Qual)
			Fil=str(info1.group(7))
			list2.append(Fil)
				#print(Fil)
			Inf=str(info1.group(8))
			list2.append(Inf)
			
		if not info2.group(1) :
			#if not info2.group(1) :
			#print(ligne)
			list1=ligne.split("\t")
			print(list1[0])
		
			if Chro in dicoChro:
				if list1[0] in dicoChro[Chro]:
					print("ca marche")
					if list1[1] in dicoChro[Chro][list1[0]] :
							print("ca marche")
							#if list1[1] in dicoChro[Chro][list1[0]][list2[1]] :
								#print("ca marche")
							#else :
								#dicoChro[Chro][list1[0]][list2[1].append(list1[1])]
								#print("YOLO")
					else :
							dicoChro[Chro][list1[0]][list2[1]]=[]
							#print("YOLO")
							
					if list1[2] in dicoChro[Chro][list1[0]] :
							print("ca marche")
							#if list1[1] in dicoChro[Chro][list1[0]][list2[1]] :
								#print("ca marche")
							#else :
								#dicoChro[Chro][list1[0]][list2[1].append(list1[1])]
								#print("YOLO")
					else :
							dicoChro[Chro][list1[0]][list2[2]]=[]
							
					if list1[3] in dicoChro[Chro][list1[0]] :
							print("ca marche")
							#if list1[1] in dicoChro[Chro][list1[0]][list2[1]] :
								#print("ca marche")
							#else :
								#dicoChro[Chro][list1[0]][list2[1].append(list1[1])]
								#print("YOLO")
					else :
							dicoChro[Chro][list1[0]][list2[3]]=[]
							
					if list1[4] in dicoChro[Chro][list1[0]] :
							print("ca marche")
							#if list1[1] in dicoChro[Chro][list1[0]][list2[1]] :
								#print("ca marche")
							#else :
								#dicoChro[Chro][list1[0]][list2[1].append(list1[1])]
								#print("YOLO")
					else :
							dicoChro[Chro][list1[0]][list2[4]]=[]
							
					if list1[5] in dicoChro[Chro][list1[0]] :
							print("ca marche")
							#if list1[1] in dicoChro[Chro][list1[0]][list2[1]] :
								#print("ca marche")
							#else :
								#dicoChro[Chro][list1[0]][list2[1].append(list1[1])]
								#print("YOLO")
					else :
							dicoChro[Chro][list1[0]][list2[5]]=[]
							
					if list1[6] in dicoChro[Chro][list1[0]] :
							print("ca marche")
							#if list1[1] in dicoChro[Chro][list1[0]][list2[1]] :
								#print("ca marche")
							#else :
								#dicoChro[Chro][list1[0]][list2[1].append(list1[1])]
								#print("YOLO")
					else :
							dicoChro[Chro][list1[0]][list2[6]]=[]
							
					if list1[7] in dicoChro[Chro][list1[0]] :
							print("ca marche")
							#if list1[1] in dicoChro[Chro][list1[0]][list2[1]] :
								#print("ca marche")
							#else :
								#dicoChro[Chro][list1[0]][list2[1].append(list1[1])]
								#print("YOLO")
					else :
							dicoChro[Chro][list1[0]][list2[7]]=[]
							
					if list1[7] in dicoChro[Chro][list1[0]] :
							print("ca marche")
							#if list1[1] in dicoChro[Chro][list1[0]][list2[1]] :
								#print("ca marche")
							#else :
								#dicoChro[Chro][list1[0]][list2[1].append(list1[1])]
								#print("YOLO")
					else :
							dicoChro[Chro][list1[0]][list2[7]]={}
					
				
				else :
					dicoChro[Chro][list1[0]]={}
						
			else :
				dicoChro[Chro]={}
		

				
		
		
				
print(list1[1])			
print(dicoChro) 	
			

			
			
