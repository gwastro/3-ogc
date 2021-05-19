# 3-OGC: Open Gravitational-wave Catalog of binary mergers from analysis of public Advanced LIGO and Virgo data
** Alexander H. Nitz <sup>1,2</sup>, Collin D. Capano<sup>1,2</sup>, Sumit Kumar<sup>1,2</sup>, Yi-Fan Wang<sup>1,2</sup>, Shilpa Kastha<sup>1,2</sup>, Marlin Schaefer<sup>1,2</sup>, Rahul Dhurkunde<sup>1,2</sup>, and Miriam Cabero<sup>3</sup> **

<sub>1. [Albert-Einstein-Institut, Max-Planck-Institut for Gravitationsphysik, D-30167 Hannover, Germany](http://www.aei.mpg.de/obs-rel-cos)</sub>  
<sub>2. Leibniz Universitat Hannover, D-30167 Hannover, Germany</sub>  
<sub>3. Department of Physics and Astronomy, The University of British Columbia, Vancouver, BC V6T 1Z4, Canada </sub>



## [Parameter Estimates for top 55 BBH candidates] ##
Posteriors sample for the 55 most significant BBH candidates are located in the ['posterior_samples'](https://github.com/gwastro/3-ogc/tree/master/posterior_samples) folder. A summary of the parameter estimation results may be found here:
 
 * BBH summary page:
 The posterior samples are in the `samples` group in the posterior data hdf files. These may be read in a python environment using an installation of h5py. For example,
 
 ```
>>> import h5py
>>> a = h5py.File('./GW190925_232845-PYCBC-POSTERIOR-XPHM.hdf', 'r')
>>> a.keys()
<KeysViewHDF5 ['samples']>
>>> a['samples']
<HDF5 group "/samples" (21 members)>
>>> a['samples'].keys()
<KeysViewHDF5 ['chi_eff', 'chi_p', 'coa_phase', 'dec', 'delta_tc', 'distance', 'inclination', 'loglikelihood', 'logwt', 'q', 'ra', 'redshift', 'spin1_a', 'spin1_azimuthal', 'spin1_polar', 'spin2_a', 'spin2_azimuthal', 'spin2_polar', 'srcmass1', 'srcmass2', 'srcmchirp']>
>>> a['samples']['chi_eff']   
<HDF5 dataset "chi_eff": shape (56604,), type "<f8">
```

Provided parameters are:
 * `srcmass1`: The source-frame mass of the larger object, in solar masses.
 * `srcmass2`: The source-frame mass of the smaller object, in solar masses.
 * `srcmchirp`: The source-frame chirp mass, in solar masses.
 * `q`: The mass ratio, larger object mass to smaller object mass.
 * `chi_eff`: The effective spin of the binary.
 * `chi_p`: The precessing-spin parameter of the binary.
 * `spin1_a`: The dimensionless spin-magnitude of the larger object.
 * `spin2_a`: The dimensionless spin-magnitude of the smaller object.
 * `spin1_azimuthal`: The azimuthal angle of the spin of the larger object.
 * `spin2_azimuthal`: The azimuthal angle of the spin of the smaller object.
 * `spin1_polar`: The polar angle of the spin of the spin of the larger object.
 * `spin2_polar`: The polar angle of the spin of the spin of the smaller object.
 * `tc`: The geocentric GPS time of the signal merger.
 * `ra`: The right ascension of the signal (in radians).
 * `dec`: The declination of the signal (in radians).
 * `distance`: The lumionsity distance to the signal (in Mpc).
 * `redshift`: The cosmological redshift of the signal.
 * `comoving_volume`: The comoving volume at the redshift of the signal.
 * `inclination`: The inclination of the binary's orbital angular momentum with
   respect to the line of sight, in radians. An inclination of 0 (pi)
   corresponds to a face-on (face-away) orientation.
 * `coa_phase`: The coalescence phase of the binary system.
 * `loglikelihood`: The natural log of the likelihood of each sample.
 * `logprior`: The natural log of the prior of each sample.
 * `logjacobian`: The natural log of the Jacobian between the parameter space and the sampling parameter-space that was used.
