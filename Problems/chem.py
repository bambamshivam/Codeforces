import math
P1=float(input("Please Input Pressure "))
T1=float(input("Please Input Temperature "))


def throttle(P1,T1):
	if(P1==1.4):
		Cp=[118.76,120.15,121.83,123.75,125.91,128.28,130.84,133.59,136.52,139.63,142.95,146.49,150.29,154.41,158.95,164.06,170.09,148.90,142.82,140.36,139.56]
		Ts=368.760
		Hl=31450.9
		Hv=46891.0
		Sl=263.868
		Sv=305.738
		Cpsl=176.63
		Cpsv=150.15
	elif(P1==1.6):
		Cp=[118.74,120.13,121.8,123.73,125.88,128.24,130.8,133.53,136.45,139.55,142.85,146.37,150.14,154.21,158.69,163.71,169.56,176.87,153.78,147.2,144.38]
		Ts=375.611
		Hl=32665.2
		Hv=47338.3
		Sl=267.065
		Sv=306.130
		Cpsl=182.10
		Cpsv=159.3
	else:
		Cp=[118.87,120.28,121.98,123.94,126.13,128.54,131.15,133.95,96.22,98.31,100.54,102.86,105.25,107.68,110.13,112.61,115.1,117.59,120.09,122.57,125.04]
		Ts=272.64
		Hl=16770.1
		Hv=39202.7
		Sl=218.485
		Sv=300.764
		Cpsl=134.73
		Cpsv=94.82
	if(T1>Ts):
		Td=(Ts//10)*10 + 10
		if(T1<Td):
			Ta=(Ts+T1)/2
			Tu=(Ta//10)*10
			Td=Tu+10
			c=((Td-Ta)/(Td-Tu))*Cp[(int)(Tu-200)//10] + ((Ta-Tu)/(Td-Tu))*Cp[(int)(Td-200)//10]
			H1=Hv + c*(T1-Ts)
			S1=Sv + c*math.log(T1/Ts)
		else:
			s=0
			p=0
			Tu=Ts
			Td=(Tu//10)*10 + 10
			while(Td<T1):
				Ta=(Tu+Td)/2
				c=((Td-Ta)/(Td-Tu))*Cp[(int)(Tu-200)//10] + ((Ta-Tu)/(Td-Tu))*Cp[(int)(Td-200)//10]
				s=s + c*(Td-Tu)
				p=p + c*math.log(Td/Tu)
				Tu=Td
				Td=Td+10
			Ta=(Tu+T1)/2
			Td=Tu+10
			c=((Td-Ta)/(Td-Tu))*Cp[(int)(Tu-200)//10] + ((Ta-Tu)/(Td-Tu))*Cp[(int)(Td-200)//10]
			s=s + c*(T1-Tu)
			p=p + c*math.log(T1/Tu)
			H1=Hv + s
			S1=Sv + p
	elif(T1<Ts):
		Td=(T1//10)*10 + 10
		if(Ts<Td):
			Ta=(Ts+T1)/2
			Tu=(Ta//10)*10
			Td=Tu+10
			c=((Td-Ta)/(Td-Tu))*Cp[(int)(Tu-200)//10] + ((Ta-Tu)/(Td-Tu))*Cp[(int)(Td-200)//10]
			H1=Hl - c*(Ts-T1)
			S1=Sl - c*math.log(Ts/T1)
		else:
			s=0
			p=0
			Tu=T1
			Td=(Tu//10)*10 + 10
			while(Td<Ts):
				Ta=(Tu+Td)/2
				c=((Td-Ta)/(Td-Tu))*Cp[(int)(Tu-200)//10] + ((Ta-Tu)/(Td-Tu))*Cp[(int)(Td-200)//10]
				s=s + c*(Td-Tu)
				p=p + c*math.log(Td/Tu)
				Tu=Td
				Td=Td+10
			Ta=(Tu+Ts)/2
			Td=Tu+10
			c=((Td-Ta)/(Td-Tu))*Cp[(int)(Tu-200)//10] + ((Ta-Tu)/(Td-Tu))*Cp[(int)(Td-200)//10]
			s=s + c*(Ts-Tu)
			p=p + c*math.log(Ts/Tu)
			H1=Hl - s
			S1=Sl - p
	else:
		x=float(input("Please Input quality factor "))
		H1=(1-x)*Hl + x*Hv
		S1=(1-x)*Sl + x*Sv
	return (H1,S1)


def CalcT(P1,T1):
	print("Q1)")
	H2,S2=throttle(P1,T1)
	print("H2="+str(H2))
	if(H2>39202.7):
		print("State=Superheated Vapour")
	elif(H2<16770.1):
		print("State=Supercooled Liquid")
	else:
		print("State=Liquid Vapour Coexistence")
	print("Q2)")
	if(H2>16770.1 and H2<39202.7):
		T2=272.64
		x=(H2-16770.1)/(39202.7-16770.1)
		print("x="+str(x))
	else:
		Ha,Sa=throttle(0.1,200)
		Hb,Sb=throttle(0.1,300)
		T2=(H2-Hb)*(200-300)/(Ha-Hb) + 300
	print("T2="+str(T2))
	print("Q3)")
	print("S2="+str(S2))
	if(S2<218.485):
		H3,S3=throttle(0.1,T2)
		print("Maximum Work="+str(H3-H2))
	elif(S2>300.764):
		H3,S3=throttle(0.1,T2)
		print("Maximum Work="+str(H3-H2))
	else:
		x=(S2-218.485)/(300.764-218.485)
		print("x="+str(x))
		H=(1-x)*16770.1 + x*39202.7
		print("Maximum Work="+str(H-H2))


CalcT(P1,T1)
