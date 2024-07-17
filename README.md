# StageLoWaRAN

To run, go on main and choose if you want to print prediction results or map coverage.

To add gateway, go on GatewayModule and add Gateway information.
To add Data, go on manageDataModule and paste your CSV file.
Then add this CSV file in the code of TransformCSV as for the others. (Note their is two classes for data management because the CSV files changed in format)


Classes:
-Approximaiton predict environmental variable
-Calcul helps other classes with general methods
-DeleteData was used for data 
-Gateways have gateways information and get methods
-Learn_n_RSSI is used to learn environmental variable for train_data
-ManageDataModule transorm CSV into usefull tabs
-PredPos calculate the RSSI given the position
-RealMap shows the heatmap
-RSSI_Model have methods to calculate the RSSI

-SignalPred and VerifPrediction are there to print the effectiveness of the prediction.
