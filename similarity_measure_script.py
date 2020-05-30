import numpy as np
import scipy.spatial.distance as sd

class similarityMeasure:
    
    '''
    Various similarity measure between two vectors
    '''
    
    def __init__(self, v1, v2):
        
        self.firstVector = v1
        self.secondVector = v2
        
        self.dot_product = np.dot(v1, v2)
        
        
        self.denominator = np.linalg.norm(self.firstVector)**2 + np.linalg.norm(self.secondVector)**2 - self.dot_product
        
        if self.denominator ==0:
            #print("denominator is zero, select different vector")
            return None
    
    def calculate_TanimotoCoefficient(self):
        similarity_coeff = self.dot_product / self.denominator
        return similarity_coeff
    
    def calculate_cosineSimilarity(self):
        similarity_coeff = self.dot_product / (np.linalg.norm(self.firstVector)* np.linalg.norm(self.secondVector))
        return similarity_coeff
    
    def calculate_cosine_root(self):
        cosine_sim = np.sqrt(self.dot_product)
        return cosine_sim
    
    
    
def calculate_euclidean_distance(m_by_n_array):
        '''
        Calculate euclidean distance between list of list in a single form
        ex: list = [[1,2,3], [2,4,5]]
        '''
        distance = sd.pdist(m_by_n_array, metric = 'euclidean')
        return distance

def calculate_gaussian(pass_list):
    
    '''
    Calculate gaussian distribution by calculating mean and standard deviation
    '''
    sigma = np.std(pass_list)
    mu = np.mean(pass_list)
    gauss = [1/(sigma * np.sqrt(2* np.pi)) * np.exp(-(i - mu)**2 / (2* sigma **2)) for i in pass_list]
    return gauss

def calculate_average_between_two_list_of_list(l1, l2):
    '''
    calculate average between two. lists
    '''
    mean_list = []
    for i in range(len(l1)):
        mean = [(x1+y1)/2 for x1, y1 in zip(l1[i], l2[i])]
        mean_list.append(mean)
    return mean
    
