# gracescore
Python class to calculate Grace Score mortality risk after Acute Coronary Syndrome

This class is based on the jasvascript functions found on website: https://www.outcomes-umassmed.org/grace/acs_risk2/index.html
I just downloaded the grace_lookups.js script, which seemed to be responsible for calculation of the grace score values in the online calculator and I translated it to a python class.

If you find this useful to you, you may want to cite:
Konrad Pieszko, Jarosław Hiczkiewicz, Paweł Budzianowski, et al., 
“Predicting Long-Term Mortality after Acute Coronary Syndrome Using Machine Learning Techniques and Hematological Markers,” 
Disease Markers, vol. 2019, Article ID 9056402, 9 pages, 2019. https://doi.org/10.1155/2019/9056402.


Example usage:
```python
import pandas as pd
from gracescore import GraceScore 

data=pd.read_csv("sample_data.csv")
Grace=GraceScore()

data['grace_in_hospital']=data.apply(lambda row: Grace.CalculateAdmissionToInHospitalDeath(row['age'],row['EkgHR'], row['SystolicPressure'], row['Creatinine'],row['KillipClass'],row['CardiacArrest'],row['Troponin'] ,row['EkgSTdeviation']),axis=1)

data['grace180']=data.apply(lambda row: Grace.CalculateSixMonthDeath(row['age'],row['EkgHR'], row['SystolicPressure'], row['Creatinine'],row['KillipClass'],row['CardiacArrest'],row['Troponin'] ,row['EkgSTdeviation']),axis=1)

data['grace365']=data.apply(lambda row: Grace.CalculateOneYearDeath(row['age'],row['EkgHR'], row['SystolicPressure'], row['Creatinine'],row['KillipClass'],row['CardiacArrest'],row['Troponin'] ,row['EkgSTdeviation']),axis=1)



```
