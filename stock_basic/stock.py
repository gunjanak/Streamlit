import numpy as np
import streamlit as st
import pandas as pd


def load_data():
    st.write("Upload a csv file")

    #upload file
    uploaded_file = st.file_uploader("Choose a file",'csv')

    #Setting flag for uploaded 
    if(uploaded_file == None):
        status = False
    else:
        status = True

    #returning uploaded_file and status of flad
    to_return = [uploaded_file,status]
    return to_return

def read_data(uploaded_file):

    #reading the uploaded file
    df = pd.read_csv(uploaded_file)

    #Setting the Date column to pandas date
    df['Date']=pd.to_datetime(df['Date']).dt.date

    #Setting date as indes
    df = df.set_index('Date')


    #printing the dataframe
    st.dataframe(df,800,300)
    return df

#function to plot the various aspects of dataframe
def plot_dataframe(df):
    st.title('Plot graph')
    #Making a list of columns of present in data frame
    col_list = list(df.columns.values)

    #Adding None at begining of the list to plot nothing when nothing is selected
    col_list.insert(0,'None')
    length = len(col_list)

    #Putting col_list in selectbox in sidebar
    op = st.sidebar.selectbox('Option',col_list)
    #print the selected option
    st.write('You selected',op)

    #Does not print anything when 'None' is selected or by default
    if op == col_list[0]:
        pass
    #Print according to selected option in selectbox sidebar
    else:
        st.line_chart(df[op],1000)


#Following function can plot multiple parameters in the dataframe
def multi_plot_dataframe(df):
    st.title('Plot graph of multiple parameters')
   
    col_list = list(df.columns.values)

    options = st.multiselect('Select:',col_list)
       
    st.write('You Selected: ',options)


    st.line_chart(df[options])


#The main function of streamlit
def main():

    #Setting the title
    st.title('Stock Visualization Basic')

    #Setting the sidebar
    st.sidebar.title('Sidebar')

    #Setting the flag
    status = False

    #Calling the load_data function
    uploaded_file,status = load_data()

    #The following block of code only runs when a file is uploaded
    if(status == True):

        #Calling the read data function defined above
        df = read_data(uploaded_file)

        #calling the plot dataframe function defined above
        plot_dataframe(df)

        #calling the multi_plot_dataframe function defined above
        multi_plot_dataframe(df)



if __name__ == '__main__':
    main()