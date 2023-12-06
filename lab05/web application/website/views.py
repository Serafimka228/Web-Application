from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import AlbumRating
from . import db
from sqlalchemy import func

from .spotifyAPIfunctions import (
    get_token,
    search_artist,
    search_track,
    search_album,
    get_album_by_id,
)

views = Blueprint("views", __name__)


@views.route("/main", methods=["GET", "POST"])
@login_required
def main_page():
    token = get_token()
    if request.method == "POST":
        search_str = request.form.get("search_line")
        if search_str:
            album_id = search_album(token, search_str, 1)[0]["id"]
            return redirect(f"/album/{album_id}")
    return render_template("MainPage.html", user=current_user)


@views.route("/album/<string:id>", methods=["GET", "POST"])
@login_required
def album_page(id):
    token = get_token()
    if request.method == "POST":
        search_str = request.form.get("search_line")
        if not search_str:
            pass
        album_id = search_album(token, search_str, 1)[0]["id"]
        return redirect(f"/album/{album_id}")

    album = get_album_by_id(token, id)
    if album == None:
        flash("No albums were found", "error")
        return render_template("AlbumPage.html")

    album_avg_rating = -1
    album_user_rating = -1

    album_rating = AlbumRating.query.filter_by(
        user_id=current_user.id, album_id=id
    ).first()
    if album_rating != None:
        print(album_rating)
        album_user_rating = album_rating.rating
        print(album_user_rating)
        album_avg_rating = (
            AlbumRating.query(func.avg(AlbumRating.rating))
            .filter_by(album_id=id)
            .scalar()
        )
        print(album_avg_rating)

    album_name = album["name"]
    album_release_date = album["release_date"]
    artist_name = album["artists"]
    tracks = get_list_of_tracks(album)
    album_total_tracks = album["total_tracks"]
    album_image_url = album["images"][0]["url"]

    return render_template(
        "AlbumPage.html",
        current_page_id=id,
        album_name=album_name,
        artist_name=artist_name,
        album_release_date=album_release_date,
        album_total_tracks=album_total_tracks,
        album_image_url=album_image_url,
        tracks=tracks,
        user=current_user,
        album_avg_rating=album_avg_rating,
        album_user_rating=album_user_rating,
    )


@views.route("/")
def index():
    return render_template("Main.html")


def get_list_of_tracks(album):
    album_tracks = album["tracks"]
    tracks = []
    avg_rating = -1
    user_rating = -1
    for i, track in enumerate(album_tracks):
        track_info = {}
        track_info["index_in_list"] = str(i + 1) + "."
        track_info["name_in_list"] = track
        track_info["avg_rating_in_list"] = avg_rating
        track_info["your_rating_in_list"] = user_rating
        tracks.append(track_info)
    return tracks
