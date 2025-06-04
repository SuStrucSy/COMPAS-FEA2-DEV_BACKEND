
from compas_fea2.model import AngleSection
from compas_fea2.model import BeamSection
from compas_fea2.model import GenericBeamSection
from compas_fea2.model import BoxSection
from compas_fea2.model import CircularSection
from compas_fea2.model import HexSection
from compas_fea2.model import ISection
from compas_fea2.model import MassSection
from compas_fea2.model import MembraneSection
from compas_fea2.model import PipeSection
from compas_fea2.model import RectangularSection
from compas_fea2.model import ShellSection
from compas_fea2.model import SolidSection
from compas_fea2.model import SpringSection
from compas_fea2.model import StrutSection
from compas_fea2.model import TieSection
from compas_fea2.model import TrapezoidalSection
from compas_fea2.model import TrussSection

# NOTE in opensees the sectional properties are assigned directly to the element UNLESS it is a nonliner thing...
# in that case there is a tag for the section....aaaaarrrrhhhh


def beam_jobdata(self):
    return "section Elastic {} {} {} {} {} {} {}".format(self.key, self.material.E, self.A, self.Iyy, self.Ixx, self.material.G, self.J)


# ==============================================================================
# 0D
# ==============================================================================
class OpenseesMassSection(MassSection):
    """"""

    __doc__ += MassSection.__doc__

    def __init__(self, mass, **kwargs):
        super(OpenseesMassSection, self).__init__(mass, **kwargs)


class OpenseesSpringSection(SpringSection):
    """"""

    __doc__ += SpringSection.__doc__
    __doc__ += """
    Warning
    -------
    Currently not available in Opensees.

    """

    def __init__(self, axial, lateral, rotational, **kwargs):
        super(OpenseesSpringSection, self).__init__(axial, lateral, rotational, **kwargs)


# ==============================================================================
# 1D
# ==============================================================================


class OpenseesBeamSection(BeamSection):
    """"""

    __doc__ += BeamSection.__doc__
    __doc__ += """
    Warning
    -------
    Currently not available in Opensees.

    """

    def __init__(self, *, A, Ixx, Iyy, Ixy, Avx, Avy, J, g0, gw, material, **kwargs):
        super().__init__(A=A, Ixx=Ixx, Iyy=Iyy, Ixy=Ixy, Avx=Avx, Avy=Avy, J=J, g0=g0, gw=gw, material=material, **kwargs)

    def jobdata(self):
        return beam_jobdata(self)


class OpenseesGenericBeamSection(GenericBeamSection):
    """"""

    __doc__ += GenericBeamSection.__doc__
    __doc__ += """
    Warning
    -------
    Currently not available in Opensees.

    """

    def __init__(self, *, A, Ixx, Iyy, Ixy, Avx, Avy, J, g0, gw, material, **kwargs):
        super().__init__(A=A, Ixx=Ixx, Iyy=Iyy, Ixy=Ixy, Avx=Avx, Avy=Avy, J=J, g0=g0, gw=gw, material=material, **kwargs)

    def jobdata(self):
        return beam_jobdata(self)


class OpenseesAngleSection(AngleSection):
    """"""

    __doc__ += AngleSection.__doc__

    def __init__(self, w, h, t, material, **kwargs):
        super(OpenseesAngleSection, self).__init__(w, h, t, material, **kwargs)

    def jobdata(self):
        return beam_jobdata(self)


class OpenseesBoxSection(BoxSection):
    """"""

    __doc__ += BoxSection.__doc__

    def __init__(self, w, h, t, material, **kwargs):
        super(OpenseesBoxSection, self).__init__(self, w, h, t, material, **kwargs)

    def jobdata(self):
        return beam_jobdata(self)


class OpenseesCircularSection(CircularSection):
    """"""

    __doc__ += CircularSection.__doc__

    def __init__(self, r, material, **kwargs):
        super(OpenseesCircularSection, self).__init__(r, material, **kwargs)

    def jobdata(self):
        return beam_jobdata(self)


class OpenseesHexSection(HexSection):
    """"""

    __doc__ += HexSection.__doc__

    def __init__(self, r, t, material, **kwargs):
        super(OpenseesHexSection, self).__init__(r, t, material, **kwargs)

    def jobdata(self):
        return beam_jobdata(self)


class OpenseesISection(ISection):
    """"""

    __doc__ += ISection.__doc__

    def __init__(self, w, h, tw, tbf, ttf, material, **kwargs):
        super(OpenseesISection, self).__init__(w, h, tw, tbf, ttf, material, **kwargs)

    def jobdata(self):
        return beam_jobdata(self)


class OpenseesPipeSection(PipeSection):
    """"""

    __doc__ += PipeSection.__doc__

    def __init__(self, r, t, material, **kwarg):
        super(OpenseesPipeSection, self).__init__(r, t, material, **kwarg)

    def jobdata(self):
        return beam_jobdata(self)


class OpenseesRectangularSection(RectangularSection):
    """OpenSees implementation of :class:`RectangularSection`. \n"""

    __doc__ += RectangularSection.__doc__

    def __init__(self, w, h, material, **kwargs):
        super(OpenseesRectangularSection, self).__init__(w=w, h=h, material=material, **kwargs)

    def jobdata(self):
        return beam_jobdata(self)


class OpenseesTrapezoidalSection(TrapezoidalSection):
    """"""

    __doc__ += TrapezoidalSection.__doc__
    __doc__ += """
    Warning
    -------
    Currently not available in Opensees.

    """

    def __init__(self, w1, w2, h, material, **kwargs):
        super(OpenseesTrapezoidalSection, self).__init__(w1, w2, h, material, **kwargs)
        raise NotImplementedError("{self.__class__.__name__} is not available in Opensees")


class OpenseesTrussSection(TrussSection):
    """"""

    __doc__ += TrussSection.__doc__
    __doc__ += """
    Warning
    -------
    Currently not available in Opensees.

    """

    def __init__(self, A, material, **kwargs):
        super(OpenseesTrussSection, self).__init__(A, material, **kwargs)


class OpenseesStrutSection(StrutSection):
    """"""

    __doc__ += StrutSection.__doc__
    __doc__ += """
    Warning
    -------
    Currently not available in Opensees.

    """

    def __init__(self, A, material, **kwargs):
        super(OpenseesStrutSection, self).__init__(A, material, **kwargs)
        raise NotImplementedError("{self.__class__.__name__} is not available in Opensees")


class OpenseesTieSection(TieSection):
    """"""

    __doc__ += TieSection.__doc__
    __doc__ += """
    Warning
    -------
    Currently not available in Opensees.

    """

    def __init__(self, A, material, **kwargs):
        super(OpenseesTieSection, self).__init__(A, material, **kwargs)
        raise NotImplementedError("{self.__class__.__name__} is not available in Opensees")


# ==============================================================================
# 2D
# ==============================================================================


class OpenseesShellSection(ShellSection):
    """"""

    __doc__ += ShellSection.__doc__

    def __init__(self, t, material, **kwargs):
        super(OpenseesShellSection, self).__init__(t, material, **kwargs)

    def jobdata(self):
        return "section ElasticMembranePlateSection {} {} {} {} {}".format(self.key, self.material.E, self.material.v, self.t, self.material.density)


class OpenseesMembraneSection(MembraneSection):
    """"""

    __doc__ += MembraneSection.__doc__

    def __init__(self, t, material, **kwargs):
        super(OpenseesMembraneSection, self).__init__(t, material, **kwargs)
        raise NotImplementedError


# ==============================================================================
# 3D
# ==============================================================================


class OpenseesSolidSection(SolidSection):
    """
    Note
    ----
    OpenSees does not have the concept of a solid section.

    """

    __doc__ += SolidSection.__doc__
