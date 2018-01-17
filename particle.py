class Particle:

    def init(self,dim, max_param):
        self.position = max_param*(np.random.rand(dim))
    
        self.momentum = (max_param/10)*np.random.rand(dim)