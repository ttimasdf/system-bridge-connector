# generated by datamodel-codegen:
#   filename:  media_play.json

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class MediaPlay(BaseModel):
    """
    Media Play
    """

    album: Optional[str] = None
    artist: Optional[str] = None
    autoplay: Optional[bool] = False
    cover: Optional[str] = None
    title: Optional[str] = None
    url: str
    volume: Optional[float] = 40
