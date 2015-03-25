import json


class JSONEncoderBinary(json.JSONEncoder):
	"""
	JSONEncoderBinary subclass that knows how to encode Python data structure at binary string
	"""
	def encode(self, obj):
		"""
		Return a binary string representation of a Python data structure.
		
		>>> JSONEncoderBinary().encode({"foo": ["bar", "baz"]})
		"""
		json_str = super(JSONEncoderBinary, self).encode(obj)
		binaries = list(format(ord(value), 'b') for value in json_str)
		return ''.join(binaries)