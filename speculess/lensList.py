import re

# This is the one file storing all the lens information
class newLens():
	def __init__(self,name,man,ident,born =0.0, 
		focus = None,
		aperture = None,
		color=None, 
		img=True, amazon=None, bh = None, kind=None, customShop = None, customShopName = None, adorama = None, ebay = None):
		self.name = name
		self.focus = focus
		self.aperture = aperture #the lowest aperture
		self.man = manRef(man)
		self.color = color
		self.id = man + str(ident)
		if img == False:
			self.img = 'http://placehold.it/260x180' 
		else:
			self.img = '/images/lenses/%s/%s.jpg' % (re.sub(' ','_',self.man), ident)
		self.amazon = amazon
		if amazon is None:
			self.amazonDisplay = 'none'
		else:
			self.amazonDisplay = 'visible'
		self.bh = bh
		if bh is None:
			self.bhDisplay = 'none'
		else:
			self.bhDisplay = 'visible'

		self.adorama = adorama
		if adorama is None:
			self.adoramaDisplay = 'none'
		else:
			self.adoramaDisplay = 'visible'

		self.ebay = ebay
		if ebay is None:
			self.ebayDisplay = 'none'
		else:
			self.ebayDisplay = 'visible'

		self.born = born

		self.kind = kind

		self.customShopName = customShopName
		self.customShop = customShop
		if customShop is None:
			self.customShopDisplay = 'none'
		else:
			self.customShopDisplay = 'visible'

def manRef(reference):
	mannyMap = {
	'O': 'Olympus', 
	'P': 'Panasonic', 
	'S': 'Sigma', 
	'C': 'Cosina', 
	'T': 'Tokina',
	'R': 'Rokinon',
	'M': 'SLR Magic',
	'Y': 'Yasuhara',
	'J': 'Jackar',
	}
	return mannyMap[reference]
			
lensList = []

# Olympus Lenses
#---------------------------

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 60mm f/2.8 Macro', 
	man = 'O',
	focus = '60',
	aperture = 2.8,
	color = 'black',
	ident = 1000,
	kind = 'prime, macro',
	born = 2012.0917,
	bh='http://www.bhphotovideo.com/c/product/892512-REG/Olympus_v312010bu000_MSC_ED_M_60mm_f_2_8.html',
	amazon = 'http://www.amazon.com/Olympus-MSC-60mm-2-8-Lens/dp/B0096WDK0K/ref=sr_1_3?ie=UTF8&qid=1352209742&sr=8-3&keywords=60mm+macro'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 12mm f/2.0 Limited Edition', 
	man = 'O',
	focus = '12',
	aperture = 2.0,
	color = 'black',
	kind = 'prime',
	born = 2012.0917,
	ident= 1001,
	amazon = 'http://www.amazon.com/Olympus-Special-Edition-12mm-Lens/dp/B0096WDLOU/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital 17mm f/1.8', 
	man = 'O',
	focus = '17',
	aperture = 1.8,
	kind = 'prime', 
	color = 'unknown',
	born = 2012.12,
	ident= 1002,
	adorama = 'http://www.adorama.com/IOM1718MSL.html'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 9-18mm f/4.0-5.6', 
	man = 'O',
	ident= 1003,
	aperture = 4.0,
	kind = 'zoom, wide',
	born = 2012.0203,
	amazon= 'http://www.amazon.com/Olympus-M-Zuiko-9-18mm-4-0-5-6-Black/dp/B004F7IH0O/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 14-42mm f/3.5-5.6', 
	man = 'O',
	ident= 1004,
	born = 2009.0616,
	kind = 'zoom',
	aperture = 3.5,
	amazon= 'http://www.amazon.com/Olympus-14-42mm-3-5-5-6-Digital-Black/dp/B002CGSYLW/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 12-50mm f/3.5-6.3', 
	man = 'O',
	ident= 1005,
	aperture = 3.5,
	kind = 'zoom',
	born = 2011.1214,
	amazon = 'http://www.amazon.com/Olympus-M-ZUIKO-DIGITAL-F3-5-6-3-V314040BU000/dp/B0073AIXOA'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital 14-42mm f/3.5-6.3 II R', 
	man = 'O',
	ident= 1006,
	aperture = 3.5,
	kind = 'zoom',
	born = 2011.0630,
	amazon = 'http://www.amazon.com/Zuiko-Digital-14-42mm-3-5-5-6--Black/dp/B005AHKY0O/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital 14-42mm f/3.5-6.3 II', 
	man = 'O',
	ident= 1007,
	aperture = 3.5,
	kind = 'zoom',
	born = 2010.1116,
	amazon = 'http://www.amazon.com/gp/product/B00866SCTG/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 14-150mm f/4.0-5.6', 
	man = 'O',
	ident= 1008,
	aperture = 4.0,
	kind = 'tele',
	born = 2010.0203,
	amazon = 'http://www.amazon.com/Olympus-ED-14-150mm-Panasonic-Interchangeable/dp/B0035LBRMQ/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 40-150mm f/4.0-5.6', 
	man = 'O',
	ident= 1009,
	aperture = 4.0,
	kind = 'tele',
	born = 2010.0831,
	amazon = 'http://www.amazon.com/Olympus-M-Zuiko-40-150mm-4-0-5-6-Digital/dp/B004EEL3HW'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 40-150mm f/4.0-5.6 R', 
	man = 'O',
	ident= 1010,
	aperture = 4.0,
	kind = 'tele',
	born = 2011.0630,
	amazon = 'http://www.amazon.com/Olympus-M-Zuiko-40-150mm-4-0-5-6-Digital/dp/B0066J6EOU/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 75-300mm f/4.8-6.7 R', 
	man = 'O',
	ident= 1011,
	aperture = 4.8,
	kind = 'tele',
	born = 2010.0831,
	amazon = 'http://www.amazon.com/Olympus-M-Zuiko-75-300mm-4-8-6-7-Digital/dp/B00492GLFS/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 12mm f/2.0', 
	man = 'O',
	ident= 1012,
	kind = 'prime',
	aperture = 2.0,
	born = 2011.0630,
	amazon = 'http://www.amazon.com/Olympus-Zuiko-Digital-Thirds-Cameras/dp/B0058PL9R0/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital 17mm f/2.8', 
	man = 'O',
	ident= 1013,
	kind = 'prime',
	aperture = 2.8,
	born = 2009.0616,
	amazon = 'http://www.amazon.com/Olympus-M-Zuiko-17mm-Lens-Black/dp/B004IK8F32/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital 45mm f/1.8', 
	man = 'O',
	ident= 1014,
	kind = 'prime',
	born = 2011.0230,
	aperture = 1.8,
	amazon = 'http://www.amazon.com/Olympus-Zuiko-Digital-Thirds-Cameras/dp/B0058PL9QG/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 75mm f/1.8', 
	man = 'O',
	ident= 1015,
	kind = 'prime',
	aperture = 1.8,
	born = 2012.0208,
	amazon = 'http://www.amazon.com/Olympus-M-ZUIKO-DIGITAL-High-Grade-Portrait/dp/B00836JHVQ'
	))

# Panasonic Lenses
#----------------------------

lensList.append(newLens(
	name = 'Lumix G 20mm f/1.7 ASPH.', 
	man = 'P',
	focus = '20',
	color = 'black',
	ident= 1000,
	kind = 'prime',
	aperture = 1.7,
	born = 2009.0902,
	amazon = 'http://www.amazon.com/Panasonic-Aspherical-Pancake-Interchangeable-Cameras/dp/B002IKLJVE/ref=sr_1_1?ie=UTF8&qid=1352731179&sr=8-1&keywords=panasonic+20+1.7'
	))

lensList.append(newLens(
	name = 'Lumix G X Vario 35-100mm f/2.8 ASPH.', 
	man = 'P',
	focus = '35-100',
	color = 'black',
	ident= 1001,
	kind = 'tele', 
	aperture = 2.8,
	born = 2012.0917,
	amazon = 'http://www.amazon.com/Panasonic-H-HS35100-35-100mm-Lumix-Cameras/dp/B009B0X9PI/'
	))

lensList.append(newLens(
	name = 'Lumix G Vario 7-14mm f/4.0 ASPH.', 
	man = 'P',
	focus = '7-14',
	color = 'black',
	ident= 1002,
	kind = 'zoom, wide', 
	aperture = 4.0,
	born = 2009.0303,
	amazon = 'http://www.amazon.com/Panasonic-7-14mm-Micro-Four-Thirds/dp/B0028Y5GKK/'
	))

lensList.append(newLens(
	name = 'Lumix G X Vario 12-35mm f/2.8 ASPH. Power O.I.S.', 
	man = 'P',
	ident= 1003,
	aperture = 2.8,
	kind = 'zoom', 
	born = 2012.0531,
	amazon = 'http://www.amazon.com/Panasonic-H-HS12035-LUMIX-VARIO-12-35mm/dp/B00843ERMW'
	))

lensList.append(newLens(
	name = 'Lumix G Vario 14-42mm f/3.5-5.6 ASPH. Mega O.I.S.', 
	man = 'P',
	ident= 1004,
	aperture = 3.5,
	kind = 'zoom', 
	born = 2012.0307,
	amazon = 'http://www.amazon.com/Panasonic-14-42mm-Aspherical-OIS-Interchangeable/dp/B0043VE28I/'
	))

lensList.append(newLens(
	name = 'Lumix G X Vario PZ 14-42mm f/3.5-5.6 ASPH. Power O.I.S.', 
	man = 'P',
	ident= 1005,
	aperture = 3.5,
	kind = 'zoom',
	born = 2011.0826,
	amazon = 'http://www.amazon.com/Panasonic-14-42mm-F3-5-5-6-Digital-Cameras/dp/B005J5TZVG'
	))

lensList.append(newLens(
	name = 'Lumix G Vario 14-45mm f/2.8 ASPH. Mega O.I.S.', 
	man = 'P',
	ident= 1006,
	aperture = 2.8,
	kind = 'zoom',
	born = 2008.0912,
	amazon = 'http://www.amazon.com/Panasonic-14-45mm-F3-5-5-6-H-FS014045-Japanese/dp/B0021L90JI/'
	))

lensList.append(newLens(
	name = 'Lumix G Vario HD 14-140mm f/4.0-5.8 ASPH. Mega O.I.S.', 
	man = 'P',
	ident= 1007,
	aperture = 4.0,
	kind = 'tele',
	born = 2009.0303,
	amazon = 'http://www.amazon.com/Panasonic-14-140mm-Micro-Four-Thirds/dp/B0028Y5GLO'
	))

lensList.append(newLens(
	name = 'Lumix G X Vario PZ 45-175mm f/4.0-5.6 ASPH. Power O.I.S.', 
	man = 'P',
	ident= 1008,
	aperture = 4.0,
	kind = 'tele',
	born = 2011.0826,
	amazon = 'http://www.amazon.com/Panasonic-45-175mm-F4-0-5-6-Digital-Cameras/dp/B005J5TZWK'
	))

lensList.append(newLens(
	name = 'Lumix G Vario 45-200mm f/4.0-5.6 Mega O.I.S.', 
	man = 'P',
	ident= 1009,
	aperture = 4.0,
	kind = 'tele',
	born = 2008.0912,
	amazon = 'http://www.amazon.com/Panasonic-45-200mm-4-0-5-6-Olympus-Cameras/dp/B001ISKNKA'
	))

lensList.append(newLens(
	name = 'Lumix G Vario 100-300mm f/4.0-5.6 Mega O.I.S.', 
	man = 'P',
	ident= 1010,
	aperture = 4.0,
	kind = 'tele',
	born = 2010.0921,
	amazon = 'http://www.amazon.com/Panasonic-100-300mm-4-0-5-6-OIS-Interchangeable/dp/B0043VE28S'
	))

lensList.append(newLens(
	name = 'Leica DG Macro-Elmarit 45mm f/2.8 ASPH. Mega O.I.S.', 
	man = 'P',
	ident= 1011,
	aperture = 2.8,
	kind = 'prime, macro',
	born = 2009.0902,
	amazon = 'http://www.amazon.com/Panasonic-45mm-2-8-OIS-Interchangeable/dp/B002NKM29C'
	))

lensList.append(newLens(
	name = 'Lumix G Fisheye 8mm f/3.5', 
	man = 'P',
	ident= 1012,
	aperture = 3.5,
	kind = 'prime, wide',
	born = 2010.0601,
	amazon = 'http://www.amazon.com/Panasonic-8mm-Fisheye-Digital-Cameras/dp/B003O868UG'
	))

lensList.append(newLens(
	name = 'Lumix G 14mm f/2.5 ASPH.', 
	man = 'P',
	ident= 1013,
	aperture = 2.5,
	kind = 'prime',
	born = 2010.0921,
	amazon = 'http://www.amazon.com/Panasonic-14mm-2-5-Aspherical-Interchangeable/dp/B0043VE29C'
	))

lensList.append(newLens(
	name = 'Lumix DG Summilux 25mm f/1.4 ASPH.', 
	man = 'P',
	ident= 1014,
	aperture = 1.4,
	kind = 'prime',
	born = 2011.0613,
	amazon = 'http://www.amazon.com/Panasonic-Lumix-Micro-SUMMILUX-Aspherical/dp/B0055N2L22'
	))


# Sigma Lenses
#--------------------------------
lensList.append(newLens(
	name = '19mm f/2.8 EX DN', 
	man = 'S',
	ident= 1000,
	aperture = 2.8,
	kind = 'prime',
	born = 2012.0110,
	amazon = 'http://www.amazon.com/Sigma-19mm-F2-8--Micro-400963/dp/B007F7G6WW/'
	))

lensList.append(newLens(
	name = '30mm f/2.8 EX DN', 
	man = 'S',
	ident= 1001,
	aperture = 2.8,
	kind = 'prime',
	born = 2012.0110,
	amazon = 'http://www.amazon.com/Sigma-30mm-F2-8-Micro-330963/dp/B0076F3RS4'
	))

# Cosina Lenses
#---------------------------------
lensList.append(newLens(
	name = 'Nokton 17.5mm f/0.95', 
	man = 'C',
	ident= 1000,
	aperture = 0.95,
	kind = 'prime',
	born = 2012.0208,
	amazon = 'http://www.amazon.com/Voigtlander-Nokton-17-5mm-Manual-Focus/dp/B007VHDUN4'
	))

lensList.append(newLens(
	name = 'Nokton 25mm f/0.95', 
	man = 'C',
	ident= 1001,
	aperture = 0.95,
	kind = 'prime',
	born = 2010.0826,
	amazon = 'http://www.amazon.com/Voigtlander-Nokton-Manual-Focus-Micro/dp/B0046EC1OE'
	))

# Tokina Lenses
#---------------------------------

lensList.append(newLens(
	name = '300mm f/6.3 Reflex MF Macro', 
	man = 'T',
	ident= 1000,
	aperture = 6.3,
	kind = 'prime',
	born = 2012.0401,
	amazon = 'http://www.amazon.com/Tokina-Reflex-Olympus-Panasonic-Cameras/dp/B008U9V7P0/'
	))

# Rokinon Lenses
#---------------------------------

lensList.append(newLens(
	name = '7.5mm f/3.5 UMC Fisheye',
	man = 'R',
	ident = 1000,
	born = 2011.0930,
	aperture = 3.5,
	kind = 'prime, wide', 
	amazon = 'http://www.amazon.com/Rokinon-FE75MFT-B-Fisheye-Olympus-Panasonic/dp/B005TOU804/'
	))

# SLR Magic Lenses
#-----------------------------------

lensList.append(newLens(
	name = 'Noktor 50mm f/0.95 HyperPrime',
	man = 'M', 
	ident = 1000,
	aperture = 0.95,
	born = 2011.1112,
	kind = 'prime',
	adorama = 'http://www.adorama.com/SLR5095MFT.html', 
	amazon = 'http://www.amazon.com/SLR-Magic-Noktor-HyperPrime-Cameras/dp/B006QFRLR8'
	))

lensList.append(newLens(
	name = 'Cine 12mm T/1.6 HyperPrime',
	man = 'M',
	ident = 1001,
	aperture = 1.6,
	born = 2011.1112,
	kind = 'prime',
	adorama = 'http://www.adorama.com/SLR1216MFT.html',
	ebay = 'http://www.ebay.com/itm/SLR-Magic-Noktor-Hyper-Prime-Cine-12mm-T1-6-12-1-6-M4-3-SLRMAG-12F16M43-/160900148962?pt=Camera_Lenses&hash=item2576656ee2'
	))

lensList.append(newLens(
	name = '35mm f/1.7 MC',
	man = 'M', 
	ident = 1002,
	aperture = 1.7,
	born = 2009.08,
	kind = 'prime',
	adorama = 'http://www.adorama.com/SLR3517MFT.html',
	ebay = 'http://www.ebay.com/itm/SLR-Magic-35mm-f-1-7-MC-lens-for-EP1-EP2-EPL1-GF1-G1-G2-/250673066577?pt=Camera_Lenses&hash=item3a5d477251'
	))

lensList.append(newLens(
	name = 'Toy Lens 26mm f/1.4',
	man = 'M', 
	ident = 1003,
	aperture = 1.4,
	born = 2010.12,
	kind = 'prime',
	adorama = 'http://www.adorama.com/SLRT2614MFT.html',
	ebay = 'http://www.ebay.com/itm/SLR-Magic-x-Toy-Lens-26mm-f-1-4-lens-w-Macro-EPL2-GF2-/250800912189?pt=Camera_Lenses&hash=item3a64e6373d'
	))

lensList.append(newLens(
	name = 'Toy Lens 11mm f/1.4',
	man = 'M', 
	ident = 1004,
	aperture = 1.4,
	born = 2011.05,
	kind = 'prime',
	adorama = 'http://www.adorama.com/SLRT1114MFT.html', 
	ebay= 'http://www.ebay.com/itm/Toy-Lens-11mm-f-1-4-lens-GH2-AF100-GF2-G3-EP2-EPL2-/260784291391?pt=Camera_Lenses&hash=item3cb7f47e3f'
	))

#Yasuhara Lenses
#-----------------------------------

lensList.append(newLens(
	name = 'Nanoha x5 Ultra-Macro f/11',
	man = 'Y',
	ident = 1000,
	aperture = 11,
	born = 2011.12,
	kind = 'macro',
	customShop = 'http://www.yasuhara.co.jp/nanoha/purchase-e.html',
	customShopName = 'Yasuhara',
	amazon = 'http://www.amazon.com/Yasuhara-NANOHAx5-Mirrorless-Cameras-Panasonic/dp/B0076MSDAO'
	))

# Jackar Lenses
#-----------------------------------