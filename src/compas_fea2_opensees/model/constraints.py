from compas_fea2.model import TieConstraint


class OpenseesTieConstraint(TieConstraint):
    def __init__(self, master, slave, **kwargs):
        super(OpenseesTieConstraint, self).__init__(master, slave, tol=None, **kwargs)
        self.master = master
        self.slave = slave

        _freedoms = kwargs.get("freedoms") if "freedoms" in kwargs else [1, 2, 3, 4, 5, 6]
        self.freedoms = " ".join(str(freedom) for freedom in _freedoms)
    
    def jobdata(self):
        """Return the OpenSees command for equal DOF constraint.  """
        return f"equalDOF {self.master} {self.slave} {self.freedoms}"

class OpenseesFixConstraint(TieConstraint):
    """Opensees implementation of the :class:`FixConstraint`."""

    def __init__(self, node, **kwargs):
        super(OpenseesFixConstraint, self).__init__(node=node, **kwargs)
        self.node = node
        
        _freedoms = kwargs.get("freedoms") if "freedoms" in kwargs else [1, 1, 1, 1, 1, 1]
        self.freedoms = " ".join(str(freedom) for freedom in _freedoms)

    def jobdata(self):
        """Return the OpenSees command for fixed constraint."""
        return f"fix {self.node.key} {self.freedoms}"