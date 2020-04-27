## AIM: Prediction of ATP interacting residues

#### HOW TO RUN

	`python3 script.py`

#### STEPS

* **TRAINING**

	* Choose a value of n, i.e length of patterns. eg, n=7/n=9,n=17 etc.

	* Add ((n-1)/2)'XXX..' in the starting and end of the protien sequence such that we have (XX..protien_seq..XX).

	* Make patterns or cut windows of length n for each protien sequence.

	* Apply Binary Profiling on each pattern i.e we'll have matrix of size (21 * n) for one pattern
	Binary profile essentially means making a 2-Dimentional array, which stores 1 for each match with the list of Amino Acids and 'X'. Else, stores 0 for non-match.

	* We know that a small aplhabet indicates an ATP interacting residue, so mark it as -1 (non interacting) or +1 (interacting) 

	* Used OneVsRestClassifier in SVM.

	* Used (.fit(X,Y)) to train the dataset, where X is the binary profiled matrix and Y is the list containing answers i.e if each residue is ATP interacting or not.

* **TESTING**

	* Predict using `predict(X)` function by passing the residue protien as an argument.

	* For Testing purposes, we join all amino Acids into a protien and then perform pattern formation (as explained above in training dataset) followed by binary profiling. 

#### OUTPUT

* Output.txt with `ID,Label` columns, where label is value 		
	* +1 = ATP INTERACTING RESIDUE
	* -1 = NON ATP INTERACTING RESIDUE

* Kaggle score = 0.61957

[Output file](https://github.com/ria18405/ATP-Interaction/blob/master/output.txt)

#### Identification of ATP binding residues of a protein from its primary sequence 

Chauhan, J.S., Mishra, N.K. & Raghava, G.P. Identification of ATP binding residues of a protein from its primary sequence. BMC Bioinformatics 10, 434 (2009). https://doi.org/10.1186/1471-2105-10-434 

