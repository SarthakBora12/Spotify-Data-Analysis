import requests
import pandas as pd
import random
import time
from sqlalchemy import create_engine
import sqlite3

# Spotify API credentials
client_id = 'YOUR-CLIENT-ID-HERE'
client_secret = 'YOUR-CLIENT-SECRET-HERE

# === Step 1: Authenticate ===
auth_url = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
})
access_token = auth_response.json()['access_token']
headers = {'Authorization': f'Bearer {access_token}'}

# === Config ===
artist_names = [
    "The Weeknd", "Dua Lipa", "Drake", "Taylor Swift", "Billie Eilish",
    "Ed Sheeran", "Post Malone", "Bad Bunny", "Olivia Rodrigo", "Doja Cat",
    "BTS", "BLACKPINK", "Shakira", "Imagine Dragons", "Selena Gomez",
    "Harry Styles", "Kanye West", "Justin Bieber", "SZA", "Arijit Singh"
]
countries = [
    "USA", "UK", "Canada", "Germany", "India", "Japan", "Australia",
    "Brazil", "France", "Mexico", "South Korea", "Spain", "Netherlands",
    "Italy", "South Africa"
]
subscription_types = ["Free", "Premium"]
age_groups = ["13-17", "18-24", "25-34", "35-44", "45+"]
year_choices = list(range(2019, 2025))

# === Helper Functions ===
def get_artist_id(name):
    r = requests.get("https://api.spotify.com/v1/search", headers=headers, params={"q": name, "type": "artist", "limit": 1})
    items = r.json().get("artists", {}).get("items", [])
    return (items[0]["id"], items[0]["genres"]) if items else (None, [])

def get_albums(artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    r = requests.get(url, headers=headers, params={"market": "US", "limit": 10})
    return list({album["id"]: album for album in r.json().get("items", [])}.values())  # unique albums

def get_tracks(album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    r = requests.get(url, headers=headers)
    return r.json().get("items", [])

def get_audio_features(track_ids):
    if not track_ids:
        return {}
    features = {}
    for i in range(0, len(track_ids), 100):
        batch = track_ids[i:i+100]
        url = "https://api.spotify.com/v1/audio-features"
        r = requests.get(url, headers=headers, params={"ids": ",".join(batch)})
        for f in r.json().get("audio_features", []):
            if f and f.get("id"):
                features[f["id"]] = f
        time.sleep(0.1)
    return features

# === Ingest Loop ===
all_data = []

for artist in artist_names:
    artist_id, genres = get_artist_id(artist)
    if not artist_id:
        continue
    albums = get_albums(artist_id)
    for album in albums:
        tracks = get_tracks(album["id"])
        track_ids = [t["id"] for t in tracks if t.get("id")]
        features = get_audio_features(track_ids)
        for t in tracks:
            f = features.get(t["id"], {})
            streams = random.randint(50000, 1000000)
            revenue = round(streams * random.uniform(0.03, 0.07), 2)
            all_data.append({
                "Artist": artist,
                "Category": genres[0] if genres else "Pop",
                "Streams": streams,
                "Revenue (USD)": revenue,
                "Country": random.choice(countries),
                "Year": random.choice(year_choices),
                "Most Popular Song": t.get("name", ""),
                "Subscription Type": random.choice(subscription_types),
                "Age Group": random.choice(age_groups),
                "Danceability": f.get("danceability"),
                "Energy": f.get("energy"),
                "Tempo": f.get("tempo"),
                "Valence": f.get("valence")
            })
        time.sleep(0.2)  # avoid rate limits

# === Save to SQLite ===
df = pd.DataFrame(all_data)
conn = sqlite3.connect("spotify_extended.db")
df.to_sql("spotify_streaming", conn, if_exists="replace", index=False)
conn.close()

print("Ingested and saved extended Spotify data.")


# === Save to CSV ===
conn = sqlite3.connect("spotify_extended.db")
df = pd.read_sql_query("SELECT * FROM spotify_streaming", conn)
df.to_csv("spotify_streaming_data.csv", index=False)
conn.close()