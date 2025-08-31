from compas_fea2.model import Model, Part, Node, BeamElement, ElasticIsotropic, ElasticOrthotropic, BeamSection, RectangularSection, PipeSection
from compas_fea2.problem import Problem, StaticStep, LoadCombination
from compas_fea2.results import DisplacementFieldResults, ReactionFieldResults, StressFieldResults
from compas_fea2_opensees import TEMP
import compas_fea2
import os

'''
Author(s): Andrew Liew (github.com/andrewliew), Moosa Saboor (https://github.com/Moosa-Saboor)
Originally written/conceptualized for compas_fea by Andrew Liew, re-written completely for compas_fea2 by Moosa Saboor
'''

compas_fea2.set_backend("compas_fea2_opensees")
mdl = Model(name="Beam_bathe")
prt = mdl.add_part(Part(name="Beam_bathe_analysis"))

prt.ndm = 3
prt.ndf = 6
steel = ElasticIsotropic(name="Steel", E=100000000, v=0.3, density=7850)

section_beam1 = RectangularSection(w=1, h=1, material=steel)

nodes_data = {0: (70.710678, -29.289322, 0.000000),
  1: (0.000000, 0.000000, 0.000000),
  2: (9.801714, -0.481527, 0.000000),
  3: (19.509032, -1.921472, 0.000000),
  4: (29.028468, -4.305966, 0.000000),
  5: (38.268343, -7.612047, 0.000000),
  6: (47.139674, -11.807874, 0.000000),
  7: (55.557023, -16.853039, 0.000000),
  8: (63.439328, -22.698955, 0.000000),}

elements_data = [
  (1, 2),
  (2, 3),
  (3, 4),
  (4, 5),
  (5, 6),
  (6, 7),
  (7, 8),
  (8, 0),]

nodes = {}
for nid, xyz in nodes_data.items():
    nodes[nid] = prt.add_node(Node(name=nid, xyz=xyz))

for nodes_ids in elements_data:
    n1 = nodes[nodes_ids[0]]
    n2 = nodes[nodes_ids[1]]
    prt.add_element(BeamElement(nodes=[n1, n2], section=section_beam1, frame=[1,1,1]))

support_node = prt.find_closest_nodes_to_point((0.0, 0.0, 0.0), single=True)
loaded_node = prt.find_closest_nodes_to_point((70.710678, -29.289322, 0.000000), single=True)
mdl.add_fix_bc(support_node)

# mdl.show(show_bcs=0.005)

prb = mdl.add_problem(Problem(name="BeamBatheAnalysis"))
stp = prb.add_step(StaticStep(name="StaticStep"))

stp.combination = LoadCombination.SLS()
stp.add_uniform_node_load(nodes=loaded_node, load_case="LL", x=0.0, y=0.0, z=600, xx=0.0, yy=0.0, zz=0.0)

stp.add_outputs([DisplacementFieldResults])
prb.analyse_and_extract(problems=[prb], path=os.path.join(TEMP, prb.name), Verbose=True)

stp.show_deformed(scale_results=1, show_original=0.1, show_bcs=0.003, show_loads=0.001)

