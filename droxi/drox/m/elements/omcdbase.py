#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# droxi
# Copyright (c) 2014, Andrew Robbins, All rights reserved.
# 
# This library ("it") is free software; it is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; you can redistribute it and/or modify it under the terms of the
# GNU Lesser General Public License ("LGPLv3") <https://www.gnu.org/licenses/lgpl.html>.
from __future__ import absolute_import

from ...omcdbase.arith1 import _mapping as arith1
from ...omcdbase.integer1 import _mapping as integer1

from ...omcdbase.quant1._mapping import _namespace_mapping as quant1
from ...omcdbase.complex1._mapping import _namespace_mapping as complex1
from ...omcdbase.rounding1._mapping import _namespace_mapping as rounding1
from ...omcdbase.relation1._mapping import _namespace_mapping as relation1
from ...omcdbase.minmax1._mapping import _namespace_mapping as minmax1
from ...omcdbase.logic1._mapping import _namespace_mapping as logic1
from ...omcdbase.set1._mapping import _namespace_mapping as set1

from ..models import CSym
import argparse
_namespace_mapping = argparse.Namespace()

# --- custom
# interval
# lambda


# # # CUSTOM
# # @CSym.called("int")
# # class C(calculus1.int): pass
# # 
# # @CSym.called("int")
# # class C(calculus1.defint): pass
# 
# @CSym.called("diff")
# class CDiff(calculus1.diff): pass
# 
# # @CSym.called("partialdiff")
# # class C(calculus1.partialdiff): pass

# @CSym.called("inverse")
# class CInverse(fns1.inverse): pass
# 
# @CSym.called("compose")
# class CCompose(fns1.left_compose): pass
# 
# @CSym.called("ident")
# class CIdentity(fns1.identity): pass
# 
# @CSym.called("domain")
# class CDomain(fns1.domain): pass
# 
# @CSym.called("codomain")
# class CCodomain(fns1.range): pass
# 
# @CSym.called("image")
# class CCodomain(fns1.image): pass
# 
# @CSym.called("piecewise")
# class CPiecewise(piece1.piecewise): pass
# 
# @CSym.called("piece")
# class CPiece(piece1.piece): pass
# 
# @CSym.called("otherwise")
# class COtherwise(piece1.otherwise): pass
 
# @CSym.called("divergence")
# class CDivergence(veccalc1.divergence): pass
# _namespace_mapping.__dict__[""] = 
# 
# @CSym.called("grad")
# class CGrad(veccalc1.grad): pass
# _namespace_mapping.__dict__[""] = 
# 
# @CSym.called("curl")
# class CCurl(veccalc1.curl): pass
# _namespace_mapping.__dict__[""] = 
# 
# @CSym.called("laplacian")
# class Claplacian(veccalc1.Laplacian): pass
# _namespace_mapping.__dict__[""] = 

@CSym.called("quotient")
class CQuo(integer1.quotient): pass
_namespace_mapping.__dict__["quotient"] = CQuo

@CSym.called("factorial")
class CFactorial(integer1.factorial): pass
_namespace_mapping.__dict__["factorial"] = CFactorial

@CSym.called("divide")
class CDivide(arith1.divide): pass
_namespace_mapping.__dict__["divide"] = CDivide

@CSym.called("max")
class CMax(minmax1.max): pass
_namespace_mapping.__dict__["max"] = CMax

@CSym.called("min")
class CMin(minmax1.min): pass
_namespace_mapping.__dict__["min"] = CMin

@CSym.called("minus")
class CMinus(arith1.minus): pass
_namespace_mapping.__dict__["minus"] = CMinus

@CSym.called("plus")
class CPlus(arith1.plus): pass
_namespace_mapping.__dict__["plus"] = CPlus

@CSym.called("power")
class CPower(arith1.power): pass
_namespace_mapping.__dict__["power"] = CPower

@CSym.called("rem")
class CRem(integer1.remainder): pass
_namespace_mapping.__dict__["rem"] = CRem

@CSym.called("times")
class CTimes(arith1.times): pass
_namespace_mapping.__dict__["times"] = CTimes

@CSym.called("root")
class CRoot(arith1.root): pass
_namespace_mapping.__dict__["root"] = CRoot

@CSym.called("gcd")
class CGcd(arith1.gcd): pass
_namespace_mapping.__dict__["gcd"] = CGcd

@CSym.called("and")
class CAnd(getattr(logic1, 'and')): pass
_namespace_mapping.__dict__["and"] = CAnd

@CSym.called("or")
class COr(getattr(logic1, 'or')): pass
_namespace_mapping.__dict__["or"] = COr

@CSym.called("xor")
class CXor(getattr(logic1, 'xor')): pass
_namespace_mapping.__dict__["xor"] = CXor

@CSym.called("not")
class CNot(getattr(logic1, 'not')): pass
_namespace_mapping.__dict__["not"] = CNot

@CSym.called("implies")
class CImplies(logic1.implies): pass
_namespace_mapping.__dict__["implies"] = CImplies

@CSym.called("forall")
class CForAll(quant1.forall): pass
_namespace_mapping.__dict__["forall"] = CForAll

@CSym.called("exists")
class CExists(quant1.exists): pass
_namespace_mapping.__dict__["CExists"] = CExists

@CSym.called("abs")
class CAbs(arith1.abs): pass
_namespace_mapping.__dict__["abs"] = CAbs

@CSym.called("conjugate")
class CConjugate(complex1.conjugate): pass
_namespace_mapping.__dict__["conjugate"] = CConjugate

@CSym.called("arg")
class CArgument(complex1.argument): pass
_namespace_mapping.__dict__["arg"] = CArgument

@CSym.called("real")
class CReal(complex1.real): pass
_namespace_mapping.__dict__["real"] = CReal

@CSym.called("imaginary")
class CImaginary(complex1.imaginary): pass
_namespace_mapping.__dict__["imaginary"] = CImaginary

@CSym.called("lcm")
class CLcm(arith1.lcm): pass
_namespace_mapping.__dict__["lcm"] = CLcm

@CSym.called("floor")
class CFloor(rounding1.floor): pass
_namespace_mapping.__dict__["floor"] = CFloor

@CSym.called("ceiling")
class CCeiling(rounding1.ceiling): pass
_namespace_mapping.__dict__["ceiling"] = CCeiling

@CSym.called("eq")
class CEq(relation1.eq): pass
_namespace_mapping.__dict__["eq"] = CEq

@CSym.called("neq")
class CNeq(relation1.neq): pass
_namespace_mapping.__dict__["neq"] = CNeq

@CSym.called("gt")
class CGt(relation1.gt): pass
_namespace_mapping.__dict__["gt"] = CGt

@CSym.called("lt")
class CLt(relation1.lt): pass
_namespace_mapping.__dict__["lt"] = CLt

@CSym.called("geq")
class CGeq(relation1.geq): pass
_namespace_mapping.__dict__["geq"] = CGeq

@CSym.called("leq")
class CLeq(relation1.leq): pass
_namespace_mapping.__dict__["leq"] = CLeq

@CSym.called("equivalent")
class CEquivalent(logic1.equivalent): pass
_namespace_mapping.__dict__["equivalent"] = CEquivalent

@CSym.called("approx")
class CApprox(relation1.approx): pass
_namespace_mapping.__dict__["approx"] = CApprox

@CSym.called("factorof")
class CFactorOf(integer1.factorof): pass
_namespace_mapping.__dict__["factorof"] = CFactorOf

@CSym.called("union")
class CUnion(set1.union): pass
_namespace_mapping.__dict__["union"] = CUnion

@CSym.called("intersect")
class CIntersect(set1.intersect): pass
_namespace_mapping.__dict__["intersect"] = CIntersect

@CSym.called("in")
class CIn(getattr(set1, 'in')): pass
_namespace_mapping.__dict__["in"] = CIn

@CSym.called("notin")
class CNotIn(set1.notin): pass
_namespace_mapping.__dict__["notin"] = CNotIn

@CSym.called("subset")
class CSubSet(set1.subset): pass
_namespace_mapping.__dict__["subset"] = CSubSet

@CSym.called("prsubset")
class CPrSubSet(set1.prsubset): pass
_namespace_mapping.__dict__["prsubset"] = CPrSubSet

@CSym.called("notsubset")
class CNotSubSet(set1.notsubset): pass
_namespace_mapping.__dict__["notsubset"] = CNotSubSet

@CSym.called("notprsubset")
class CNotPrSubSet(set1.notprsubset): pass
_namespace_mapping.__dict__["notprsubset"] = CNotPrSubSet

@CSym.called("setdiff")
class CSetDiff(set1.setdiff): pass
_namespace_mapping.__dict__["setdiff"] = CSetDiff

@CSym.called("card")
class CCard(set1.size): pass
_namespace_mapping.__dict__["card"] = CCard

@CSym.called("cartesianproduct")
class CCartesianProduct(set1.cartesian_product): pass
_namespace_mapping.__dict__["cartesianproduct"] = CCartesianProduct

@CSym.called("sum")
class CSum(arith1.sum): pass
_namespace_mapping.__dict__["sum"] = CSum

@CSym.called("product")
class CProduct(arith1.product): pass
_namespace_mapping.__dict__["product"] = CProduct

# @CSym.called("")
# class C(.): pass
# _namespace_mapping.__dict__[""] = 
# 
# @CSym.called("")
# class C(.): pass
# _namespace_mapping.__dict__[""] = 
