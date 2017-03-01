import pytest

import mbuild as mb


class BaseTest:

    @pytest.fixture(autouse=True)
    def initdir(self, tmpdir):
        tmpdir.chdir()

    @pytest.fixture
    def ethane(self):
        from mbuild.examples import Ethane
        return Ethane()

    @pytest.fixture
    def methane(self):
        from mbuild.examples import Methane
        return Methane()

    @pytest.fixture
    def h2o(self):
        from mbuild.lib.moieties import H2O
        return H2O()

    @pytest.fixture
    def ch2(self):
        from mbuild.lib.moieties import CH2
        return CH2()

    @pytest.fixture
    def ester(self):
        from mbuild.lib.moieties import Ester
        return Ester()

    @pytest.fixture
    def ch3(self):
        from mbuild.lib.moieties import CH3
        return CH3()

    @pytest.fixture
    def c3(self):
        from mbuild.lib.atoms import C3
        return C3()

    @pytest.fixture
    def n4(self):
        from mbuild.lib.atoms import N4
        return N4()

    @pytest.fixture
    def betacristobalite(self):
        from mbuild.lib.surfaces import Betacristobalite
        return Betacristobalite()

    @pytest.fixture
    def propyl(self):
        from mbuild.examples import Alkane
        return Alkane(3, cap_front=True, cap_end=False)

    @pytest.fixture
    def hexane(self, propyl):
        class Hexane(mb.Compound):
            def __init__(self):
                super(Hexane, self).__init__()

                self.add(propyl, 'propyl1')
                self.add(mb.clone(propyl), 'propyl2')

                mb.force_overlap(self['propyl1'],
                                 self['propyl1']['down'],
                                 self['propyl2']['down'])
        return Hexane()

    @pytest.fixture
    def sixpoints(self):
        molecule = mb.Compound()
        molecule.add(mb.Particle(name='C', pos=[5, 5, 5]), label='middle')
        molecule.add(mb.Particle(name='C', pos=[6, 5, 5]), label='right')
        molecule.add(mb.Particle(name='C', pos=[4, 5, 5]), label='left')
        molecule.add(mb.Port(anchor=molecule[0]), label='up')
        mb.translate(molecule['up'], [0, 1, 0])
        molecule.add(mb.Port(anchor=molecule[0]), label='down')
        mb.translate(molecule['down'], [0, -1, 0])
        molecule.add(mb.Particle(name='C', pos=[5, 5, 6]), label='front')
        molecule.add(mb.Particle(name='C', pos=[5, 5, 4]), label='back')
        molecule.generate_bonds('C', 'C', 0.9, 1.1)
        return molecule
