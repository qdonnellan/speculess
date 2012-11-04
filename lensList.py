# This is the one file storing all the lens information
class newLens():
	def __init__(self,name,focus,aperture,man,ident,color=None, img=True):
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
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital ED 12mm f/2.0 Limited Edition', 
	man = 'O',
	focus = '12',
	aperture = '2.0',
	color = 'black',
	ident= 1001
	))

lensList.append(newLens(
	name = 'M.Zuiko Digital 17mm f/1.8', 
	man = 'O',
	focus = '17',
	aperture = '1.8',
	color = 'unknown',
	ident= 1002
	))

# Panasonic Lenses
#----------------------------

lensList.append(newLens(
	name = '20mm f/1.7', 
	man = 'P',
	focus = '20',
	aperture = '1.7',
	color = 'black',
	ident= 1000
	))

lensList.append(newLens(
	name = 'Lumix G X Vario 35-100mm f/2.8 ASPH.', 
	man = 'P',
	focus = '35-100',
	aperture = '2.8',
	color = 'black',
	ident= 1001
	))



# Sigma Lenses
#--------------------------------

