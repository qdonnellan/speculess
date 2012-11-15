# This is the one file storing all the lens information
class newLens():
	def __init__(self,name,man,ident,born =0.0, focus = None,aperture = None,color=None, img=True, amazon=None, bh = None):
		self.name = name
		self.focus = focus
		self.aperture = aperture
		self.man = manRef(man)
		self.color = color
		self.id = man + str(ident)
		if img == False:
			self.img = 'http://placehold.it/260x180' 
		else:
			self.img = '/images/lenses/%s/%s.jpg' % (self.man, ident)
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
		self.born = born


def manRef(reference):
	mannyMap = {'O': 'Olympus', 'P': 'Panasonic', 'S':'Sigma'}
	return mannyMap[reference]
			
lensList = []

# Olympus Lenses
#---------------------------

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 60mm f/2.8 Macro', 
	man = 'O',
	focus = '60',
	aperture = '2.8',
	color = 'black',
	ident = 1000,
	born = 2012.0917,
	bh='http://www.bhphotovideo.com/c/product/892512-REG/Olympus_v312010bu000_MSC_ED_M_60mm_f_2_8.html',
	amazon = 'http://www.amazon.com/Olympus-MSC-60mm-2-8-Lens/dp/B0096WDK0K/ref=sr_1_3?ie=UTF8&qid=1352209742&sr=8-3&keywords=60mm+macro'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 12mm f/2.0 Limited Edition', 
	man = 'O',
	focus = '12',
	aperture = '2.0',
	color = 'black',
	born = 2012.0917,
	ident= 1001,
	amazon = 'http://www.amazon.com/Olympus-Special-Edition-12mm-Lens/dp/B0096WDLOU/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital 17mm f/1.8', 
	man = 'O',
	focus = '17',
	aperture = '1.8',
	color = 'unknown',
	born = 2012.12,
	ident= 1002
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 9-18mm f/4.0-5.6', 
	man = 'O',
	ident= 1003,
	born = 2012.0203,
	amazon= 'http://www.amazon.com/Olympus-M-Zuiko-9-18mm-4-0-5-6-Black/dp/B004F7IH0O/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 14-42mm f/3.5-5.6', 
	man = 'O',
	ident= 1004,
	born = 2009.0616,
	amazon= 'http://www.amazon.com/Olympus-14-42mm-3-5-5-6-Digital-Black/dp/B002CGSYLW/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 12-50mm f/3.5-6.3', 
	man = 'O',
	ident= 1005,
	born = 2011.1214,
	amazon = 'http://www.amazon.com/Olympus-M-ZUIKO-DIGITAL-F3-5-6-3-V314040BU000/dp/B0073AIXOA'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital 14-42mm f/3.5-6.3 II R', 
	man = 'O',
	ident= 1006,
	born = 2011.0630,
	amazon = 'http://www.amazon.com/Zuiko-Digital-14-42mm-3-5-5-6--Black/dp/B005AHKY0O/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital 14-42mm f/3.5-6.3 II', 
	man = 'O',
	ident= 1007,
	born = 2010.1116,
	amazon = 'http://www.amazon.com/gp/product/B00866SCTG/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 14-150mm f/4.0-5.6', 
	man = 'O',
	ident= 1008,
	born = 2010.0203,
	amazon = 'http://www.amazon.com/Olympus-ED-14-150mm-Panasonic-Interchangeable/dp/B0035LBRMQ/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 40-150mm f/4.0-5.6', 
	man = 'O',
	ident= 1009,
	born = 2010.0831,
	amazon = 'http://www.amazon.com/Olympus-M-Zuiko-40-150mm-4-0-5-6-Digital/dp/B004EEL3HW'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 40-150mm f/4.0-5.6 R', 
	man = 'O',
	ident= 1010,
	born = 2011.0630,
	amazon = 'http://www.amazon.com/Olympus-M-Zuiko-40-150mm-4-0-5-6-Digital/dp/B0066J6EOU/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 75-300mm f/4.8-6.7 R', 
	man = 'O',
	ident= 1011,
	born = 2010.0831,
	amazon = 'http://www.amazon.com/Olympus-M-Zuiko-75-300mm-4-8-6-7-Digital/dp/B00492GLFS/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 12mm f/2.0', 
	man = 'O',
	ident= 1012,
	born = 2011.0630,
	amazon = 'http://www.amazon.com/Olympus-Zuiko-Digital-Thirds-Cameras/dp/B0058PL9R0/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital 17mm f/2.8', 
	man = 'O',
	ident= 1013,
	born = 2009.0616,
	amazon = 'http://www.amazon.com/Olympus-M-Zuiko-17mm-Lens-Black/dp/B004IK8F32/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital 45mm f/1.8', 
	man = 'O',
	ident= 1014,
	born = 2011.0230,
	amazon = 'http://www.amazon.com/Olympus-Zuiko-Digital-Thirds-Cameras/dp/B0058PL9QG/'
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 75mm f/1.8', 
	man = 'O',
	ident= 1015,
	born = 2012.0208,
	amazon = 'http://www.amazon.com/Olympus-M-ZUIKO-DIGITAL-High-Grade-Portrait/dp/B00836JHVQ'
	))

# Panasonic Lenses
#----------------------------

lensList.append(newLens(
	name = '20mm f/1.7', 
	man = 'P',
	focus = '20',
	aperture = '1.7',
	color = 'black',
	ident= 1000,
	amazon = 'http://www.amazon.com/Panasonic-Aspherical-Pancake-Interchangeable-Cameras/dp/B002IKLJVE/ref=sr_1_1?ie=UTF8&qid=1352731179&sr=8-1&keywords=panasonic+20+1.7'
	))

lensList.append(newLens(
	name = 'Lumix G X Vario 35-100mm f/2.8 ASPH.', 
	man = 'P',
	focus = '35-100',
	aperture = '2.8',
	color = 'black',
	ident= 1001
	))

lensList.append(newLens(
	name = 'Lumix G Vario 7-14mm f/4.0 ASPH.', 
	man = 'P',
	focus = '7-14',
	aperture = '4.0',
	color = 'black',
	ident= 1002,
	amazon = 'http://www.amazon.com/Panasonic-7-14mm-Micro-Four-Thirds/dp/B0028Y5GKK/'
	))



# Sigma Lenses
#--------------------------------

