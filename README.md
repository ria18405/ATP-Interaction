## AIM: Prediction of ATP interacting residues

#### HOW TO RUN

	`python3 script.py`

#### STEPS

* **TRAINING**

	* Make patterns of length n=7 for each protien sequence.

	* Apply Binary Profiling on each pattern i.e we'll have matrix of size (21 * n) for one pattern

	* We know that a small aplhabet indicates an ATP interacting residue, so mark it as -1 (non interacting) or +1 (interacting) 

* **TESTING**

	* Predict using `predict(X)` function by passing the residue protien as an argument.

#### OUTPUT

* Output.txt with `ID,Label` columns, where label is value 		
	* +1 = ATP INTERACTING RESIDUE
	* -1 = NON ATP INTERACTING RESIDUE

[Output file](https://github.com/ria18405/ATP-Interaction/output.txt)


