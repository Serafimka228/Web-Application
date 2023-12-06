from dotenv import load_dotenv
import os, sqlite3
import base64
from requests import post, get
import json

dotenv_path = "env\.env"
load_dotenv(dotenv_path)

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode(encoding="utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    result = json.loads(result.content)
    token = result["access_token"]
    return token


def get_authorization_header(token):
    return {"Authorization": "Bearer " + token}


def search_artist(token, artist_name, limit):
    url = "https://api.spotify.com/v1/search"
    headers = get_authorization_header(token)
    query = f"q={artist_name}&type=artist&limit={limit}"  # limit - number of artists to search
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    result = json.loads(result.content)["artists"]["items"]
    if len(result) == 0:
        return None
    return result


def search_track(token, track_name, limit):
    url = "https://api.spotify.com/v1/search"
    headers = get_authorization_header(token)
    query = f"q={track_name}&type=track&limit={limit}"  # limit - number of artists to search
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    result = json.loads(result.content)["tracks"]["items"]
    if len(result) == 0:
        return None
    return result


def search_album(token, album_name, limit):
    url = "https://api.spotify.com/v1/search"
    headers = get_authorization_header(token)
    query = f"q={album_name}&type=album&limit={limit}"  # limit - number of artists to search
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    result = json.loads(result.content)["albums"]["items"]
    if len(result) == 0:
        return None
    return result


def get_album_by_id(token, album_id):
    url = "https://api.spotify.com/v1/albums/"
    headers = get_authorization_header(token)
    # query = f"q={album_name_name}&type=album&limit={limit}"  # limit - number of artists to search
    query_url = url + album_id
    response = get(query_url, headers=headers)
    if response.status_code == 200:
        result = json.loads(response.content)
        name = result["name"]
        artists = result["artists"]
        artist_name = ""
        for artist in artists:
            artist_name += artist["name"]
            artist_name += " "
        total_tracks = result["total_tracks"]
        release_date = result["release_date"]
        images = result["images"]

        tracks = []
        for track in result["tracks"]["items"]:
            tracks.append(track["name"])
        album_info = {
            "name": name,
            "artists": artist_name,
            "total_tracks": total_tracks,
            "tracks": tracks,
            "release_date": release_date,
            "images": images,
        }
        return album_info
    return None


def get_songs_by_artist_id(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=BY"
    headers = get_authorization_header(token)
    result = get(url, headers=headers)
    result = json.loads(result.content)["tracks"]
    return result


# token = get_token()
# album = search_album(token, "The Queen is dead", 1)
# print(album[0]["name"])
# album_id = album[0]["id"]
# print(album_id)
# al = get_album_by_id(token, album_id)
# print(al["name"])
# print(al["artists"])
# tracks = al["tracks"]
# for track in tracks:
#     print(track)


# artists = search_artist(token, "The ", 5)
# for artist in artists:
#    print(artist["name"])
# tracks = search_track(token, "The ", 5)
# for track in tracks:
#    print(track["id"])
#    print(track["name"])
# artist_id = search_artist(token, "imagine")["id"]
# print(type(artist_id))
# songs = get_songs_by_artist_id(token, artist_id)
# for idx, song in enumerate(songs):
#    print(f"{idx + 1}: {song['name']}")
