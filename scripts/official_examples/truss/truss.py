from compas_fea2.model import Model, Part, Node, TrussElement, ElasticIsotropic, TrussSection
from compas_fea2.problem import Problem, StaticStep, LoadCombination
from compas_fea2.results import DisplacementFieldResults, ReactionFieldResults, StressFieldResults
from compas_fea2_opensees import TEMP
import compas_fea2
import os

# Set the backend
compas_fea2.set_backend("compas_fea2_opensees")

mdl = Model(name="TrussModel")
prt = mdl.add_part(Part(name="Truss-1"))
prt.ndm = 3
prt.ndf = 3

#Materials
steel = ElasticIsotropic(name="Steel", E=3000.0, v=0.0, density=0.0)
section_large = TrussSection(name="TrussSec", A=10.0, material=steel)
section_small = TrussSection(name="TrussSecSmall", A=5.0, material=steel)

#nodal coords
nodes_data = {
    1: (0.0, 0.0, 0.0),
    2: (144.0, 0.0, 0.0),
    3: (168.0, 0.0, 0.0),
    4: (72.0, 96.0, 0.0),
}

nodes = {}
for nid, xyz in nodes_data.items():
    nodes[nid] = prt.add_node(Node(name=nid, xyz=xyz))

for nid in [1, 2, 3]:
    rid = nodes_data[nid]
    n = prt.find_closest_nodes_to_point(rid, single=True)
    mdl.add_pin_bc(n)


for nid in [4]:
    rid = nodes_data[nid]
    n = prt.find_closest_nodes_to_point(rid, single=True)
    mdl.add_specific_bc(n)


elements = [
    (1, 1, 4),
    (2, 2, 4),
    (3, 3, 4),
]

prt.add_element(TrussElement(name=str(1), nodes=[nodes[1], nodes[4]], section=section_large))
prt.add_element(TrussElement(name=str(2), nodes=[nodes[2], nodes[4]], section=section_small))
prt.add_element(TrussElement(name=str(3), nodes=[nodes[3], nodes[4]], section=section_small))

prb = mdl.add_problem(Problem(name="TrussAnalysis"))
stp = prb.add_step(StaticStep(name="StaticStep"))


loaded_node = prt.find_closest_nodes_to_point(nodes_data[4], single = True)
stp.combination = LoadCombination.SLS()
stp.add_uniform_node_load(nodes=loaded_node, load_case="LL", x=100.0, y=-50.0, z=0.0, xx = 0.0, yy = 0.0, zz = 0.0)
stp.add_outputs([DisplacementFieldResults])

#mdl.show(show_bcs = 0.03, show_loads = 10)

prb.analyse_and_extract(problems=[prb], path=os.path.join(TEMP, prb.name), Verbose=True)

stp.show_deformed(scale_results=10, show_original=0.1, show_bcs=0.01)

