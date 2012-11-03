# All operations on the lens list are stored here

def manRef(reference):
	mannyMap = {'O': 'Olympus', 'P': 'Panasonic', 'S':'Sigma'}
	return mannyMap[reference]

def getLens(lensID, allLenses):
    lensFound = None
    for lens in allLenses:
        if str(lens.id) == str(lensID):
            lensFound = lens
    return lensFound

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