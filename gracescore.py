#This class is based on the functions found on website: https://www.outcomes-umassmed.org/grace/acs_risk2/index.html
#I just downloeded the grace_lookups.js script, which seemed to be responsible for calculation of the grace score values
#and I translated it to python class

#This work is licensed under a GNU General Public License

#If you  use this adaptation of Grace Score for publication purposes we kindly ask you to cite:
#Konrad Pieszko, Jarosław Hiczkiewicz, Paweł Budzianowski, et al., 
#“Predicting Long-Term Mortality after Acute Coronary Syndrome Using Machine Learning Techniques and Hematological Markers,” 
#Disease Markers, vol. 2019, Article ID 9056402, 9 pages, 2019. https://doi.org/10.1155/2019/9056402.


import math

class GraceScore:

    def __init__(self):

        #dictionaries for Admission To In Hospital Mortality, all start with Admission
        
        self.__Admission_Age = {
            "29": "1.5399",
            "30": "1.593",
            "31": "1.6461",
            "32": "1.6992",
            "33": "1.7523",
            "34": "1.8054",
            "35": "1.8585",
            "36": "1.9116",
            "37": "1.9647",
            "38": "2.0178",
            "39": "2.0709",
            "40": "2.124",
            "41": "2.1771",
            "42": "2.2302",
            "43": "2.2833",
            "44": "2.3364",
            "45": "2.3895",
            "46": "2.4426",
            "47": "2.4957",
            "48": "2.5488",
            "49": "2.6019",
            "50": "2.655",
            "51": "2.7081",
            "52": "2.7612",
            "53": "2.8143",
            "54": "2.8674",
            "55": "2.9205",
            "56": "2.9736",
            "57": "3.0267",
            "58": "3.0798",
            "59": "3.1329",
            "60": "3.186",
            "61": "3.2391",
            "62": "3.2922",
            "63": "3.3453",
            "64": "3.3984",
            "65": "3.4515",
            "66": "3.5046",
            "67": "3.5577",
            "68": "3.6108",
            "69": "3.6639",
            "70": "3.717",
            "71": "3.7701",
            "72": "3.8232",
            "73": "3.8763",
            "74": "3.9294",
            "75": "3.9825",
            "76": "4.0356",
            "77": "4.0887",
            "78": "4.1418",
            "79": "4.1949",
            "80": "4.248",
            "81": "4.3011",
            "82": "4.3542",
            "83": "4.4073",
            "84": "4.4604",
            "85": "4.5135",
            "86": "4.5666",
            "87": "4.6197",
            "88": "4.6728",
            "89": "4.7259",
            "90": "4.779",
            "91": "4.8321",
            "92": "4.8852",
            "93": "4.9383",
            "94": "4.9914",
            "95": "5.0445",
            "96": "5.0976",
            "97": "5.1507",
            "98": "5.2038",
            "99": "5.2569",
            "100": "5.31"
        }
        self.__Admission_Pulse = {
            "49":"0.4263",
            "59.5":"0.51765",
            "74.5":"0.64815",
            "84.5":"0.73515",
            "94.5":"0.82215",
            "104.5":"0.90915",
            "119.5":"1.03965",
            "139.5":"1.21365",
            "174.5":"1.51815",
            "200":"1.74"
        }
        self.__Admission_BloodPressure = {
            "79":"-1.3272",
            "89.5":"-1.5036",
            "104.5":"-1.7556",
            "114.5":"-1.9236",
            "124.5":"-2.0916",
            "134.5":"-2.2596",
            "149.5":"-2.5116",
            "169.5":"-2.8476",
            "180":"-3.024"
        }
        self.__Admission_Creatine =  {
            "0.195":"0.0355485",
            "0.595":"0.1084685",
            "0.995":"0.1813885",
            "1.395":"0.2543085",
            "1.795":"0.3272285",
            "2.995":"0.5459885",
            "4.0":"0.7292"
        }
        self.__Admission_Renal =  {
            "no": "0.09115",
            "yes": "0.3646"
        }
        self.__Admission_Killip = {
            "1": "0.6931",
            "2": "1.3862",
            "3": "2.0793",
            "4": "2.7724"
        }
        self.__Admission_Diuretic = {
            "no": "0.6931",
            "yes": "1.73275"
        }
        self.__Admission_Cardiac = {
            "no": "0",
            "yes": "1.4586"
        }
        self.__Admission_ElevatedEnzymes = {
            "no": "0",
            "yes": "0.4700"
        }
        self.__Admission_STEMI ={
            "no": "0",
            "yes": "0.8755"
        }

        #dictionaries for ^-Month Mortality, all start with SixMonth
        
        self.__SixMonth_Age = {
            "29": "0",
            "30": "0",
            "31": "0",
            "32": "0",
            "33": "0",
            "34": "0",
            "35": "0",
            "36": "1.8",
            "37": "3.6",
            "38": "5.4",
            "39": "7.2",
            "40": "9",
            "41": "10.8",
            "42": "12.6",
            "43": "14.4",
            "44": "16.2",
            "45": "18",
            "46": "19.8",
            "47": "21.6",
            "48": "23.4",
            "49": "25.2",
            "50": "27",
            "51": "28.8",
            "52": "30.6",
            "53": "32.4",
            "54": "34.2",
            "55": "36",
            "56": "37.8",
            "57": "39.6",
            "58": "41.4",
            "59": "43.2",
            "60": "45",
            "61": "46.8",
            "62": "48.6",
            "63": "50.4",
            "64": "52.2",
            "65": "54",
            "66": "55.9",
            "67": "57.8",
            "68": "59.7",
            "69": "61.6",
            "70": "63.5",
            "71": "65.4",
            "72": "67.3",
            "73": "69.2",
            "74": "71.1",
            "75": "73",
            "76": "74.8",
            "77": "76.6",
            "78": "78.4",
            "79": "80.2",
            "80": "82",
            "81": "83.8",
            "82": "85.6",
            "83": "87.4",
            "84": "89.2",
            "85": "91",
            "86": "92.8",
            "87": "94.6",
            "88": "96.4",
            "89": "98.2",
            "90": "100",
            "91": "100",
            "92": "100",
            "93": "100",
            "94": "100",
            "95": "100",
            "96": "100",
            "97": "100",
            "98": "100",
            "99": "100",
            "100": "100"
        }
        self.__SixMonth_Pulse = {
            "49":"0",
            "59.5":"0",
            "74.5":"1.35",
            "84.5":"3.9",
            "94.5":"6.35",
            "104.5":"8.9",
            "119.5":"12.85",
            "139.5":"18.85",
            "174.5": "29.35",
            "200":"34.0"
        }
        self.__SixMonth_BloodPressure = {
            "79":"40",
            "89.5":"37.15",
            "104.5":"32.65",
            "114.5":"29.2",
            "124.5":"25.65",
            "134.5":"22.65",
            "149.5":"16.2",
            "169.5":"11.15",
            "180":"8.0"
        }
        self.__SixMonth_Creatine = {
            "0.195": "0.975",
            "0.595": "3.975",
            "0.995": "6.975",
            "1.395": "9.95",
            "1.795": "12.95",
            "2.995": "20.965",
            "4.0":   "28"
        }
        self.__SixMonth_Renal ={
            "no": "3.5",
            "yes": "14"
        }
        self.__SixMonth_Killip = {
            "1": "0",
            "2": "15",
            "3": "29",
            "4": "44"
        }
        self.__SixMonth_Diuretic = {
            "no": "0",
            "yes": "20"
        }
        self.__SixMonth_Cardiac = {
            "no": "0",
            "yes": "1"
        }
        self.__SixMonth_ElevatedEnzymes =  {
            "no": "0",
            "yes": "1"
        }
        self.__SixMonth_STEMI ={
            "no": "0",
            "yes": "1"
        }

        #dictionaries for OneYear Mortality, all start with OneYear
        self.__OneYear_Age = {
            "29":"1.193553",
            "30":"1.23471",
            "31":"1.275867",
            "32":"1.317024",
            "33":"1.358181",
            "34":"1.399338",
            "35":"1.440495",
            "36":"1.481652",
            "37":"1.522809",
            "38":"1.563966",
            "39":"1.605123",
            "40":"1.64628",
            "41":"1.687437",
            "42":"1.728594",
            "43":"1.769751",
            "44":"1.810908",
            "45":"1.852065",
            "46":"1.893222",
            "47":"1.934379",
            "48":"1.975536",
            "49":"2.0167005",
            "50":"2.0579297",
            "51":"2.0993009",
            "52":"2.1408916",
            "53":"2.1827791",
            "54":"2.2250408",
            "55":"2.2677541",
            "56":"2.3109965",
            "57":"2.3548453",
            "58":"2.3993779",
            "59":"2.4446718",
            "60":"2.4908043",
            "61":"2.5378528",
            "62":"2.5858947",
            "63":"2.6350075",
            "64":"2.6852685",
            "65":"2.7367551",
            "66":"2.7895448",
            "67":"2.8437127",
            "68":"2.8992632",
            "69":"2.9561152",
            "70":"3.0141823",
            "71":"3.0733784",
            "72":"3.1336173",
            "73":"3.1948128",
            "74":"3.2568786",
            "75":"3.3197285",
            "76":"3.3832763",
            "77":"3.4474359",
            "78":"3.5121209",
            "79":"3.5772452",
            "80":"3.6427226",
            "81":"3.7084667",
            "82":"3.7743915",
            "83":"3.8404108",
            "84":"3.9064488",
            "85":"3.9724869",
            "86":"4.0385249",
            "87":"4.104563",
            "88":"4.1706011",
            "89":"4.2366391",
            "90":"4.3026772",
            "91":"4.3687153",
            "92":"4.4347533",
            "93":"4.5007914",
            "94":"4.5668295",
            "95":"4.6328675",
            "96":"4.6989056",
            "97":"4.7649437",
            "98":"4.8309817",
            "99":"4.8970198",
            "100":"4.9630578"
        }
        self.__OneYear_Pulse = {
            "49":"0.2145873",
            "59.5":"0.2687747",
            "74.5":"0.5049219",
            "84.5":"0.7361786",
            "94.5":"0.8628367",
            "104.5":"0.8966225",
            "119.5":"0.8578086",
            "139.5":"0.7824602",
            "174.5":"0.6506006",
            "200":"0.5545314"
        }
        self.__OneYear_BloodPressure = {
            "79":"0.4071228",
            "89.5":"0.2421043",
            "104.5":"0.0063635",
            "114.5":"-0.1499551",
            "124.5":"-0.2985642",
            "134.5":"-0.4299701",
            "149.5":"-0.5769774",
            "169.5":"-0.6951633",
            "180":"-0.7399799"
        }
        self.__OneYear_Creatine ={
            "0.195":"-0.0999551",
            "0.595":"-0.3049911",
            "0.995":"-0.2920628",
            "1.395":"0.2625441",
            "1.795":"0.4717919",
            "2.995":"0.6085038",
            "4.0":"0.7131714"
        }
        self.__OneYear_Killip ={
            "1": "0",
            "2": "0.63827",
            "3": "0.85325",
            "4": "1.29372"
        }
        self.__OneYear_Cardiac ={
            "no": "0",
            "yes": "0.87185"
        }
        self.__OneYear_ElevatedEnzymes ={
            "no": "0",
            "yes": "0.37660"
        }
        self.__OneYear_STEMI ={
            "no": "0",
            "yes": "0.44303"
        }
        ####################

        

    #############################################  FUNCTIONS   #########################################
    #fuctions to look up dictionaries
    #def __myroundstr(self,x):
        
        
    def __lookupAge(self,age,dictAge):
        if (math.isnan(age)):
            return None
        else:
            if(age<29):
                age=29
            roundstr=str(round(age))
        return float(dictAge[roundstr])

    def __lookupPulse(self,pulse, dictPulse):
    #accepts pulse value as float
        if(pulse<50):
            npulse=dictPulse["49"]
        elif(50<pulse<70):
            npulse=dictPulse["59.5"]
        elif(70<=pulse<80):
            npulse=dictPulse["74.5"]
        elif(80<=pulse<90):
            npulse=dictPulse["84.5"]
        elif(90<=pulse<100):
            npulse=dictPulse["94.5"]
        elif(100<=pulse<110):
            npulse=dictPulse["104.5"]
        elif(110<=pulse<130):
            npulse=dictPulse["119.5"]
        elif(130<=pulse<149):
            npulse=dictPulse["139.5"]
        elif(150<=pulse<199):
            npulse=dictPulse["174.5"]
        elif(200<=pulse):
            npulse=dictPulse["200"]
        else:
            return None
        return float(npulse)

    def __lookupBloodPressure(self,bp, dictBloodPressure):
    #accepts BP value as float
        if(bp<80):
            nbp=dictBloodPressure["79"]
        elif(80<=bp<100):
            nbp=dictBloodPressure["89.5"]
        elif(100<=bp<110):
            nbp=dictBloodPressure["104.5"]
        elif(110<=bp<120):
            nbp=dictBloodPressure["114.5"]
        elif(120<=bp<130):
            nbp=dictBloodPressure["124.5"]
        elif(130<=bp<140):
            nbp=dictBloodPressure["134.5"]
        elif(140<=bp<160):
            nbp=dictBloodPressure["149.5"]
        elif(160<=bp<180):
            nbp=dictBloodPressure["169.5"]
        elif(180<=bp):
            nbp=dictBloodPressure["180"]
        else:
            return None
        return float(nbp)

    def __lookupCrea(self,cr, dictCrea):
        if(cr<0.039):
            ncr=dictCrea["0.195"]
        elif(0.4<=cr<0.8):
            ncr=dictCrea["0.595"]
        elif(0.8<=cr<1.2):
            ncr=dictCrea["0.995"]
        elif(1.2<=cr<1.6):
            ncr=dictCrea["1.395"]
        elif(1.6<=cr<2.0):
            ncr=dictCrea["1.795"]
        elif(2.0<=cr<4.0):
            ncr=dictCrea["2.995"]
        elif(4.0<=cr):
            ncr=dictCrea["4.0"]
        else:
            return None
        return float(ncr)

    def __lookupTF(self,TF, dictTF):
        if(TF==True):
            return float(dictTF["yes"])
        elif(TF==False):
            return float(dictTF["no"])
        else:
             return None

    def __lookupKillip(self,killip, dictKillip):
        return float(dictKillip[str(killip)])

    def CalculateOneYearDeath(self,age, pulse, bloodPressure, creatinine, killip, cardiac, enzymes, stemi):
        
        ageValue = self.__lookupAge(age,self.__OneYear_Age)
        pulseValue = self.__lookupPulse(pulse, self.__OneYear_Pulse)
        bloodPressureValue = self.__lookupBloodPressure(bloodPressure,self.__OneYear_BloodPressure)
        killipValue = self.__lookupKillip(killip, self.__OneYear_Killip)
        creatinineValue = self.__lookupCrea(creatinine, self.__OneYear_Creatine)
        cardiacValue = self.__lookupTF(cardiac, self.__OneYear_Cardiac)
        enzymesValue = self.__lookupTF(enzymes, self.__OneYear_ElevatedEnzymes)
        stemiValue = self.__lookupTF(stemi, self.__OneYear_STEMI)

        try:
            xbhat = ageValue + pulseValue + bloodPressureValue + creatinineValue + cardiacValue + enzymesValue + stemiValue + killipValue
        except:
            return None
        sZeroT = 0.9983577131
        temp = math.exp(xbhat)
        temp2 = math.pow(sZeroT, temp)
        result = 1 - temp2
        
        return result


    def CalculateAdmissionToInHospitalDeath(self,age, pulse, bloodPressure, creatinine,  killip,  cardiac, enzymes, stemi):

        ageValue = self.__lookupAge(age,self.__Admission_Age)
        pulseValue = self.__lookupPulse(pulse, self.__Admission_Pulse)
        bloodPressureValue = self.__lookupBloodPressure(bloodPressure,self.__Admission_BloodPressure)
        killipValue = self.__lookupKillip(killip, self.__Admission_Killip)
        creatinineValue = self.__lookupCrea(creatinine, self.__Admission_Creatine)
        cardiacValue = self.__lookupTF(cardiac, self.__Admission_Cardiac)
        enzymesValue = self.__lookupTF(enzymes, self.__Admission_ElevatedEnzymes)
        stemiValue = self.__lookupTF(stemi, self.__Admission_STEMI)

        fiddleFactor = -7.7035
        try:
            xbhat = fiddleFactor + ageValue + pulseValue+ bloodPressureValue + creatinineValue + cardiacValue + enzymesValue + stemiValue + killipValue
        except:
            return None
        temp = math.exp(xbhat)

        probabilityOfDeath = temp / (1 + temp)

        


        return probabilityOfDeath
    

    def CalculateSixMonthDeath(self,age, pulse, bloodPressure, creatinine,  killip,  cardiac, enzymes, stemi):

        ageValue = self.__lookupAge(age,self.__SixMonth_Age)
        pulseValue = self.__lookupPulse(pulse, self.__SixMonth_Pulse)
        bloodPressureValue = self.__lookupBloodPressure(bloodPressure,self.__SixMonth_BloodPressure)
        killipValue = self.__lookupKillip(killip, self.__SixMonth_Killip)
        creatinineValue = self.__lookupCrea(creatinine, self.__SixMonth_Creatine)
        cardiacValue = self.__lookupTF(cardiac, self.__SixMonth_Cardiac)
        enzymesValue = self.__lookupTF(enzymes, self.__SixMonth_ElevatedEnzymes)
        stemiValue = self.__lookupTF(stemi, self.__SixMonth_STEMI)


        try:
            deathmi_pt = killipValue + bloodPressureValue + pulseValue + ageValue + creatinineValue + (17 * stemiValue) + (13 * enzymesValue) + (30 * cardiacValue)
        except:
            return None

        if (deathmi_pt <= 6):
            probability = 0.002
        
        elif (deathmi_pt > 7 and deathmi_pt <= 27):
            probability = 0.004
        
        elif (deathmi_pt > 27 and deathmi_pt <= 39):
            probability = 0.006
        
        elif (deathmi_pt > 39 and deathmi_pt <= 48):
            probability = 0.008
        
        elif (deathmi_pt > 48 and deathmi_pt <= 55):
            probability = 0.01
        
        elif (deathmi_pt > 55 and deathmi_pt <= 60):
            probability = 0.012
        
        elif (deathmi_pt > 60 and deathmi_pt <= 65):
            probability = 0.014
        
        elif (deathmi_pt > 65 and deathmi_pt <= 69):
            probability = 0.016
        
        elif (deathmi_pt > 69 and deathmi_pt <= 73):
            probability = 0.018
        
        elif (deathmi_pt > 73 and deathmi_pt <= 76):
            probability = 0.02
        
        elif (deathmi_pt > 76 and deathmi_pt <= 88):
            probability = 0.03
        
        elif (deathmi_pt > 88 and deathmi_pt <= 97):
            probability = 0.04
        
        elif (deathmi_pt > 97 and deathmi_pt <= 104):
            probability = 0.05
        
        elif (deathmi_pt > 104 and deathmi_pt <= 110):
            probability = 0.06
        
        elif (deathmi_pt > 110 and deathmi_pt <= 115):
            probability = 0.07
        
        elif (deathmi_pt > 115 and deathmi_pt <= 119):
            probability = 0.08
        
        elif (deathmi_pt > 119 and deathmi_pt <= 123):
            probability = 0.09
        
        elif (deathmi_pt > 123 and deathmi_pt <= 126):
            probability = 0.10
        
        elif (deathmi_pt > 126 and deathmi_pt <= 129):
            probability = 0.11
        
        elif (deathmi_pt > 129 and deathmi_pt <= 132):
            probability = 0.12
        
        elif (deathmi_pt > 132 and deathmi_pt <= 134):
            probability = 0.13
        
        elif (deathmi_pt > 134 and deathmi_pt <= 137):
            probability = 0.14
        
        elif (deathmi_pt > 137 and deathmi_pt <= 139):
            probability = 0.15
        
        elif (deathmi_pt > 139 and deathmi_pt <= 141):
            probability = 0.16
        
        elif (deathmi_pt > 141 and deathmi_pt <= 143):
            probability = 0.17
        
        elif (deathmi_pt > 143 and deathmi_pt <= 146):
            probability = 0.18
        
        elif (deathmi_pt > 146 and deathmi_pt <= 147):
            probability = 0.19
        
        elif (deathmi_pt > 147 and deathmi_pt <= 149):
            probability = 0.20
        
        elif (deathmi_pt > 149 and deathmi_pt <= 150):
            probability = 0.21
        
        elif (deathmi_pt > 150 and deathmi_pt <= 152):
            probability = 0.22
        
        elif (deathmi_pt > 152 and deathmi_pt <= 153):
            probability = 0.23
        
        elif (deathmi_pt > 153 and deathmi_pt <= 155):
            probability = 0.24
        
        elif (deathmi_pt > 155 and deathmi_pt <= 156):
            probability = 0.25
        
        elif (deathmi_pt > 156 and deathmi_pt <= 158):
            probability = 0.26
        
        elif (deathmi_pt > 158 and deathmi_pt <= 159):
            probability = 0.27
        
        elif (deathmi_pt > 159 and deathmi_pt <= 160):
            probability = 0.28
        
        elif (deathmi_pt > 160 and deathmi_pt <= 162):
            probability = 0.29
        
        elif (deathmi_pt > 162 and deathmi_pt <= 163):
            probability = 0.3
        
        elif (deathmi_pt > 163 and deathmi_pt <= 174):
            probability = 0.4
        
        elif (deathmi_pt > 174 and deathmi_pt <= 183):
            probability = 0.5
        
        elif (deathmi_pt > 183 and deathmi_pt <= 191):
            probability = 0.6
        
        elif (deathmi_pt > 191 and deathmi_pt <= 200):
            probability = 0.7
        
        elif (deathmi_pt > 200 and deathmi_pt <= 208):
            probability = 0.8
        
        elif (deathmi_pt > 208 and deathmi_pt <= 219):
            probability = 0.9
        
        elif (deathmi_pt > 219 and deathmi_pt <= 240):
            probability = 0.99
        
        elif (deathmi_pt > 240):
            probability = 1.13
        

        

        probability = probability * (80 / 91)

        if (probability > .90):
            probability = .92
        

      
        return probability
      
    