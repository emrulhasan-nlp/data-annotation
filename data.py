import pandas as pd
import streamlit as st
st.set_page_config(page_title="Reading News articles", layout="wide")

df=pd.read_csv("./data/data_annotation.csv")
#name=input("Please Enter your name: ")

batch_size=10

num_batches=int(len(df)/10)
st.markdown(
    "<h1 style='text-align: center;'>Data Annotation</h1>",
    unsafe_allow_html=True
)
while True:
    try:
        i=int(input("Please Enter your code number: "))
        break
    except ValueError:
        print('Your code number is invalid. Please Enter your correct code number')
    
while i<num_batches:
    start_idx = i * batch_size
    end_idx = start_idx + batch_size
    # Create a batch dataframe and add it to the list
    batch_df = df.iloc[start_idx:end_idx]
    
    for idx, row in batch_df.iterrows():
        # print(row['users'])
        # #print(row[0])
        users=row['users']
        items=row['items']
        user_documents=row['user_documents']
        item_documents=row['item_documents']
        
        st.subheader(f"Index: {idx}, userID: {row['users']}, itemID: {row['items']}")
        #st.subheader(f"userID: {row['items']}")
        
        st.write(f"User documents:\n {row['user_documents']}")
        st.write(f"User documents:\n {row['item_documents']}")

        #break
        
    break

