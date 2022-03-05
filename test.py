from stillingerweber import StillingerWeber as SW
import numpy as np
import pairlist as pl
import networkx as nx
import itertools as it

L = 6.381821280722142
cell = np.array([L, L, L])
cell = np.diag(cell)
celli = np.linalg.inv(cell)

atoms = np.fromstring("""
0.0 0.0 0.0
3.190910640361071 3.190910640361071 0.0
3.190910640361071 0.0 3.190910640361071
0.0 3.190910640361071 3.190910640361071
1.5954553201805355 1.5954553201805355 1.5954553201805355
4.786365960541606 4.786365960541606 1.5954553201805355
4.786365960541606 1.5954553201805355 4.786365960541606
1.5954553201805355 4.786365960541606 4.786365960541606
""", sep=" ").reshape(-1, 3)

rpos = atoms @ celli

mw = SW(epsilon=6.189, sigma=2.3925, lambda_=23.15)
rc = mw.sigma * mw.a

g = nx.Graph([(i, j)
             for i, j, d in pl.pairs_iter(rpos, rc, cell)])

e2 = 0.0
for i, j in g.edges():
    dij = rpos[j] - rpos[i]
    dij -= np.floor(dij + 0.5)
    rij = np.linalg.norm(dij @ cell)
    e2 += mw.f2(rij)
e3 = 0.0
for i in g:
    ri = rpos[i]
    for j, k in it.combinations(g[i], 2):
        rj = rpos[j]
        rk = rpos[k]
        dij = rj - ri
        dij -= np.floor(dij + 0.5)
        dik = rk - ri
        dik -= np.floor(dik + 0.5)
        dij = dij @ cell
        dik = dik @ cell
        rij = np.linalg.norm(dij)
        rik = np.linalg.norm(dik)
        costhetajik = dij @ dik / (rij * rik)
        ep = mw.h(rij, rik, costhetajik)
        e3 += ep
print(f"{(e2+e3)/len(atoms)} kcal/mol Energy of a diamond structure.")


# more redundant calculation but simpler
e = 0.0
for i in g:
    v = rpos[g[i]] - rpos[i]
    v -= np.floor(v + 0.5)
    e += mw.localenergy(v @ cell)
print(f"{(e)/len(atoms)} kcal/mol Energy of a diamond structure.")
