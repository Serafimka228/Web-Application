from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    photo = db.Column(db.String(50), unique=True)

    album_ratings = db.relationship("AlbumRating")
    song_ratings = db.relationship("SongRating")


class AlbumRating(db.Model):
    __tablename__ = "album_rating"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    album_id = db.Column(db.String(500), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class SongRating(db.Model):
    __tablename__ = "song_rating"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    song_id = db.Column(db.String(500), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
