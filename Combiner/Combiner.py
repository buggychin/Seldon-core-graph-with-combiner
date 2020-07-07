import numpy as np
import json

class Combiner(object):

	def aggregate(self, Xs, features_names=None):
		"""average out the probabilities from multiple classifier and return that as a result"""
		try:
			return [x.tolist() for x in Xs]
		except Exception as e:
			return str(e)

		return [type(x) for x in Xs]
		i=0
		for x in Xs:
			print("==================================")
			print(i)
			print(x, type(x))
			i+=1
			print()
			print("==================================")
			result.append(x)
		return np.array(result)



# if __name__== "__main__":
#	 clf1_res = np.array(['0.80', 'Spam'])
#	 clf2_res = np.array(['0.9959868467126312e-04', 'Spam'])

#	 example = np.array([clf1_res, clf2_res])
#	 combine = Combiner()
#	 res = combine.aggregate(example, features_names=None)
#	 print(res)




