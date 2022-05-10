# -*- coding: utf-8 -*-
from mofdscribe.chemistry.partialchargehistogram import PartialChargeHistogram

from ..helpers import is_jsonable


def test_partialchargehistogram(hkust_structure, irmof_structure):
    pch = PartialChargeHistogram()
    assert len(pch.feature_labels()) == 16

    for structure in [hkust_structure, irmof_structure]:
        features = pch.featurize(structure)
        assert len(features) == 16
    assert is_jsonable(dict(zip(pch.feature_labels(), features)))
    assert features.ndim == 1
