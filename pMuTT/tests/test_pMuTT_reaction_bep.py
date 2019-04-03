# -*- coding: utf-8 -*-
"""
pMuTT.test_pMuTT_model_reaction_bep
Tests for pMuTT module
"""
import unittest
from pMuTT import constants as c
from pMuTT.reaction import Reaction
from pMuTT.reaction.bep import BEP
from pMuTT.statmech import StatMech, presets


class TestBEP(unittest.TestCase):
    def setUp(self):
        self.T = c.T0('K')
        # Factor to convert potential energy to dimensionless number
        dim_factor = c.R('eV/K')*self.T
        self.m = 0.5  # BEP Slope
        self.c = 20.  # BEP Intercept in kcal/mol
        species = {
            'H2': StatMech(name='H2', potentialenergy=2.*dim_factor,
                           **presets['electronic']),
            'O2': StatMech(name='O2', potentialenergy=4.*dim_factor,
                           **presets['electronic']),
            'H2O': StatMech(name='H2O', potentialenergy=3.*dim_factor,
                            **presets['electronic']),
        }
        self.rxn_delta_H = Reaction.from_string(
                reaction_str='H2 + 0.5O2 = H2O',
                species=species,
                descriptor='delta_H',
                slope=self.m,
                intercept=self.c,
                bep=BEP)
        self.bep_delta_H = self.rxn_delta_H.bep

        rxn_rev_delta_H = Reaction.from_string(
                reaction_str='H2 + 0.5O2 = H2O',
                species=species,
                descriptor='rev_delta_H',
                slope=self.m,
                intercept=self.c,
                bep=BEP)
        self.bep_rev_delta_H = rxn_rev_delta_H.bep

        rxn_reactants_H = Reaction.from_string(
                reaction_str='H2 + 0.5O2 = H2O',
                species=species,
                descriptor='reactants_H',
                slope=self.m,
                intercept=self.c,
                bep=BEP)
        self.bep_reactants_H = rxn_reactants_H.bep

        rxn_products_H = Reaction.from_string(
                reaction_str='H2 + 0.5O2 = H2O',
                species=species,
                descriptor='products_H',
                slope=self.m,
                intercept=self.c,
                bep=BEP)
        self.bep_products_H = rxn_products_H.bep

        self.rxn_delta_E = Reaction.from_string(
                reaction_str='H2 + 0.5O2 = H2O',
                species=species,
                descriptor='delta_E',
                slope=self.m,
                intercept=self.c,
                bep=BEP)
        self.bep_delta_E = self.rxn_delta_E.bep

        rxn_rev_delta_E = Reaction.from_string(
                reaction_str='H2 + 0.5O2 = H2O',
                species=species,
                descriptor='rev_delta_E',
                slope=self.m,
                intercept=self.c,
                bep=BEP)
        self.bep_rev_delta_E = rxn_rev_delta_E.bep

        rxn_reactants_E = Reaction.from_string(
                reaction_str='H2 + 0.5O2 = H2O',
                species=species,
                descriptor='reactants_E',
                slope=self.m,
                intercept=self.c,
                bep=BEP)
        self.bep_reactants_E = rxn_reactants_E.bep

        rxn_products_E = Reaction.from_string(
                reaction_str='H2 + 0.5O2 = H2O',
                species=species,
                descriptor='products_E',
                slope=self.m,
                intercept=self.c,
                bep=BEP)
        self.bep_products_E = rxn_products_E.bep

    def test_get_EoRT(self):
        delta_H = self.rxn_delta_H.get_delta_HoRT(T=self.T)
        exp_EoRT_delta = self.m*delta_H + self.c/c.R('kcal/mol/K')/self.T
        exp_EoRT_delta_rev = (self.m-1.)*delta_H \
                             + self.c/c.R('kcal/mol/K')/self.T

        self.assertAlmostEqual(self.bep_delta_H.get_EoRT_act(T=self.T,
                                                           rev=False),
                               exp_EoRT_delta)
        self.assertAlmostEqual(self.bep_delta_H.get_EoRT_act(T=self.T,
                                                           rev=True),
                               exp_EoRT_delta_rev)

        rev_delta_H = self.rxn_delta_H.get_delta_HoRT(T=self.T,
                                                    rev=True)
        exp_EoRT_delta = (self.m-1.)*rev_delta_H \
                         + self.c/c.R('kcal/mol/K')/self.T
        exp_EoRT_delta_rev = self.m*rev_delta_H \
                             + self.c/c.R('kcal/mol/K')/self.T
        self.assertAlmostEqual(self.bep_rev_delta_H.get_EoRT_act(T=self.T,
                                                               rev=False),
                               exp_EoRT_delta)
        self.assertAlmostEqual(self.bep_rev_delta_H.get_EoRT_act(T=self.T,
                                                               rev=True),
                               exp_EoRT_delta_rev)

        reactants_H = self.rxn_delta_H.get_HoRT_state(state='reactants',
                                                      T=self.T)
        exp_EoRT_delta = self.m*reactants_H + self.c/c.R('kcal/mol/K')/self.T
        exp_EoRT_delta_rev = (self.m-1.)*reactants_H \
                             + self.c/c.R('kcal/mol/K')/self.T

        self.assertAlmostEqual(self.bep_reactants_H.get_EoRT_act(T=self.T,
                                                               rev=False),
                               exp_EoRT_delta)
        self.assertAlmostEqual(self.bep_reactants_H.get_EoRT_act(T=self.T,
                                                               rev=True),
                               exp_EoRT_delta_rev)

        products_H = self.rxn_delta_H.get_HoRT_state(state='products',
                                                   T=self.T)
        exp_EoRT_delta = self.m*products_H + self.c/c.R('kcal/mol/K')/self.T
        exp_EoRT_delta_rev = (self.m-1.)*products_H \
                             + self.c/c.R('kcal/mol/K')/self.T

        self.assertAlmostEqual(self.bep_products_H.get_EoRT_act(T=self.T,
                                                              rev=False),
                               exp_EoRT_delta)
        self.assertAlmostEqual(self.bep_products_H.get_EoRT_act(T=self.T,
                                                              rev=True),
                               exp_EoRT_delta_rev)

        delta_E = self.rxn_delta_E.get_delta_EoRT(T=self.T)
        exp_EoRT_delta = self.m*delta_E + self.c/c.R('kcal/mol/K')/self.T
        exp_EoRT_delta_rev = (self.m-1.)*delta_E \
                             + self.c/c.R('kcal/mol/K')/self.T

        self.assertAlmostEqual(self.bep_delta_E.get_EoRT_act(T=self.T,
                                                           rev=False),
                               exp_EoRT_delta)
        self.assertAlmostEqual(self.bep_delta_E.get_EoRT_act(T=self.T,
                                                           rev=True),
                               exp_EoRT_delta_rev)

        rev_delta_E = self.rxn_delta_E.get_delta_EoRT(T=self.T,
                                                    rev=True)
        exp_EoRT_delta = (self.m-1.)*rev_delta_E \
                         + self.c/c.R('kcal/mol/K')/self.T
        exp_EoRT_delta_rev = self.m*rev_delta_E \
                             + self.c/c.R('kcal/mol/K')/self.T

        self.assertAlmostEqual(self.bep_rev_delta_E.get_EoRT_act(T=self.T,
                                                               rev=False),
                               exp_EoRT_delta)
        self.assertAlmostEqual(self.bep_rev_delta_E.get_EoRT_act(T=self.T,
                                                               rev=True),
                               exp_EoRT_delta_rev)

        reactants_E = self.rxn_delta_E.get_EoRT_state(state='reactants',
                                                    T=self.T)
        exp_EoRT_delta = self.m*reactants_E + self.c/c.R('kcal/mol/K')/self.T
        exp_EoRT_delta_rev = (self.m-1.)*reactants_E \
                             + self.c/c.R('kcal/mol/K')/self.T

        self.assertAlmostEqual(self.bep_reactants_E.get_EoRT_act(T=self.T,
                                                               rev=False),
                               exp_EoRT_delta)
        self.assertAlmostEqual(self.bep_reactants_E.get_EoRT_act(T=self.T,
                                                               rev=True),
                               exp_EoRT_delta_rev)

        products_E = self.rxn_delta_E.get_EoRT_state(state='products',
                                                   T=self.T)
        exp_EoRT_delta = self.m*products_E + self.c/c.R('kcal/mol/K')/self.T
        exp_EoRT_delta_rev = (self.m-1.)*products_E \
                             + self.c/c.R('kcal/mol/K')/self.T

        self.assertAlmostEqual(self.bep_products_E.get_EoRT_act(T=self.T,
                                                              rev=False),
                               exp_EoRT_delta)
        self.assertAlmostEqual(self.bep_products_E.get_EoRT_act(T=self.T,
                                                              rev=True),
                               exp_EoRT_delta_rev)


if __name__ == '__main__':
    unittest.main()
