from types import ModuleType

import cloudcoil.models.contour as contour


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), contour.__dict__.values()))
    assert modules, "No modules found in contour"
