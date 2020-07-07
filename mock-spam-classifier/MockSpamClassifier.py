import random
import numpy as np

class MockSpamClassifier():

    def __init__(self):
        pass

    def predict(self, text, feature_names=None): #List[Tuple[float, float]]:
        """
        Randomly guess if the text is a spam message. The output returns the random probability of text being spam
        """
        guess_prob = random.uniform(0, 1)
        guess_class = "spam" if guess_prob>0.5 else "ham"
        return np.array([guess_prob, guess_class])


# if __name__== "__main__":

#     text = 'please click this link to win the price'
#     #vect_path=Path('/Users/sandhya.sandhya/Desktop/data/doc/data'),
#     sc = KerasSpamClassifier(model_path=Path('./model'))
#     res = sc.predict(text, feature_names=None)
#     print(res)