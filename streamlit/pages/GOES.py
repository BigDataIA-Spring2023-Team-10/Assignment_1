import streamlit as st
import sqlite_main as db_methods
import backend_ops as ops
import boto3
import re

st.title('GOES')
st.subheader('Search by Fields')

product  = ["ABI-L1b-RadC"]

selectedProduct = st.selectbox("Product", product)

year, day, hour = st.columns(3)

year_list = db_methods.geos_get_year()['year'].values.tolist()

with year:
    selectedYear = st.selectbox("Year", year_list)
    # ops.create_steamlit_logs(ops.getCloudwatchInstance(), f"Selected Year {selectedYear}")

day_list = db_methods.geos_get_day(selectedYear)['day'].values.tolist()

with day:
    selectedDay = st.selectbox("Day", day_list)
    # ops.create_steamlit_logs(ops.getCloudwatchInstance(), f"Selected Day {selectedDay}")

hour_list = db_methods.geos_get_hour(selectedYear, selectedDay)['hour'].values.tolist()

with hour:
    selectedHour = st.selectbox("Hour", hour_list)
    # ops.create_steamlit_logs(ops.getCloudwatchInstance(), f"Selected Hour {selectedHour}")

# files = ["Select search query"]

# def handleSearch():
    # files = ops.geos_query_files(product[0], selectedYear, selectedDay, selectedHour)


if 'btn_clicked' not in st.session_state:
    st.session_state['btn_clicked'] = False
if 'generate_link' not in st.session_state:
    st.session_state['generate_link'] = False
if 'prefix_filename' not in st.session_state:
    st.session_state['prefix_filename'] = False
if "searched_filename" not in st.session_state:
    st.session_state["searched_filename"] = False

def callback():
    st.session_state['btn_clicked'] = True
    ops.create_steamlit_logs(ops.getCloudwatchInstance(), f"Search Hit {selectedProduct} {selectedYear} {selectedDay} {selectedHour}")
    

def generateLink():
    st.session_state['generate_link'] = True

st.button("Search", on_click=callback, key = "search")

selectedFile=""

st.session_state

if st.session_state['btn_clicked']:

    print("called here", selectedHour)

    selectedFile = st.selectbox("Files", ops.geos_query_files(product[0], selectedYear, selectedDay, selectedHour))
    
    st.write(selectedFile)

    st.button("Generate Link", on_click = generateLink, key = "gen_link")      
    

if st.session_state['generate_link']:
    ops.downloadFileAndMove(selectedFile)
    st.write("AWS link")

    st.write("https://damg7245-s3-storage.s3.amazonaws.com/" + selectedFile)


### Search by Filename

st.subheader("Search By File Name")

searchedFilename = st.text_input("Filename", key="filename-search")

if 'file-searched' not in st.session_state:
    st.session_state['file-searched'] = False

if 'file-name-check' not in st.session_state:
    st.session_state['file-name-check'] = False

if 'file-link-generated' not in st.session_state:
    st.session_state['file-link-generated'] = False

def handleSearchedFileName():
    print('************89898******************')
    print(st.session_state['file-searched'])
    if st.session_state['file-searched']:
        pattern = r"^OR_ABI-L1b-RadC-M6C\d{2}_G\d+_s20\d{12}_e20\d{12}_c20\d{12}\.nc$"

        if re.match(pattern, st.session_state['file-searched']):
            st.session_state['file-name-check'] = True
            aws_file_link = ops.get_geos_file_link(st.session_state['file-searched'])
            print("AWS FIle Link", aws_file_link)
            if aws_file_link != "":
                prefix = "https://damg7245-s3-storage.s3.amazonaws.com/"
                st.session_state['file-link-generated'] = prefix + aws_file_link
                st.session_state['filename-search']= ""
        else:
            print(re.match(pattern, st.session_state['file-searched']) )
            st.error('Provide proper file name', icon = "⚠️")
            st.session_state['file-searched']= ""
            st.session_state['filename-search']= ""
            st.session_state['file-link-generated'] = ""


        

if not searchedFilename == "":
    st.session_state['file-searched'] = searchedFilename
    st.button("Generate File Link", on_click = handleSearchedFileName)


if st.session_state['file-name-check']:
    st.write("File name")
    st.write(st.session_state['file-searched'])

if st.session_state['file-link-generated']:
    st.write(st.session_state['file-link-generated'])


# print("/////////////////////", searchedFilename)
# st.session_state["searched_filename"] = searchedFilename

# def handleSearchedFilename():
#     fn = st.session_state["searched_filename"]
#     print(fn)
#     ops.create_steamlit_logs(ops.getCloudwatchInstance(), f"Search Hit {fn}")
#     prefix_filename = ops.get_geos_file_link(st.session_state["searched_filename"])
#     if prefix_filename:
#         st.session_state['prefix_filename'] = prefix_filename

# st.button("Generate File Link", on_click = handleSearchedFilename, key = "file_gen_link")


# st.write("AWS S3 Bucket link")

# if st.session_state['prefix_filename']:
#     st.write("https://damg7245-s3-storage.s3.amazonaws.com/" + st.session_state['prefix_filename'])






