**Content prediction**


The software makes it possible to:
- train/improve the predictions models
- use trained model to perform predictions

There app comes with models pre-trained on the included data.

**Usage**

***Training***

The app comes pre-trained on the included data. Training is only needed if new data is added.

The data for training is provided in png format and is stored in the _trainingset_ directory. The file name contains the content description, see examples. 

There are 2 training methods available, they can be accessed by calling the following apps:
 - _python train.py_ - trains Resnet18
 - _python trainxgboost_ - trains XGBoostRegressor

Training produces model files that are later used in predictions. 

***Predictions***

The prodiction is available through a web interface. The implementation uses Streamlit, therefore streamlit is required. To perform predictions run '_streamlit run predict.py_' and upload images through the web interface. The predictions will be presented on the website, there is also an option to download them in Excel format.

**Notes**

SessionState used in the webinterface is taken from the following gist: https://gist.github.com/tvst/036da038ab3e999a64497f42de966a92
