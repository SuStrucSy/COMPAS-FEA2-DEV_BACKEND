from compas_fea2.model import Model, Part, Node, TrussElement, ElasticIsotropic, TrussSection
from compas_fea2.problem import Problem, StaticStep, LoadCombination
from compas_fea2.results import DisplacementFieldResults, ReactionFieldResults, StressFieldResults
from compas_fea2_opensees import TEMP
import compas_fea2
import os

# Set the backend
compas_fea2.set_backend("compas_fea2_opensees")
mdl = Model(name="TrussTower")
prt = mdl.add_part(Part(name="Truss-3"))
prt.ndm = 3
prt.ndf = 3


# Materials
steel = ElasticIsotropic(name="Steel", E=200000000000, v=0.3, density=7850)

# Sections

mainTruss = TrussSection(name='sec_main', A=0.0001, material=steel)

nodes_data ={0: (0.250000, 0.250000, 2.500000),
  1: (0.750000, 0.250000, 2.500000),
  2: (0.750000, 0.750000, 2.500000),
  3: (0.250000, 0.750000, 2.500000),
  4: (0.375000, 0.375000, 3.750000),
  5: (0.625000, 0.375000, 3.750000),
  6: (0.625000, 0.625000, 3.750000),
  7: (0.375000, 0.625000, 3.750000),
  8: (0.500000, 0.500000, 5.000000),
  9: (0.000000, 0.000000, 0.000000),
  10: (0.125000, 0.125000, 1.250000),
  11: (0.000000, 1.000000, 0.000000),
  12: (0.125000, 0.875000, 1.250000),
  13: (1.000000, 0.000000, 0.000000),
  14: (0.875000, 0.125000, 1.250000),
  15: (1.000000, 1.000000, 0.000000),
  16: (0.875000, 0.875000, 1.250000),
  17: (0.125000, 0.500000, 1.250000),
  18: (0.500000, 0.125000, 1.250000),
  19: (0.875000, 0.500000, 1.250000),
  20: (0.500000, 0.875000, 1.250000),}

lines = [(0, 1),
  (1, 2),
  (2, 3),
  (3, 0),
  (4, 5),
  (5, 6),
  (6, 7),
  (7, 4),
  (0, 4),
  (4, 8),
  (3, 7),
  (7, 8),
  (1, 5),
  (5, 8),
  (2, 6),
  (6, 8),
  (9, 10),
  (10, 0),
  (11, 12),
  (12, 3),
  (13, 14),
  (14, 1),
  (15, 16),
  (16, 2),
  (11, 17),
  (17, 9),
  (9, 18),
  (18, 13),
  (19, 13),
  (19, 15),
  (20, 15),
  (20, 11),
  (10, 18),
  (18, 14),
  (14, 19),
  (19, 16),
  (12, 20),
  (20, 16),
  (12, 17),
  (17, 10),
  (19, 2),
  (19, 1),
  (2, 20),
  (20, 3),
  (0, 17),
  (3, 17),
  (0, 18),
  (1, 18),
  (2, 0),
  (7, 5),
  (7, 0),
  (7, 2),
  (5, 0),
  (5, 2),
  (17, 18),
  (18, 19),
  (19, 20),
  (20, 17),
  (20, 18),
]

constrained_nodes_coordinates = [(0.000000, 0.000000, 0.000000), (0.000000, 1.000000, 0.000000), (1.000000, 1.000000, 0.000000), (1.000000, 0.000000, 0.000000),]
loaded_nodes_coordinates = [(0.500000, 0.500000, 5.000000)]

nodes = {}
for nid, xyz in nodes_data.items():
    nodes[nid] = prt.add_node(Node(name=nid, xyz=xyz))

iteration = 1
for nodes in lines:
    n1 = prt.find_closest_nodes_to_point(nodes_data[nodes[0]], single = True)
    n2 = prt.find_closest_nodes_to_point(nodes_data[nodes[1]], single = True)
    prt.add_element(TrussElement(name=str(iteration), nodes=[n1, n2], section=mainTruss))
    iteration += 1

for coords in constrained_nodes_coordinates:
    n = prt.find_closest_nodes_to_point(coords, single=True)
    mdl.add_pin_bc(n)

# mdl.show(show_bcs=0.0003)

prb = mdl.add_problem(Problem(name="TrussTowerAnalysis"))
stp = prb.add_step(StaticStep(name="StaticStep"))

stp.combination = LoadCombination.SLS()
for coords in loaded_nodes_coordinates:
    n = prt.find_closest_nodes_to_point(coords, single=True)
    stp.add_uniform_node_load(nodes=n, load_case="LL", x=2000.0, y=-1000, z=-100000, xx=0.0, yy=0.0, zz=0.0)

stp.add_outputs([DisplacementFieldResults])
prb.analyse_and_extract(problems=[prb], path=os.path.join(TEMP, prb.name), Verbose=True)

stp.show_deformed(scale_results=10, show_original=0.1, show_bcs=0.0003, show_loads=0.000005)
