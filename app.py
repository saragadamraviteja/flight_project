from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        dep_time_hour = Dep_hour + (Dep_min/60)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        arr_time_hour = Arrival_hour+(Arrival_min/60)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        Duration_hour = dur_hour+(dur_min/60)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        airline=request.form['airline']
        if(airline=='Jet Airways'):
            A_Air_Asia = 0
            A_Air_India = 0
            A_GoAir = 0
            A_IndiGo = 0
            A_Jet_Airways = 1
            A_Jet_Airways_Business = 0
            A_Multiple_carriers = 0
            A_Multiple_carriers_Premium_economy = 0
            A_SpiceJet = 0
            A_Trujet = 0
            A_Vistara = 0
            A_Vistara_Premium_economy = 0

        elif (airline=='IndiGo'):
            A_Air_Asia = 0
            A_Air_India = 0
            A_GoAir = 0
            A_IndiGo = 1
            A_Jet_Airways = 0
            A_Jet_Airways_Business = 0
            A_Multiple_carriers = 0
            A_Multiple_carriers_Premium_economy = 0
            A_SpiceJet = 0
            A_Trujet = 0
            A_Vistara = 0
            A_Vistara_Premium_economy = 0

        elif (airline=='Air India'):
            A_Air_Asia = 0
            A_Air_India = 1
            A_GoAir = 0
            A_IndiGo = 0
            A_Jet_Airways = 0
            A_Jet_Airways_Business = 0
            A_Multiple_carriers = 0
            A_Multiple_carriers_Premium_economy = 0
            A_SpiceJet = 0
            A_Trujet = 0
            A_Vistara = 0
            A_Vistara_Premium_economy = 0
            
        elif (airline=='Multiple carriers'):
            A_Air_Asia = 0
            A_Air_India = 0
            A_GoAir = 0
            A_IndiGo = 0
            A_Jet_Airways = 0
            A_Jet_Airways_Business = 0
            A_Multiple_carriers = 1
            A_Multiple_carriers_Premium_economy = 0
            A_SpiceJet = 0
            A_Trujet = 0
            A_Vistara = 0
            A_Vistara_Premium_economy = 0
            
        elif (airline=='SpiceJet'):
            A_Air_Asia = 0
            A_Air_India = 0
            A_GoAir = 0
            A_IndiGo = 0
            A_Jet_Airways = 0
            A_Jet_Airways_Business = 0
            A_Multiple_carriers = 0
            A_Multiple_carriers_Premium_economy = 0
            A_SpiceJet = 1
            A_Trujet = 0
            A_Vistara = 0
            A_Vistara_Premium_economy = 0 
            
        elif (airline=='Vistara'):
            A_Air_Asia = 0
            A_Air_India = 0
            A_GoAir = 0
            A_IndiGo = 0
            A_Jet_Airways = 0
            A_Jet_Airways_Business = 0
            A_Multiple_carriers = 0
            A_Multiple_carriers_Premium_economy = 0
            A_SpiceJet = 0
            A_Trujet = 0
            A_Vistara = 1
            A_Vistara_Premium_economy = 0

        elif (airline=='GoAir'):
            A_Air_Asia = 0
            A_Air_India = 0
            A_GoAir = 1
            A_IndiGo = 0
            A_Jet_Airways = 0
            A_Jet_Airways_Business = 0
            A_Multiple_carriers = 0
            A_Multiple_carriers_Premium_economy = 0
            A_SpiceJet = 0
            A_Trujet = 0
            A_Vistara = 0
            A_Vistara_Premium_economy = 0

        elif (airline=='Multiple carriers Premium economy'):
            A_Air_Asia = 0
            A_Air_India = 0
            A_GoAir = 0
            A_IndiGo = 0
            A_Jet_Airways = 0
            A_Jet_Airways_Business = 0
            A_Multiple_carriers = 0
            A_Multiple_carriers_Premium_economy = 1
            A_SpiceJet = 0
            A_Trujet = 0
            A_Vistara = 0
            A_Vistara_Premium_economy = 0

        elif (airline=='Jet Airways Business'):
            A_Air_Asia = 0
            A_Air_India = 0
            A_GoAir = 0
            A_IndiGo = 0
            A_Jet_Airways = 0
            A_Jet_Airways_Business = 1
            A_Multiple_carriers = 0
            A_Multiple_carriers_Premium_economy = 0
            A_SpiceJet = 0
            A_Trujet = 0
            A_Vistara = 0
            A_Vistara_Premium_economy = 0

        elif (airline=='Vistara Premium economy'):
            A_Air_Asia = 0
            A_Air_India = 0
            A_GoAir = 0
            A_IndiGo = 0
            A_Jet_Airways = 0
            A_Jet_Airways_Business = 0
            A_Multiple_carriers = 0
            A_Multiple_carriers_Premium_economy = 0
            A_SpiceJet = 0
            A_Trujet = 0
            A_Vistara = 0
            A_Vistara_Premium_economy = 1
            
        elif (airline=='Trujet'):
            A_Air_Asia = 0
            A_Air_India = 0
            A_GoAir = 0
            A_IndiGo = 0
            A_Jet_Airways = 0
            A_Jet_Airways_Business = 0
            A_Multiple_carriers = 0
            A_Multiple_carriers_Premium_economy = 0
            A_SpiceJet = 0
            A_Trujet = 1
            A_Vistara = 0
            A_Vistara_Premium_economy = 0

        else:
            A_Air_Asia = 1
            A_Air_India = 0
            A_GoAir = 0
            A_IndiGo = 0
            A_Jet_Airways = 0
            A_Jet_Airways_Business = 0
            A_Multiple_carriers = 0
            A_Multiple_carriers_Premium_economy = 0
            A_SpiceJet = 0
            A_Trujet = 0
            A_Vistara = 0
            A_Vistara_Premium_economy = 0

        Source = request.form["Source"]
        if (Source == 'New Delhi'):
            S_Delhi = 1
            S_Kolkata = 0
            S_Mumbai = 0
            S_Chennai = 0
            S_Banglore = 0

        elif (Source == 'Kolkata'):
            S_Delhi = 0
            S_Kolkata = 1
            S_Mumbai = 0
            S_Chennai = 0
            S_Banglore = 0

        elif (Source == 'Mumbai'):
            S_Delhi = 0
            S_Kolkata = 0
            S_Mumbai = 1
            S_Chennai = 0
            S_Banglore = 0

        elif (Source == 'Chennai'):
            S_Delhi = 0
            S_Kolkata = 0
            S_Mumbai = 0
            S_Chennai = 1
            S_Banglore = 0

        else:
            S_Delhi = 0
            S_Kolkata = 0
            S_Mumbai = 0
            S_Chennai = 0
            S_Banglore = 1

        Destination = request.form["Destination"]
        if (Source == 'Cochin'):
            D_Cochin = 1
            D_New_Delhi = 0
            D_Hyderabad = 0
            D_Kolkata = 0
            D_Banglore = 0
    

        elif (Destination == 'New_Delhi'):
            D_Cochin = 0
            D_New_Delhi = 1
            D_Hyderabad = 0
            D_Kolkata = 0
            D_Banglore = 0

        elif (Destination == 'Hyderabad'):
            D_Cochin = 0
            D_New_Delhi = 0
            D_Hyderabad = 1
            D_Kolkata = 0
            D_Banglore = 0

        elif (Destination == 'Kolkata'):
            D_Cochin = 0
            D_New_Delhi = 0
            D_Hyderabad = 0
            D_Kolkata = 1
            D_Banglore = 0

        else:
            D_Cochin = 0
            D_New_Delhi = 0
            D_Hyderabad = 0
            D_Kolkata = 0
            D_Banglore = 1

        if Source == Destination:
            return render_template("index.html",prediction_text="You shouldn't select same location for destination.")
        
        if date_arr < date_dep:
            return render_template("index.html",prediction_text="You should select arrival date and time properly.")

        ['Total_Stops', 'Journey_day', 'Journey_month', 'dep_time_hour',
       'arr_time_hour', 'Duration_hour', 'S_Banglore', 'S_Chennai', 'S_Delhi',
       'S_Kolkata', 'S_Mumbai', 'D_Banglore', 'D_Cochin', 'D_Hyderabad',
       'D_Kolkata', 'D_New Delhi', 'A_Air Asia', 'A_Air India', 'A_GoAir',
       'A_IndiGo', 'A_Jet Airways', 'A_Jet Airways Business',
       'A_Multiple carriers', 'A_Multiple carriers Premium economy',
       'A_SpiceJet', 'A_Trujet', 'A_Vistara', 'A_Vistara Premium economy']

        prediction=model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            dep_time_hour,
            arr_time_hour,
            Duration_hour,
            S_Banglore,
            S_Chennai,
            S_Delhi,
            S_Kolkata,
            S_Mumbai,
            D_Banglore,
            D_Cochin,D_Hyderabad,D_Kolkata,D_New_Delhi,
            A_Air_Asia,
            A_Air_India,
            A_GoAir,
            A_IndiGo,
            A_Jet_Airways,
            A_Jet_Airways_Business,
            A_Multiple_carriers,
            A_Multiple_carriers_Premium_economy,
            A_SpiceJet,
            A_Trujet,
            A_Vistara,
            A_Vistara_Premium_economy    
        ]])

        output=round(prediction[0],2)

        return render_template('index.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
