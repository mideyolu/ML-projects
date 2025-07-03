import streamlit as st
from utils.features import cat_features, num_features
from utils.loader import predictor


def prediction():
    st.title("Bank Customer Attrition Prediction")
    st.markdown("Please fill in all the required customer details below")

    input_data ={}

    # collect all categorical inputs with dropdowns
    for i in range(0, len(cat_features),2):
        cols = st.columns(2)
        col1_name = cat_features[i]
        options = list(predictor.preprocessor.encoders[col1_name].classes_)
        input_data[col1_name]= cols[0].selectbox(label=col1_name, options=options)

        if i + 1 < len(cat_features):
            col2_name= cat_features[i+1]
            options2= list(predictor.preprocessor.encoders[col2_name].classes_)
            input_data[col2_name]= cols[1].selectbox(label=col2_name, options=options2)

    # numerical inputs two per row
    for i in range(0, len(num_features), 2):
        cols = st.columns(2)
        col1_name = num_features[i]
        input_data[col1_name] = cols[0].number_input(label=col1_name, value=0.0)

        if i + 1 < len(num_features):
            col2_name = num_features[i + 1]
            input_data[col2_name] = cols[1].number_input(label=col2_name, value=0.0)

    # prediction button
    if st.button("Predict"):
        prediction, probability = predictor.predict(input_dict=input_data)

        if prediction ==1:
            st.error(f"Customer is likely to churn!")
            st.error(f"Confidence: {probability:.2f}")
        else:
            st.success(f"Customer isn't likely to churn!")
            st.success(f"Confidence: {probability:.2f}")
