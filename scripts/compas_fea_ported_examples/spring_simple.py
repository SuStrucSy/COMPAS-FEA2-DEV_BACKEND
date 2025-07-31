from compas_fea2.model import Model, Part, Node, ElasticIsotropic, SpringSection, SpringElement
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
mdl = Model(name="Spring_Simple")
prt = mdl.add_part(Part(name="Simple_Spring_analysis"))

prt.ndm = 3
prt.ndf = 6

stiff_spring_mat = ElasticIsotropic(name="stiff_spring", E=10000, v=0.3, density=7850)
soft_spring_mat = ElasticIsotropic(name="soft_spring", E=1000, v=0.3, density=7850)

spring_stiff = SpringSection(name="Stiff_Spring",axial=10000, lateral=0, rotational=0, material=stiff_spring_mat)
spring_soft = SpringSection(name="Soft_Spring", axial=1000, lateral=0, rotational=0, material=soft_spring_mat)

nodes_data = {
    0: (0.944140, 0.000000, 1.017037),
    1: (1.399535, 0.000000, 0.244492),
    2: (0.166173, 0.000000, 0.247203),
    3: (0.434531, 0.000000, 1.518514),
    4: (1.497120, 0.000000, 1.640495),
}

stiff_spring_data = {  
  0: (0, 3),
  1: (0, 4),
  2: (0, 2),}

soft_spring_data = {3: (0, 1)}

nodes = {}
for nid, xyz in nodes_data.items():
    nodes[nid] = prt.add_node(Node(name=nid, xyz=xyz))

for eid, nodes in stiff_spring_data.items():
    n1 = prt.find_closest_nodes_to_point(nodes_data[nodes[0]], single = True)
    n2 = prt.find_closest_nodes_to_point(nodes_data[nodes[1]], single = True)
    prt.add_element(SpringElement(nodes=[n1, n2], section=spring_stiff, frame=[1,1,1]))

for eid, nodes in soft_spring_data.items():
    n1 = prt.find_closest_nodes_to_point(nodes_data[nodes[0]], single = True)
    n2 = prt.find_closest_nodes_to_point(nodes_data[nodes[1]], single = True)
    prt.add_element(SpringElement(nodes=[n1, n2], section=spring_soft, frame=[1,1,1]))

# mdl.show()