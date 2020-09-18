# Installation instructions

> git clone git@github.com:gummiks/crosscorr.git

> python setup.py install



# More detailed instllation instructions
Normally, this wouldn't be needed, as the setup.py should take care of the installation, but listing these steps just in case.

## Fortran installation instructions

You will need to compile two fortran files.

To install run the following commands:

### Linux

> f2py -c -m CCF_1d CCF_1d.f

> f2py -c -m CCF_3d CCF_3d.f

### Mac
On mac you might need to try sudo (verified that this works on my mac).

> sudo f2py -c -m CCF_1d CCF_1d.f

> sudo f2py -c -m CCF_3d CCF_3d.f
