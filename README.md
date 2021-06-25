# 3-OGC: Catalog of gravitational-waves from compact-binary mergers
** Alexander H. Nitz <sup>1,2</sup>, Collin D. Capano<sup>1,2</sup>, Sumit Kumar<sup>1,2</sup>, Yi-Fan Wang<sup>1,2</sup>, Shilpa Kastha<sup>1,2</sup>, Marlin Schaefer<sup>1,2</sup>, Rahul Dhurkunde<sup>1,2</sup>, and Miriam Cabero<sup>3</sup> **

<sub>1. [Albert-Einstein-Institut, Max-Planck-Institut for Gravitationsphysik, D-30167 Hannover, Germany](http://www.aei.mpg.de/obs-rel-cos)</sub>  
<sub>2. Leibniz Universitat Hannover, D-30167 Hannover, Germany</sub>  
<sub>3. Department of Physics and Astronomy, The University of British Columbia, Vancouver, BC V6T 1Z4, Canada </sub>

![](https://github.com/gwastro/3-ogc/blob/master/3ogc.png)

## Introduction

We present the third Open Gravitational-wave Catalog (3-OGC) of compact-binary coalescences,
based on the analysis of the public LIGO and Virgo data from 2015 through 2019 (O1, O2, O3a). Our
updated catalog includes a population of 57 observations, including four binary black hole mergers that
had not previously been reported. This consists of 55 binary black hole mergers and the two binary
neutron star mergers GW170817 and GW190425. We find no additional significant binary neutron
star or neutron star–black hole merger events. The most confident new detection is the binary black
hole merger GW190925 232845 which was observed by the LIGO Hanford and Virgo observatories
with Pastro > 0.99; its primary and secondary component masses are 20.2+3.9−2.5Msun and 15.6+2.1−2.6Msun,
respectively. We estimate the parameters of all binary black hole events using an up-to-date waveform
model that includes both sub-dominant harmonics and precession effects. To enable deep follow-up as
our understanding of the underlying populations evolves, we make available our comprehensive catalog
of events, including the sub-threshold population of candidates, and the posterior samples of our source
parameter estimates.

## [Parameter Estimates for the 55 BBH and 2 BNS detections](https://pycbc.org/3-ogc/posteriors) ##
Posteriors sample for the 55 most significant BBH and 2 BNS candidates are located in the ['posterior_samples'](https://github.com/gwastro/3-ogc/tree/master/posterior) folder. A summary of the parameter estimation results may be found here:
 
 * [Summary Page [plots!]](https://pycbc.org/3-ogc/posteriors)

 The posterior samples are in the `samples` group in the posterior data hdf files. These may be read in a python environment using an installation of h5py. For example,
 
 ```
>>> import h5py
>>> fp = h5py.File('GW150914_095045-PYCBC-POSTERIOR-XPHM.hdf','r')
>>> fp.keys()
[u'samples']
>>> fp['samples'].keys()
[u'chi_eff', u'chi_p', u'coa_phase', u'dec', u'delta_tc', u'distance', u'inclination', u'loglikelihood', u'logwt', u'q', u'ra', u'redshift', u'spin1_a', u'spin1_azimuthal', u'spin1_polar', u'spin2_a', u'spin2_azimuthal', u'spin2_polar', u'srcmass1', u'srcmass2', u'srcmchirp', u'srcmtot']
>>> fp['samples/srcmass1'][:]
array([36.1643739 , 32.75384643, 35.34795668, ..., 32.38363066,
       35.48601188, 37.46221438])
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

For GW190521_030229, uniform prior in source frame total mass and mass ratio `q` is used. A [script](https://github.com/gwastro/3-ogc/blob/master/scripts/reweight_samples.py) is used to reweight the samples to a prior uniform in component masses. For this particular event, we provide posterior files and config files for another set of run where localization (ra,dec,distance) is fixed in accordance with possible coincidence with accretion flare by the Zwicky Transient Facility (ZTF). See this [paper](https://arxiv.org/abs/2010.12558) for more detail.
## Catalog of Merger Candidates (including sub-threshold candidates) ##

### Analysis Details ###
Details of the analysis are available in this [preprint paper](https://arxiv.org/abs/2105.09151) and the configuration files needed to create the analysis workflows are provided in the [search_configs](https://github.com/gwastro/3-ogc/tree/master/search_configuration) directory.

The files 3-OGC_top.txt and 3-OGC_sub17.txt are text format version of the tables in the paper. For more complete listings of candidates see the following.

### Accessing the Catalog: 3-OGC_low.hdf, 3-OGC_high.hdf ###

The complete catalog with subthreshold candidates included is split between two files (due to github files size limits). The 'low' file includes 
candidates triggered with a template that has m1 + m2 < 6, the remainder are in the file postfixed 'high'. The formate is otherwise the same.

```python
import h5py

catalog_high = h5py.File('./3-OGC_low.hdf', 'r')

# Selecting parts of the catalog
region = candidates['mass1'][:] + candidates['mass2'][:] < 4
lowmass_snr = all_candidates['H1_snr'][:][region]
```


##### File format #####
Both datasets are structured arrays which have the following named columns. Some of these columns give information specific to either the 
LIGO Hanford, LIGO Livingston or Virgo detectors. Where this is the case, the name of the column is prefixed with either a `H1`, `L1`, or 'V1'.

Note: For template parameters and statistics, we report the values associated with the candidate at a given time with the lowest false alarm rate. The search
can report many candidates for a common single source due to the overlap between its many template waveforms, hence the parameters don't indicate the only template which identified a particular signal.

| Key           | Description                                                                                                                         |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| name          | The designation of the candidate event. This is of the form 150812_122304 ('GW is not prefixed even to confident mergers').                                                     |
| IFAR           | The rate of false alarms with a ranking statistic as large or larger than this event. The unit is yr^-1.                                                                                                           |
| stat          | The value of the ranking statistic for this candidate event.                                                                                       |
| mass1         | The component mass of one compact object in the template waveform which found this candidate. Units in detector frame solar masses. |
| mass2         | The component mass of the template waveform which found this candidate. Units in detector frame solar masses.                       |
| spin1z        | The dimensionless spin of one of the compact objects for the template waveform which found this candidate.                                                                                                                                  |
| spin2z        | The dimensionless spin of one of the compact objects for the template waveform which found this candidate.                                                                                                                                    |
| {H1/L1/V1}_end_time   | The time in GPS seconds when a fiducial point in the signal passes throught the detector. Typically this is near the time of merger.                                                                                                                              |                                                                                                                           |
| {H1/L1/V1}_snr        | The amplitude of the complex matched filter signal-to-noise observed.                                                                                                                                    |                                                      |
| {H1/L1/V1}_chisq |  Value of the signal consistency test defined in this [paper](https://arxiv.org/abs/gr-qc/0405045). This is not calculated for all candidate events. In this case a value of 0 is substituted.                                                                                                                                  |
| {H1/L1/V1}_sg_chisq      |  Value of the signal consistency test defined in this [paper](https://arxiv.org/abs/1709.08974). This is not calculated for all candidate events. In this case a value of 1 is substituted.                                                                                                                     |
| pastro |     The probability that this BBH candidate is of astrophysical origin.                                        |
                     

## License and Citation

![Creative Commons License](https://i.creativecommons.org/l/by-sa/3.0/us/88x31.png "Creative Commons License")

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 United States License](http://creativecommons.org/licenses/by-sa/3.0/us/).

We encourage use of these data in derivative works. If you use the material provided here, please cite the paper using the reference:

```
@article{Nitz:2021uxj,
    author = {Nitz, Alexander H. and Capano, Collin D. and Kumar, Sumit and Wang, Yi-Fan and Kastha, Shilpa and Sch\"afer, Marlin and Dhurkunde, Rahul and Cabero, Miriam},
    title = "{3-OGC: Catalog of gravitational waves from compact-binary mergers}",
    eprint = "2105.09151",
    archivePrefix = "arXiv",
    primaryClass = "astro-ph.HE",
    month = "5",
    year = "2021"
}
```
