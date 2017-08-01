# lecroy-reader
Small tool for reading binary .trc files from LeCroy oscilloscopes

## Scope

Extract data from .trc binary scope trace files from LeCroy oscilloscopes, with emphasis on segmented acquisition mode traces.

This code has only been tested on a LeCroy WaveRunner 6050A.

## Installation

    python setup.py develop

## Usage

    import lecroyreader as lcr
    
    metadata, trigtimes, data = lcr.read('/path/to/trace.trc')