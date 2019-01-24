import numpy as np

class Mask:
    def __init__(self, file='data/harps/masks/G2.mas',constant_v=False,disp=1.):
        """
        A simple mask class.

        Reads in a .mas file that has the following columns:
         left    right     weights
        """
        self.wi, self.wf, self.weight = np.loadtxt(file,unpack=True,dtype=np.float64)
        self.wi = airtovac.airtovac(self.wi)
        self.wf = airtovac.airtovac(self.wf)
        self.wmid = 0.5*(self.wi+self.wf)
        width_in_km = self.wmid * disp / (aconst.c.value/1.e3)
        self.wi_v = self.wmid - width_in_km/2.
        self.wf_v = self.wmid + width_in_km/2.
        if constant_v:
            self.wi = self.wi_v
            self.wf = self.wf_v
