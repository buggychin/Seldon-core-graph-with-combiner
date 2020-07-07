import numpy as np

class Lowercase():
    def __init__(self):
        pass

    # def transform_input(self, text_msg, feature_names=None):
    def transform_input(self, text_msg, feature_names=None, meta=None):

        """the translator logic will go here. This shows a use of simple library. But translator service can be a Machine Learning model itself"""
        return np.array([text_msg[0].lower()])



# if __name__== "__main__":
#     t = Translator()
#     example = np.array(['Wie läuft dein Tag'])
#     translated = t.transform_input(example)
#     print(translated)




