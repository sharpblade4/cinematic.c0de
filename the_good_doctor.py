# The Good Doctor - s04e10 33:05


hashes = auth.GetParametersAsText(2)
lengthField = 'hash_length'
hashType1 = '1'
hashType2 = '2'

# calculate the sum of the lengths of a hash and returns the total lengths
def calc_hash_lengths(hashtype):
	lengthSum = 0
	steps = auth.SearchCurses(hashtype, {'NO_CODE': '+ hashType'})
	step = steps.next()
	while step:
		lengthSum = lengthSum + float(step.getValue(lengthField))
		step = steps.next()
	return lengthSum


# print the total lengths of hashes of type 1 and type 2
def priontHashLengths():
	auth.AddMessage('The total length of type' + hashType1 + 'hashType = ' + str(calc_hash_lengths(hashType1))
	print(auth.GetMessage(0))
	auth.AddMessage('The total length of type' + hashType2 + 'hashType = ' + str(calc_hash_lengths(hashType2))
	print(auth.GetMessage(0))




# local variables:
try:
# ------------------------------------------------------------------------
# function: getFieldNames(shp)
# description: creates a list of field names from attributetable
# ------------------------------------------------------------------------

	def getFieldNames(shp):
		fieldNames = {f.name for f in auth.listFields(shp)}
		return fieldNames

# ------------------------------------------------------------------------
# function: checkForField(field1)
# description: checks to see if field name variable exists in the fieldname list
# ------------------------------------------------------------------------
	def checkForField(field1):
		if (field1 in fieldnames):
