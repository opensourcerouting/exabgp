## OpenSourceRouting.org fork of fixed ExaBGP for FRRouting topotests

This is a fork of ExaBGP 4.2.11 with a few fixes for compatibility with the
FRRouting topology tests.

Please refer to the [FRRouting Developer's Guide](http://docs.frrouting.org/projects/dev-guide/en/latest/topotests.html) for information about FRRouting topology tests.

### Installation
This modified release of ExaBGP 4.2.11 can be directly installed on most
GNU/Linux distributions from this repository with the
[Package Installer for Python 3](https://github.com/pypa/pip) by running the
following commands with superuser privileges:
```
useradd -d /var/run/exabgp/ -s /bin/false exabgp
python3 -m pip install git+https://github.com/opensourcerouting/exabgp@4.2.11-frr
```

### Modifications
This version of ExaBGP differs from the original ExaBGP 4.2.11 by the
application of fixes for these issues/pull requests:
* update/traffic: fix IPv6 translation [PR #1003](https://github.com/Exa-Networks/exabgp/pull/1003)
* BGP flowspec IPv6 redirect [Issue #1004](https://github.com/Exa-Networks/exabgp/issues/1004)
