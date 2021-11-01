# sydsap
[![Licence](http://img.shields.io/badge/license-GPLv3-blue.svg?style=flat)](http://www.gnu.org/licenses/gpl-3.0.html)

## Contributors
Tim White

## Installation

To install from source: clone this git repo, enter the directory, and run

`python setup.py install`

## Rationale

Occassionally, light curves provided by the TESS Science Processing Operations Center (SPOC) contain significant scatter, particularly during periods of less stable spacecraft pointing. Often the light curve quality can be significantly improved by picking a different, generally larger, aperture. The purpose of this code is to generate improved light curves when this situation occurs, primarily using methods from the `lightkurve` package. It first generates a new aperture mask, then calculates a new light curve from simple aperture photometry over this mask. Finally, it removes some instrumental noise using linear regression.

## Basic usage

First change the class of the target pixel file to the `sydsap_tpf` class, then run `tpf.sydsap()`:

```python
from sydsap.sydsap import sydsap_tpf

tpf__class__ = sydsap_tpf

lc = tpf.sydsap()
```

## License

We invite anyone interested to use and modify this code under a GPL v3 license. 