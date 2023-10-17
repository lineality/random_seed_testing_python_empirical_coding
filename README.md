# random_seed_testing_python_empirical_coding

Empirically test if python
global and local settings of random seeds.

e.g.
At least in colab ipython notebooks,
global random seed setting do NOT apply within function
and resetting the random seed in function does NOT change the global setting.

Merely importing a global seed setting variable does not alter this.

Only manually resetting the random see to a global (or imported) ~global value
will make the random seed globally uniform (in all functions).
