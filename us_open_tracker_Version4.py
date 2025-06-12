import streamlit as st
import pandas as pd

# Estimated earnings (update these as new results come in)
estimated_earnings = {
    "Ludvig Åberg": 4300000,
    "Rory McIlroy": 1883531,
    "Patrick Cantlay": 1883531,
    "Tony Finau": 928403,
    "Thomas Detry": 928403,
    "Sergio Garcia": 928403,
    "Harris English": 604086,
    "Collin Morikawa": 604086,
    "Xander Schauffele": 316602,
    "Viktor Hovland": 316602,
    "Ben Griffin": 100000,
    "Jon Rahm": 90000,
    "Brooks Koepka": 85000,
    "Sepp Straka": 80000,
    "Joaquin Niemann": 75000,
    "Russell Henley": 70000,
    "Tommy Fleetwood": 65000,
    "Keegan Bradley": 60000,
    "Shane Lowry": 55000,
    "Matt Fitzpatrick": 50000,
    "Justin Rose": 45000,
    "Wyndham Clark": 40000,
    "Jordan Spieth": 35000,
    "Min Woo Lee": 30000,
    "Scottie Scheffler": 25000,
    "Justin Thomas": 20000,
    "Nick Taylor": 15000,
    "Jhonattan Vegas": 10000,
    "Lucas Glover": 10000,
    "Corey Conners": 10000,
    "Brian Harman": 10000,
    "Jason Day": 10000,
    "Carlos Ortiz": 10000,
    "Daniel Berger": 10000,
    "Akshay Bhatia": 10000
}

# Participant data
participants_data = [
    ("Jones, Doug", ["Ludvig Åberg", "Keegan Bradley", "Harris English", "Ben Griffin"]),
    ("Soehner, Peter", ["Jon Rahm", "Ludvig Åberg", "Tommy Fleetwood", "Viktor Hovland"]),
    ("Eddie Dauphin", ["Ludvig Åberg", "Ben Griffin", "Joaquin Niemann", "Matt Fitzpatrick"]),
    ("Manderson, Connor", ["Russell Henley", "Jon Rahm", "Lucas Glover", "Ludvig Åberg"]),
    ("Rocci, Peter", ["Ludvig Åberg", "Min Woo Lee", "Jordan Spieth", "Jon Rahm"]),
    ("Prichard Scott", ["Patrick Cantlay", "Bryson DeChambeau", "Scottie Scheffler", "Tony Finau"]),
    ("Moore, Joe", ["Patrick Cantlay", "Ben Griffin", "Viktor Hovland", "Brooks Koepka"]),
    ("Cahill, Patrick", ["Viktor Hovland", "Joaquin Niemann", "Patrick Cantlay", "Sepp Straka"]),
    ("Buckley, Andrew", ["Ben Griffin", "Tommy Fleetwood", "Sepp Straka", "Patrick Cantlay"]),
    ("Roberts, Travis", ["Sepp Straka", "Tommy Fleetwood", "Jon Rahm", "Rory McIlroy"]),
    # Add more participants here as needed...
]

# Calculate leaderboard
leaderboard = []
for name, picks in participants_data:
    total = sum(estimated_earnings.get(player, 0) for player in picks)
    leaderboard.append((name, total))

leaderboard_df = pd.DataFrame(leaderboard, columns=["Participant", "Total Earnings"])
leaderboard_df.sort_values("Total Earnings", ascending=False, inplace=True)

# Streamlit App
st.title("🏌️ US Open Office Pool Leaderboard")
st.markdown("Live standings based on estimated payouts. Update the earnings dictionary as results change.")

st.dataframe(leaderboard_df.reset_index(drop=True), use_container_width=True)