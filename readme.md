# Pridentifier

The Pridentifier is a research project with the goal to identify the original printer of a given print (even of small snippets of a print).

To automatically identify the original printer, the individual 'handwriting' of every printer has to be analyzed in advance. For that, Fourier analysis featuers are used.

This Pridentifier software can be used to investigate what kind of printers can be distinguished with the help of Fourier analysis features. But it can also be used for other classification problems where Fourier analysis seems promising. 

Feel free to investigate your forensic classification problems with the Pridentifier.


## Installation

You should have installed miniconda. Then use conda to install a new environment from the *environment.yml*:

```bash
conda env create -f environment.yml
```

To activate the new environment type:

```bash
conda activate pridi
```


## Run the Pridentifier 

To run the Pridentifier desktop application:

```bash
python pridentifier.py
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```


## License
[MIT](https://choosealicense.com/licenses/mit/)