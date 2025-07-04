from compas_fea2.model import Model, Part, Node, TrussElement, ElasticIsotropic, TrussSection
from compas_fea2.problem import Problem, StaticStep
from compas_fea2.model.shapes import Circle
from compas_fea2_opensees import TEMP
import compas_fea2
import os

# Set the backend
compas_fea2.set_backend("compas_fea2_opensees")


mdl = Model(name="TrussModel")
prt = mdl.add_part(Part(name="TrussPart"))
prt.ndm = 2
prt.ndf = 3

#Materials
steel = ElasticIsotropic(name="Steel", E=3000.0, v=0.0, density=0.0)
face = Circle(radius=0.05)
section = TrussSection(name="TrussSec", A=10.0, material=steel,shape=face)

#nodal coords
coords = {
    1: (0.0, 0.0, 0.0),
    2: (144.0, 0.0, 0.0),
    3: (72.0, 96.0, 0.0),
}

nodes = {}
for nid, xyz in coords.items():
    nodes[nid] = prt.add_node(Node(name=nid, xyz=xyz))

elements = [
    (1, 1, 3),
    (2, 3, 2),
    (3, 1, 2),
]

for eid, n1, n2 in elements:
    prt.add_element(TrussElement(
        name=str(eid),
        nodes=[nodes[n1], nodes[n2]],
        section=section,
        frame=[0, 0, 1]
    ))

mdl.add_fix_bc(nodes[1])
mdl.add_fix_bc(nodes[2])

from compas_fea2.model import PointLoad

load_node = nodes[3]
load = PointLoad(x=100.0, y=-50.0, z=0.0)
prt.add_load(load_node, load)

prb = mdl.add_problem(Problem(name="TrussLoad"))
step = prb.add_step(StaticStep())

prb.analyse_and_extract(path=os.path.join(TEMP, prb.name), verbose=True)

# Visualize deformed shape
step.show_deformed_shape(scale=50)
