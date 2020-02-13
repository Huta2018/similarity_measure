import numpy as np
class SimilarityMeasure:
    
    def __init__(self, v1, v2):
        
        self.firstVector = v1
        self.secondVector = v2
        
        self.dot_product = np.dot(v1, v2)
        
        
        self.denominator = np.linalg.norm(self.firstVector)**2 + np.linalg.norm(self.secondVector)**2 - self.dot_product
        
        if self.denominator ==0:
            print("denominator is zero select different vector")
            return None
    
    def calculate_TanimotoCoefficient(self):
        similarity_coeff = self.dot_product / self.denominator
        return similarity_coeff
    
    def calculate_cosineSimilarity(self):
        similarity_coeff = self.dot_product / (np.linalg.norm(self.firstVector)* np.linalg.norm(self.secondVector))
        return similarity_coeff  
