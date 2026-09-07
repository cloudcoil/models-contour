# cloudcoil-models-contour

Versioned contour models for cloudcoil.

[![PyPI](https://img.shields.io/pypi/v/cloudcoil.models.contour.svg)](https://pypi.python.org/pypi/cloudcoil.models.contour)
[![Downloads](https://static.pepy.tech/badge/cloudcoil.models.contour)](https://pepy.tech/project/cloudcoil.models.contour)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/license/apache-2-0/)
[![CI](https://github.com/cloudcoil/models-contour/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudcoil/models-contour/actions/workflows/ci.yml)

Models generated from the upstream tagged CRD schemas pinned in `pyproject.toml`.

```python
from cloudcoil.models.contour import get_model

HTTPProxy = get_model("HTTPProxy", api_version="projectcontour.io/v1")
```
