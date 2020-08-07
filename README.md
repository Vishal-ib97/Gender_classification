# Gender classification
Binary classification of images based on gender using keras.

# Model Conversion
The first task involved converting the MATLAB model files to Tensorflow (keras) format.
First, the MATLAB weights were loaded and the model information was extracted. Then, based on the extracted information about the reference model, 
the base model was built. On building the base model, the weights were loaded onto the respective layers.

source: [convert matlab models to keras](https://sefiks.com/2019/07/15/how-to-convert-matlab-models-to-keras/)

# Data preparation
The images were compiled into two folders (male and female). Due to computational constraints, a random sample of 2000 (1000 male and 1000 female) images were used from the entire dataset. 80% of the images were used for training and 20% was used as validation data while training.

# Model Compilation and Training
Once the model was ready with the loaded weights, the weights were frozen and dense layers were added along with softmax activation function in the final layer.
The model was trained using Adam optimizer(learning rate = 0.001) with categorical crossentropy loss.
Early stopping constrained on the validation loss was used.
After 6 epochs, the model achieved a validation accuracy of 96%. 

# Evaluation and Results
The trained model was then evaluated on a test dataset with a random sample of 500 (250 female and 250 male) images (ones that were not used for training).
An accuracy of 95.4% was achieved with an AUC of 0.987 confirming that the model is really good at distinguishing between the classes.
Further, the model also achieved good precision and recall scores for both the classes.

|               |     Male    |   female   |
| ------------- | ------------| -----------|       
|     Recall    |     0.95    |   0.96     |
|   Precision   |     0.96    |   0.95     |


Note: The results can be further improved by incorporating more or the entire available data.

# Running the code

The model was trained using Google Colab notebooks.
Use the following scripts in the specified order to achieve the mentioned results:
1. data_preprocess.py to load and split the data into train and validation.
2. model_conversion.py to perfrom model conversion.
3. train.py to load and train the model.
4. predict.py to load and evaluate the model.

[Google Colab](https://colab.research.google.com/drive/10fB9pSFMSn1ETmYA2SxLwlxWGySZ5t4p?usp=sharing)
