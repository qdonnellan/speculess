import re

def filterLens(lensList, filterMethod):	
	filteredList = []
	if filterMethod in ['Sigma', 'Olympus', 'Panasonic', 'Tokina', 'Cosina']:
		for lens in lensList:
			if lens.man == filterMethod:
				filteredList.append(lens)

	elif filterMethod in ['f2.0', 'f2.8', 'f4.0']:
		aperture = float(re.sub('f', '', filterMethod))
		for lens in lensList:
			if lens.aperture:
				if lens.aperture <= aperture:
					filteredList.append(lens)

	elif filterMethod in ['tele', 'prime', 'wide', 'zoom', 'macro']:
		for lens in lensList:
			if lens.kind:
				if filterMethod in lens.kind:
					filteredList.append(lens)


	else:
		filteredList = lensList

	return filteredList
