Motif Compete Simulation
Grant Kinsler
Written: 15/06/2015
Last Update: 01/03/2016

motifcompetesim_master.py is the master file of the simulation. Options used to indicate the parameters used in the run.
Use --help option for more information on parameter options.

Example command line way to run a simulation (consisting of 2 trials of 100 rounds each, with various other parameters. Elongation data is suppressed in default): python motifcompetesim_master.py --trials=2 --maxStrands=10 --maxStrandLength=7 --numCells=10 --numRounds=100 --elong=0.05 --motiflist=10000,01111 --biaslist=0.9,0.1 (--elongdata=False)


List of other necessary files:
motifcompetesim_trial.py; runs a trial of the simulation
motifcompetesim_motifoutput.py; runs simulations and controls motif data csv output
motifcompetesim_allstrandoutput.py; controls all data csv output
motifcompetesim_elongdataoutput.py; controls output of elongation pattern
motifcompetesim_fulltrialoutput.py; controls full trial 1 data dsv output
motifcompetesim_cell.py; defines Cell class
motifcompetesim_population.py; defines Population class
