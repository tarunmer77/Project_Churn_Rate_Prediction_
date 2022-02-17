import streamlit as st
import pickle,bz2
import time
import numpy as np

pickle_in = bz2.BZ2File('modelfinal.pkl','rb')
model = pickle.load(pickle_in)

@st.cache(persist=True)
def predict_cancel(lead_time,adr,total_of_special_requests,booking_changes,market_segment,
deposit_type,assigned_room_type,customer_type,required_car_parking_spaces,previous_cancellations):
    input=np.array([[lead_time,adr,total_of_special_requests,booking_changes,market_segment,
    deposit_type,assigned_room_type,customer_type,required_car_parking_spaces,previous_cancellations]])
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    st.markdown("## PREDICTING HOTEL BOOKING CANCELLATIONS")
    #st.header("Predicting Hotel Cancellations Using Machine Learning")
    st.text("Choose the Below Parameters to Predict")
    st.markdown("#### Lead Time in days")
    lead_time = st.text_input("",value="0")
    lead_time = float(lead_time)
    st.markdown("#### Average Daily Rate (ADR)")
    adr = st.text_input("Enter the ADR",value="0")
    adr = float(adr)
    st.markdown("#### Total Special Requests")
    total_of_special_requests = st.text_input("Enter the number of special requests from guests",value="0")
    total_of_special_requests = float(total_of_special_requests)
    st.markdown("#### Total Modifications")
    booking_changes = st.text_input("Enter the number of modifications made by guests",value="0")
    booking_changes = float(booking_changes)
    st.markdown("#### Previous Cancellations By Guest")
    previous_cancellations = st.text_input("Enter the number of previous cancellations made by guests",value="0")
    previous_cancellations = float(previous_cancellations)


    st.markdown("#### Market Segment")
    deppo = st.selectbox("Choose the Market Segment",("Aviation","Complementary","Corporate","Direct","Groups","Offline TA/TO","Online TA","Undefined"))
    if deppo == "Aviation":
        market_segment = 0
    elif deppo == "Complementary":
        market_segment = 1
    elif deppo == 'Corporate':
        market_segment = 2
    elif deppo == 'Direct':
        market_segment = 3
    elif deppo == 'Groups':
        market_segment = 4
    elif deppo == 'Offline TA/TO':
        market_segment = 5
    elif deppo == 'Online TA':
        market_segment = 6
    elif deppo == 'Undefined':
        market_segment = 7

        
    st.markdown("#### Deposit Type")
    deposit = st.selectbox("Choose the Deposit Type",("No Deposit","Non Refund","Refundable"))
    if deposit == "No Deposit":
        deposit_type = 0
    elif deposit == 'Non Refund':
        deposit_type = 1
    elif deposit == 'Refundable':
        deposit_type = 2
        
    
    st.markdown("#### Assigned Room Type")
    room_type = st.selectbox("Choose the Assigned Room Type",("A","B","C","D","E","F","G","H","I","J","K","L"))
    if room_type == "A":
        assigned_room_type = 0
    elif room_type == "B":
        assigned_room_type = 1
    elif room_type == "C":
        assigned_room_type = 2
    elif room_type == "D":
        assigned_room_type = 3                               
    elif room_type == "E":
        assigned_room_type = 4
    elif room_type == "F":
        assigned_room_type = 5                      
    elif room_type == "G":
        assigned_room_type = 6
    elif room_type == "H":
        assigned_room_type = 7
    elif room_type == "I":
        assigned_room_type = 8
    elif room_type == "J":
        assigned_room_type = 9
    elif room_type == "K":
        assigned_room_type = 10
    elif room_type == "L":
        assigned_room_type = 11

    st.markdown("#### Customer Type")
    customer = st.selectbox("Choose the Customer Type",("Contract","Group","Transient","Transient-Party"))
    if customer == "Contract":
        customer_type = 0
    elif customer == "Group":
        customer_type = 1
    elif customer == "Transient":
        customer_type = 2
    elif customer == "Transient-Party":
        customer_type = 3
    
    
    st.markdown("#### Car Parking")
    required_car_parking_spaces = st.selectbox("Choose the number of Car Parking Spaces", [1,2,3,4,5,6,7,8])

    html_temp = """
        <div style="background-color:#000000 ;padding:10px">
        <h2 style="color:white;text-align:center;">Hotel Booking Cancellations Prediction ML App</h2>
        </div>
     """
    

    if st.button("Click Here To Predict"):
        output = predict_cancel(lead_time,adr,total_of_special_requests,booking_changes,market_segment,
        deposit_type,assigned_room_type,customer_type,required_car_parking_spaces,previous_cancellations)
        final_output = output * 100
        st.header('Probability of Guest Cancelling Reservation is {}% '.format(final_output))

        if final_output > 50.0:
            st.error("Reservation is not confirmed")
        else:
            st.success("Reservation is confirmed")
             

if __name__=='__main__':
    main()
