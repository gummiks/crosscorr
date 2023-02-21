# crosscorr
Easily calculate Cross Correlation Functions (CCFs) from different high resolution spectra. Includes masks from HARPS, ESPRESSO, and HPF. Uses Fortran for speed. The fortran code used here is originally derived from <a href='https://github.com/rabrahm/ceres'>ceres</a>. The notebooks/ directory shows an example on how to calculate CCFs with HPF spectra.

# Installation instructions
To install, run the following commands:
```
git clone git@github.com:gummiks/crosscorr.git
cd crosscorr
python setup.py install
```
This should build the fortran code as well.

# More detailed installation instructions
Normally the setup.py should fully take care of the installation (including the fotran compilation), but listing instructions to build the fotran code in python just in case.

## Fortran installation instructions

In case the fortran code does not build, run the following commands:

### Linux

```
cd crosscorr/
f2py -c -m CCF_1d CCF_1d.f
f2py -c -m CCF_3d CCF_3d.f
f2py -c -m CCF_pix CCF_pix.f
```

## Mac
On mac you might need to try sudo (verified that this works on my mac).

```
cd crosscorr/
sudo f2py -c -m CCF_1d CCF_1d.f
sudo f2py -c -m CCF_3d CCF_3d.f
sudo f2py -c -m CCF_pix CCF_pix.f
```
