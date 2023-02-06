import streamlit as st

st.title('Big Data Assignment 1')
st.title('NEXRAD')
st.subheader('Search by Fields')
st.date_input('Date')

state = ("NY - New York", "CA - California", "IL - Illionis", "TX - Texas", "AZ - Arizona", "PA - Pennsylvania",
          "AL - Alabama", "AK - Alaska", "AR - Arkansas", "CL - Colorado", "CT - Connecticut", "DE - Delaware",
          "FL - Florida", "GA - Georgia", "HI - Hawaii", "ID - Idaho", "IN - Indiana", "IA - IOWA", "KS - Kansas",
          "KY - Kentucky", "LA - Louisiana", "ME - Maine", "MD - Maryland", "MA - Massachusetts", "MI - Michigan",
          "MN - Minnesota", "MS - Mississippi", "MO - Missouri", "MT - Montana", "NE - Nebraska", "NV - Nevada", 
          "NH - New Hampshire", "NJ - New Jersey", "NM - New Mexico", "NC - North Carolina", "ND - North Dakota",
          "OH - Ohio", "OK - Oklahoma", "OR - Oregon", "RI - Rhode Island", "SC - South Carolina", "SD - South Dakota",
          "TN - Tennessee", "UT - Utah", "VT - Vermont", "VA - Virginia", "WA - Washington", "WV - West Virginia", "WI - Wisconsin", "WY - Wyoming")

stations = ("TJUA", "KCBW", "KGYX", "KCXX", "KBOX", "KENX", "KBGM", "KBUF", )

state_city_sites = {
    "PR - Puerto Rico": ["San Juan"],
    "ME - Maine": ["Houlton", "Gray/Portland"],
    "VT - Vermont": ["Burlington"],
    "MA - Massachusetts": ["Boston"],
    "NY - New York": ["Albany", "Binghamton", "Buffalo", "Montague", "New York City"],
    "DE - Delaware": ["Dover AFB"],
    "PA - Pennsylvania": ["Philadelphia", "Pittsburgh", "State College"],
    "WV - West Virginia": ["Charleston"],
    "VA - Virginia": ["Norfolk", "Roanoke", "Sterling"],
    "NC - North Carolina": ["Morehead City", "Raleigh", "Wilmington"],
    "SC - South Carolina": ["Charleston", "Columbia", "Greer"],
    "GA - Georgia": ["Atlanta", "Moddy AFB", "Robins AFB"],
    "FL - Florida": ["Eglin AFB", "Jacksonville", "Key West", "Melbourne", "Miami", "Tallahassee", "Tampa"],
    "AL - Alabama": ["Brimingham", "Fort Rucker", "Huntsville", "Maxwell AFB", "Mobile"],
    "MS - Mississippi": ["Brandon", "Columbus AFB"],
    "TN - Tennessee": ["Knoxville", "Memphis", "Nashville"],
    "KY - Kentucky": ["Fort Campbell", "Jackson", "Louisville", "Paducah"],
    "OH - Ohio": ["Wilmington", "Cleveland"],
    "MI - Michigan": ["Detroit", "Gaylord", "Grand Rapids", "Marquette"],
    "IN - Indiana": ["Owensville", "Indianapolis", "North Webster"],
    "IL - Illinois": ["Chicago", "Lincoln"],
    "WI - Wisconsin": ["Green Bay", "La Crosse", "Milwaukee"],
    "MN - Minnesota": ["Dublin", "Minneapolis"],
    "IA - IOWA": ["Davenport", "Des Moines"],
    "MO - Missouri": ["Kansas City", "Springfield", "St. Louis"],
    "AR - Arkansas": ["Fort Smith", "Little Rock"],
    "LA - Louisiana": ["Fort Polk", "Lake Charles", "New Orleans", "Shreveport"],
    "TX - Texas": ["Amarillo", "Austin", "Brownsville", "Corpus Christi", "Dallas/Ft. Worth", "Dyess AFB", "El Paso",
                   "Fort Hood", "Houston", "Laughlin AFB", "Lubbock", "Midland", "San Angelo"],
    "OK - Oklahoma": ["Frederick", "Oklahoma City", "Norman", "Tulsa", "Vance AFB"],
    "KS - Kansas": ["Dodge City", "Goodland", "Topeka", "Wichita"],
    "NE - Nebraska": ["North Platte", "Omaha"],
    "SD - South Dakota": ["Aberdeen", "Rapid City", "Sioux Falls"],
    "ND - North Dakota": ["Bismarck", "Grand Forks", "Minot AFB"],
    "MT - Montana": ["Billings", "Glasgow", "Great Falls", "Missoula"],
    "WY - Wyoming": ["Cheyenne", "Riverton"],
    "CO - Colorado": ["Denver", "Grand Junction", "Pueblo"],
    "NM - New Mexico": ["Albuquerque", "Canon AFB", "Holloman AFB"],
    "AZ - Arizona": ["Flagstaff", "Phoenix", "Tucson", "Yuma"],
    "UT - Utah": ["Cedar City", "Salt Lake City"],
    "ID - Idaho": ["Boise", "Pocatello"],
    "NV - Nevada": ["Elko", "Las Vegas", "Reno"],
    "CA - California": ["Beale AFB", "Edwards AFB", "Eureka", "Los Angeles", "Sacramento", "San Diego", "San Francisco",
                        "San Joaquin Valley", "Santa Ana Mountains", "Vandenberg AFB"],
    "HI - Hawaii": ["Kauai", "Kohala", "Molokai", "South Shore"],
    "OR - Oregon": ["Medford", "Pendleton", "Portland"],
    "WA - Washington": ["Langley Hill", "Seattle", "Spokane"],
    "AK - Alaska": ["Bethel", "Fairbanks", "Kenai", "King Salmon", "Middleton Island", "Nome", "Sitka"],
    "GU - Guam": ["Andersen AFB"],
    "NA": ["Lajes Field, Azores"],
    "SK": ["Kunsan Air Base, South Korea", "Camp Humphreys, South Korea"],
    "JP": ["Kadena Air Base, Japan"]
}


selectedState = st.selectbox("State", tuple(state_city_sites))

selectedCity = st.selectbox("City", tuple(state_city_sites[selectedState]))

st.button('Search')

st.selectbox("Files", ('file01', 'file02'))

st.button("Download")

st.write("AWS S3 Bucket File Link")

st.subheader("Search By File Name")

st.text_input("Filename")

st.button("Generate")

st.write("AWS S3 Bucket link")
# st.

# st.selectbox("City", )