import os

from pathlib import Path
from shutil import rmtree
from sys import platform
from uuid import uuid1
import requests
import re

__all__ = ['PathHolder', 'urlretrieve']


def urlretrieve(url, file):
    response = requests.get(url, stream=True)
    with open(file, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=8192):
            fd.write(chunk)


def clean(path) -> None:
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                rmtree(file_path)

        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def create_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def check_ffmpeg() -> bool:
    from shutil import which
    return which('ffmpeg') is not None


def check_env() -> bool:
    from os import environ
    return "SPOTIPY_CLIENT_ID" in environ and "SPOTIPY_CLIENT_SECRET" in environ


def check_file(path: Path) -> bool:
    return path.is_file()


def safe_path_string(string: str) -> str:
    keep_characters = " !£$%^&()_-+=,.;'@#~[]{}"
    new_string = ""

    for c in string:
        if c.isalnum() or c in keep_characters:
            new_string = new_string + c
        else:
            new_string = new_string + "_"

    return re.sub(r'\.+$', '', new_string.rstrip()).encode('utf8').decode('utf8')


class PathHolder:
    """The PathHolder holds precomputed paths relating to the currently running program."""

    def __init__(self, data_path: str = None, downloads_path: str = None):
        # Setup home/data path
        if data_path is None:
            home = Path.home()

            if platform == "win32":
                self.data_path = home / "AppData/Roaming/Savify"

            elif platform == "linux":
                self.data_path = home / ".local/share/Savify"

            elif platform == "darwin":
                self.data_path = home / "Library/Application Support/Savify"

        else:
            self.data_path = Path(data_path)

        # Setup temp path
        self.temp_path = self.data_path / "temp"
        create_dir(self.temp_path)

        # Setup downloads path
        if downloads_path is None:
            self.downloads_path = self.data_path / "downloads"
        else:
            self.downloads_path = Path(downloads_path)

        create_dir(self.downloads_path)

    def get_download_dir(self) -> Path:
        return self.downloads_path

    def get_temp_dir(self) -> Path:
        return self.temp_path

    def download_file(self, url: str, extension: str = None) -> Path:
        file_path = self.get_temp_dir() / str(uuid1())
        if extension is not None:
            file_path = file_path.with_suffix(f'.{extension}')

        urlretrieve(url, str(file_path))
        return file_path
