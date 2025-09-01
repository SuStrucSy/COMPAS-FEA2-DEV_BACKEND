
from compas_fea2.model import ElasticIsotropic
from compas_fea2.model import ElasticOrthotropic
from compas_fea2.model import ElasticPlastic
from compas_fea2.model import Stiff
from compas_fea2.model import UserMaterial
from compas_fea2.model import ElasticMultiLinear
from compas_fea2.model import MultiLinear
from compas_fea2.model import Pinching4

# ==============================================================================
# Specifics
# ==============================================================================

class OpenseesElasticMultiLinear(ElasticMultiLinear):
    """"""
    
    __doc__ += ElasticMultiLinear.__doc__
    __doc__ += """
    Opensees implementation of :class:`compas_fea2.model.materials.ElasticMultiLinear`.\n
    """

    def __init__(self, *, eta, strain, stress, **kwargs):
        super(OpenseesElasticMultiLinear, self).__init__(eta=eta, strain=strain, stress=stress, **kwargs)
        self.eta = eta
        self.strain = strain
        self.stress = stress
        self.type = "ElasticMultiLinear"

    def jobdata(self):
        return f"nDMaterial ElasticMultiLinear {self.key} {self.eta} {{{' '.join(str(s) for s in self.strain)}}} {{{' '.join(str(s) for s in self.stress)}}}\n"

class OpenseesMultiLinear(MultiLinear):
    """"""
    
    __doc__ += MultiLinear.__doc__
    __doc__ += """
    Opensees implementation of :class:`compas_fea2.model.materials.MultiLinear`.\n
    """
    
    def __init__(self, *, pts, **kwargs):
        super(OpenseesMultiLinear, self).__init__(pts=pts, **kwargs)
        self.pts = pts
        self.type = "MultiLinear"
        
    def jobdata(self):
        return f"uniaxialMaterial MultiLinear {self.key} {{{' '.join(str(s) for s in self.pts)}}}\n"

class OpenseesPinching4(Pinching4):
    """"""
    
    __doc__ += Pinching4.__doc__
    __doc__ += """
    Opensees implementation of :class:`compas_fea2.model.materials.Pinching4`.\n
    """

    def __init__(self,*, ePf1, ePf2, ePf3, ePf4, ePd1, ePd2, ePd3, ePd4, eNf1, eNf2, eNf3, eNf4, eNd1, eNd2, eNd3, eNd4, rDispP, fFoceP, uForceP, rDispN, fFoceN, uForceN, gK1, gK2, gK3, gK4, gKLim, gD1, gD2, gD3, gD4, gDLim, gF1, gF2, gF3, gF4, gFLim, gE, dmgType, **kwargs):
        super(OpenseesPinching4, self).__init__(ePf1=ePf1, ePf2=ePf2, ePf3=ePf3, ePf4=ePf4, ePd1=ePd1, ePd2=ePd2, ePd3=ePd3, ePd4=ePd4, eNf1=eNf1, eNf2=eNf2, eNf3=eNf3, eNf4=eNf4, eNd1=eNd1, eNd2=eNd2, eNd3=eNd3, eNd4=eNd4, rDispP=rDispP, fFoceP=fFoceP, uForceP=uForceP, rDispN=rDispN, fFoceN=fFoceN, uForceN=uForceN, gK1=gK1, gK2=gK2, gK3=gK3, gK4=gK4, gKLim=gKLim, gD1=gD1, gD2=gD2, gD3=gD3, gD4=gD4, gDLim=gDLim, gF1=gF1, gF2=gF2, gF3=gF3, gF4=gF4, gFLim=gFLim, gE=gE, dmgType=dmgType, **kwargs)
        self.ePf1 = ePf1
        self.ePf2 = ePf2
        self.ePf3 = ePf3
        self.ePf4 = ePf4
        self.ePd1 = ePd1
        self.ePd2 = ePd2
        self.ePd3 = ePd3
        self.ePd4 = ePd4
        self.eNf1 = eNf1
        self.eNf2 = eNf2
        self.eNf3 = eNf3
        self.eNf4 = eNf4
        self.eNd1 = eNd1
        self.eNd2 = eNd2
        self.eNd3 = eNd3
        self.eNd4 = eNd4
        self.rDispP = rDispP
        self.fFoceP = fFoceP
        self.uForceP = uForceP
        self.rDispN = rDispN
        self.fFoceN = fFoceN
        self.uForceN = uForceN
        self.gK1 = gK1
        self.gK2 = gK2
        self.gK3 = gK3
        self.gK4 = gK4
        self.gKLim = gKLim
        self.gD1 = gD1
        self.gD2 = gD2
        self.gD3 = gD3
        self.gD4 = gD4
        self.gDLim = gDLim
        self.gF1 = gF1
        self.gF2 = gF2
        self.gF3 = gF3
        self.gF4 = gF4
        self.gFLim = gFLim
        self.gE = gE
        self.dmgType = dmgType
        
        self.type = "Pinching4"
        
    def jobdata(self):
        return f"uniaxialMaterial Pinching4 {self.key} {self.ePf1} {self.ePf2} {self.ePf3} {self.ePf4} {self.ePd1} {self.ePd2} {self.ePd3} {self.ePd4} {self.eNf1} {self.eNf2} {self.eNf3} {self.eNf4} {self.eNd1} {self.eNd2} {self.eNd3} {self.eNd4} {self.rDispP} {self.fFoceP} {self.uForceP} {self.rDispN} {self.fFoceN} {self.uForceN} {self.gK1} {self.gK2} {self.gK3} {self.gK4} {self.gKLim} {self.gD1} {self.gD2} {self.gD3} {self.gD4} {self.gDLim} {self.gF1} {self.gF2} {self.gF3} {self.gF4} {self.gFLim} {self.gE} {self.dmgType}\n"
    
# ==============================================================================
# linear elastic
# ==============================================================================


class OpenseesElasticOrthotropic(ElasticOrthotropic):
    """"""

    __doc__ += ElasticOrthotropic.__doc__
    __doc__ += """
    
    OpenSees implementation of :class:`compas_fea2.model.materials.ElasticIsotropic`.\n

    """

    def __init__(self, *, Ex, Ey, Ez, vxy, vyz, vzx, Gxy, Gyz, Gzx, density, **kwargs):
        super(ElasticOrthotropic, self).__init__(Ex=Ex, Ey=Ey, Ez=Ez, vxy=vxy, vyz=vyz, vzx=vzx, Gxy=Gxy, Gyz=Gyz, Gzx=Gzx, density=density, **kwargs)
        self.Ex = Ex
        self.Ey = Ey
        self.Ez = Ez
        self.vxy = vxy
        self.vyz = vyz
        self.vzx = vzx
        self.Gxy = Gxy
        self.Gyz = Gyz
        self.Gzx = Gzx
        self.density = density

        self.type = "ElasticOrthotropic"
    
    def jobdata(self):
        return f"nDMaterial ElasticOrthotropic {self.key} {self.Ex} {self.Ey} {self.Ez} {self.vxy} {self.vyz} {self.vzx} {self.Gxy} {self.Gyz} {self.Gzx} {self.density}\n"


class OpenseesElasticIsotropic(ElasticIsotropic):
    """OpenSees implementation of :class:`compas_fea2.model.materials.ElasticIsotropic`.\n"""

    __doc__ += ElasticIsotropic.__doc__

    def __init__(self, E, v, density, notension=False, **kwargs):
        super(OpenseesElasticIsotropic, self).__init__(E=E, v=v, density=density, **kwargs)
        self.notension = notension
        self.type = "ElasticIsotropic"

    def jobdata(self):
        if not self.notension:
            line = [
                "uniaxialMaterial Elastic {} {}\n".format(self.key, self.E),
                "nDMaterial ElasticIsotropic {} {} {} {}".format(self.key + 1000, self.E, self.v, self.density),
            ]  # FIXME Remove one of the two
        else:
            line = ["uniaxialMaterial ENT {} {}\n".format(self.key, self.E)]
        return "".join(line)


class OpenseesStiff(Stiff):
    """"""

    __doc__ += Stiff.__doc__

    def __init__(self, **kwargs):
        super(OpenseesStiff, self).__init__(**kwargs)
        raise NotImplementedError


# ==============================================================================
# non-linear general
# ==============================================================================


class OpenseesElasticPlastic(ElasticPlastic):
    """"""

    __doc__ += ElasticPlastic.__doc__
    __doc__ += """
    Warning
    -------
    Currently not available in Opensees.

    """

    def __init__(self, *, E, v, density, strain_stress, **kwargs):
        super(OpenseesElasticPlastic, self).__init__(E=E, v=v, density=density, strain_stress=strain_stress, **kwargs)
        raise NotImplementedError


# ==============================================================================
# User-defined Materials
# ==============================================================================


class OpenseesUserMaterial(UserMaterial):
    """"""

    __doc__ += ElasticPlastic.__doc__
    __doc__ += """
    Warning
    -------
    Currently not available in Opensees.

    """

    def __init__(self, **kwargs):
        super(OpenseesUserMaterial, self).__init__(self, **kwargs)
        raise NotImplementedError
