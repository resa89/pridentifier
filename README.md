# Pridentifier  <img align="right" src="img/pridi.png">


This Pridentifier software can be used to investigate what kind of printers can be distinguished with the help of Fourier analysis features. But it can also be used for other classification problems where Fourier analysis seems promising (any textual images). 

Feel free to investigate your (forensic) classification problems with the Pridentifier.


## Installation

You should have installed miniconda. Then use conda to install a new environment from the *environment.yml*:

```bash
conda env create -f environment.yml
```

To activate the new environment type:

```bash
conda activate pridentifier
```

Then install the modules with:

```bash
python setup.py install 
```


## Run the Pridentifier 

To run the Pridentifier desktop application:

```bash
python pridentifier.py
```


## Usage


## Support

For any questions if having problems with the installation or usage contact: trouble@korensic.com


## Roadmap

**GUI optimization**
- responsive design

**Build process**
- integrate ui-generated python automatically in app by adding a inheritance object for additional changes made in app afterwards

**App development**
- add functionality to make evaluation on an uploaded test-set
- save-button for evaluation results
- make possible to analyze more than 8 classes (also display scrollable in GUI)

**Methods development**
- optimize feature selection with local maxima selection methods 


## Trouble shooting 
- change segment size several times, crashes or does not load any more, classes must be loaded again in the data-tab.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

To contribute in the development of the Pridentifier type:

```bash
python setup.py develop 
```


## Authors

- Theresa Kocher (theresa@korensic.com)


## Acknowledgment
This Pridentifer application was developed in close collaboration with Rolf Fauser from the Hochschule für Polizei Baden-Württemberg in Germany. The research idea came into being at the University for Applied Sciences Konstanz within a studies project of Theresa Kocher and Sabrina Hock. This research project was supervised by Prof. Dr. Matthias Franz from the Institute for Optical Systems in Konstanz.

The European Document Experts Working Group (EDEWG) of the European Network of Forensic Science Institutes (ENFSI) have been supporting the development of the Pridentifier for years. Previous projects and partial results of the Pridentifer project were presented at their conferences in Ankara 2014, Frankfurt a. M. 2016 and in Lisbon 2018. In 2018 the EDEWG promoted the productive development of this Pridentifier which was only a prototype in a research context before. That's why as from now, the Pridentifer Application can be used as it is.

I'd like to say a big thank you to all institutions and persons given above.


## License
[MIT](https://choosealicense.com/licenses/mit/)