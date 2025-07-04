from compas_fea2.model import Model, Part, Node, ElasticIsotropic, SolidSection
from compas_fea2.model.shapes import Rectangle
from compas_fea2.problem import Problem, StaticStep
from compas_fea2_opensees import TEMP
import compas_fea2
import os

compas_fea2.set_backend("compas_fea2_opensees")

#init
mdl = Model(name="SolidBeam")
prt = mdl.add_part(Part(name="SolidBeamPart"))
prt.ndm = 2
prt.ndf = 2

#Mats
steel = ElasticIsotropic(name="Steel", E=3000.0, v=0.25, density=0.0)
section = SolidSection(name="BeamSection", material=steel)

L = 10.0
H = 1.0
nx = 10  # number of divisions along x
ny = 1   # one layer along height

nodes = {}
elements = []
dx = L / nx
dy = H / ny
nid = 1
eid = 1

for j in range(ny + 1):
    for i in range(nx + 1):
        x = i * dx
        y = j * dy
        nodes[(i, j)] = prt.add_node(Node(name=f"N{nid}", xyz=[x, y, 0.0]))
        nid += 1

for j in range(ny):
    for i in range(nx):
        n1 = nodes[(i, j)]
        n2 = nodes[(i+1, j)]
        n3 = nodes[(i+1, j+1)]
        n4 = nodes[(i, j+1)]
        prt.add_element(SolidElement(name=f"E{eid}", nodes=[n1, n2, n3, n4], section=section))
        eid += 1

left_node = nodes[(0, 0)]
right_node = nodes[(nx, 0)]
mdl.add_bc(left_node, ux=None, uy=0.0)
mdl.add_bc(right_node, ux=None, uy=0.0)

top_nodes = [nodes[(i, ny)] for i in range(nx + 1)]
for i in range(nx):
    n1 = top_nodes[i]
    n2 = top_nodes[i+1]
    prt.add_load((n1, n2), FaceLoad(y=-10.0))  # Uniform load in Y

prb = mdl.add_problem(Problem(name="SolidBeamLoad"))
step = prb.add_step(StaticStep())

prb.analyse_and_extract(path=os.path.join(TEMP, prb.name), verbose=True)
step.show_deformed_shape(scale=50.0)
