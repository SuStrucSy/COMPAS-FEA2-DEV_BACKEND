
from compas_fea2.model import Node


class OpenseesNode(Node):
    """Opensees implementation of the :class:`Node`. \n"""

    __doc__ += Node.__doc__

    def __init__(self, xyz, mass=None, **kwargs):
        super(OpenseesNode, self).__init__(xyz=xyz, mass=mass, **kwargs)

    def jobdata(self):
        # FIXME: the approximation on the floating point is not correct because it depends on the units
        x, y, z = self.xyz
        coordinates = "{0}{1}{2}{3:>15.8f}{2}{4:>15.8f}{2}{5:>15.8f}".format("node ", self.key, " ", x, y, z)

        #NOTE: TEMP method to flatten the mass list, otherwise tuple format error (self.mass is a tuple)
        def flatten_mass(mass):
            for item in mass:
                if isinstance(item, (list, tuple)):
                    yield from flatten_mass(item)
                else:
                    yield item
        flat_mass = list(flatten_mass(self.mass))
        if any(self.mass):
            mass = " -mass " + " ".join(["{:>15.8f}".format(m) for m in flat_mass])
        else:
            mass = ""
        return coordinates + mass
