import streamlit as st
import importlib.util
import os

current_directory = os.getcwd()

module_directory = os.path.abspath(os.path.join(current_directory, 'src', 'data'))
module_path = os.path.join(module_directory, 'sqlite_main.py')
ops_path = os.path.join(module_directory, 'backend_ops.py')

spec = importlib.util.spec_from_file_location("sqlite_main", module_path)
spec_ops = importlib.util.spec_from_file_location("backend_ops", ops_path)
db_methods = importlib.util.module_from_spec(spec)
ops = importlib.util.module_from_spec(spec_ops)
spec.loader.exec_module(db_methods)
spec_ops.loader.exec_module(ops)

st.title('NEXRAD')
st.subheader('Search by Fields')


if 'search_btn_clicked' not in st.session_state:
    st.session_state['search_btn_clicked'] = False
if 'search_generate_link' not in st.session_state:
    st.session_state['search_generate_link'] = False
if 'nexrad_prefix_filename' not in st.session_state:
    st.session_state['nexrad_prefix_filename'] = False

year, month, day = st.columns(3)

nexrad_year_list = db_methods.nexrad_get_year()
with year:
    selectedYear = st.selectbox('Year', nexrad_year_list)
    # st.session_state['selectedYear'] = selectedYear

nexrad_month_list = db_methods.nexrad_get_month(selectedYear)
with month:
    selectedMonth = st.selectbox('Month', nexrad_month_list)
    if selectedMonth < 10:
        selectedMonth = "0" + str(selectedMonth)
    # st.session_state['selectedMonth'] = selectedMonth

nexrad_day_list = db_methods.nexrad_get_day(selectedYear, selectedMonth)
with day:
    selectedDay = st.selectbox('Day', nexrad_day_list)
    if selectedDay < 10:
        selectedDay = "0" + str(selectedDay)
    # st.session_state['selectedDay'] = selectedDay

nexrad_sites_list = db_methods.nexrad_get_sites(
    selectedYear,
    selectedMonth,
    selectedDay
)

# st.session_state['selectedSiteList'] = nexrad_sites_list
selectedSite = st.selectbox('Site', nexrad_sites_list)


def handleSearch():
    st.session_state['search_btn_clicked'] = True

def handleSearchGenLink():
    st.session_state['search_generate_link'] = True

st.button('Search', on_click = handleSearch)

selectedFile = ""

if st.session_state['search_btn_clicked']:

    selectedFile = st.selectbox("Files", ops.nexrad_query_files(selectedYear, selectedMonth, selectedDay, selectedSite))

    st.write(selectedFile)

    st.button("Generate Link", on_click = handleSearchGenLink, key = "gen_link")  

if st.session_state['search_generate_link']:

    ops.copyFileFromNexradToS3(selectedFile)

    st.write("AWS link")

    st.write("https://damg7245-s3-storage.s3.amazonaws.com/" + selectedFile)

#    Search By File Name


st.subheader("Search By File Name")

searchedFilename = st.text_input("Filename")

def handleSearchedFilename():
    prefix_filename = ops.get_nexrad_file_link(searchedFilename)
    if prefix_filename:
        st.session_state['nexrad_prefix_filename'] = prefix_filename

st.button("Generate Link", on_click = handleSearchedFilename, key = "search_gen_link")

st.write("AWS S3 Bucket link")

if st.session_state['nexrad_prefix_filename']:
    st.write("https://damg7245-s3-storage.s3.amazonaws.com/" + st.session_state['nexrad_prefix_filename'])
