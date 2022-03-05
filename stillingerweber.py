import numpy as np

__version__ = "0.1"


class StillingerWeber:
    """
    Stillinger and Weber,  Phys. Rev. B, v. 31, p. 5262, (1985)
    """

    def __init__(self,
                 epsilon=2.1683,  # eV
                 sigma=2.0951,   # AA
                 a=1.80,
                 lambda_=21.0,
                 gamma=1.20,
                 costheta0=-1 / 3,
                 A=7.049556277,
                 B=0.6022245584,
                 p=4.0,
                 q=0.0):
        self.epsilon = epsilon
        self.sigma = sigma
        self.a = a
        self.lambda_ = lambda_
        self.gamma = gamma
        self.costheta0 = costheta0
        self.A = A
        self.B = B
        self.p = p
        self.q = q

    def f2(self, r):
        r /= self.sigma
        if r >= self.a:
            return 0
        return self.epsilon * self.A * \
            (self.B / r**self.p - 1 / r**self.q) * np.exp(1 / (r - self.a))

    def h(self, rij, rik, costhetajik):
        rij /= self.sigma
        rik /= self.sigma
        return self.epsilon * self.lambda_ * np.exp(self.gamma / (
            rij - self.a) + self.gamma / (rik - self.a)) * (costhetajik - self.costheta0)**2
