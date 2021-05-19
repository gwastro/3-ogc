#!/usr/bin/env python

import logging                                                                  
import shutil                                                                   
import argparse                                                                 
import numpy                                                                    
import pycbc                                                                    
from pycbc.inference import io                                                  
from scipy.special import logsumexp 

"""Reweights samples from a prior uniform in q > 1 to a prior uniform in
m1, m2.
"""

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', required=True)
parser.add_argument('--output-file', required=True)
parser.add_argument('--input-is-posterior', action='store_true')

opts = parser.parse_args()

pycbc.init_logging(True)
logging.info("Copying input to output")
shutil.copy(opts.input_file, opts.output_file)

logging.info('Reweighting samples')
fp = io.loadfile(opts.output_file, 'a')
input_is_posterior = opts.input_is_posterior 
if input_is_posterior:
    fp.attrs['filetype'] = 'posterior_file'
    fp.close()
    fp = io.loadfile(opts.output_file, 'a')
    samples = fp.read_samples(['srcmtotal', 'q'])
else:
    samples = fp.read_samples(['srcmtotal', 'q', 'logwt'],
                              raw_samples=True)
logjacobian = samples['2*log(1+q) - log(srcmtotal)']
if input_is_posterior:
    logwt = -numpy.log(samples.size) 
else:
    logwt = samples['logwt']
logwt -= logjacobian

# renormalize and save
logz = fp.log_evidence[0]
lognorm = logsumexp(logwt - logz)
logging.info("lognorm is: %f", lognorm)
logwt -= lognorm
if input_is_posterior:
    fp['samples/logwt'] = logwt
    fp.attrs['filetype'] = 'dynesty_file'
else:
    fp['samples/logwt'][:] = logwt
fp.close()
