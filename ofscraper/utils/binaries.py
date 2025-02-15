import pathlib
import logging
import shutil
import os
import tempfile
import platform
import httpx
import ofscraper.constants as constants
from zipfile import ZipFile
from tarfile import TarFile
import stat


from rich.progress import Progress
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
)
from rich.live import Live
from rich.panel import Panel
from rich.console import Group
from rich.table import Column
import arrow
def mp4decrypt_download():
    if platform.system() == 'Windows':
        return mp4_decrypt_windows()
    else:
        return mp4_decrypt_linux()

def ffmpeg_download():
    if platform.system() == 'Windows':
        return ffmpeg_windows()
    else:
        return ffmpeg_linux()   
 
def mp4_decrypt_windows():
 with tempfile.TemporaryDirectory() as t:
        zip_path=pathlib.Path(t,"mp4decrypt.zip")
        with Progress(  TextColumn("{task.description}"),
        BarColumn()) as download:
            with httpx.stream("GET",constants.MP4DECRYPT_WINDOWS,timeout=None) as r:
                    total = int(r.headers['Content-Length'])
                    task1=download.add_task("mp4decrypt download",total=total)
                    num_bytes_downloaded = r.num_bytes_downloaded
                    with open(pathlib.Path(zip_path),"wb") as f:
                        for chunk in r.iter_bytes(chunk_size=1024):
                            f.write(chunk)
                            download.update(task1, advance=r.num_bytes_downloaded - num_bytes_downloaded)
                            num_bytes_downloaded = r.num_bytes_downloaded
            download.remove_task(task1)
        bin_path=pathlib.Path.home() / constants.configPath / "bin"/"mp4decrypt.exe"
        bin_path.parent.mkdir(exist_ok=True,parents=True)
        with ZipFile(zip_path) as zObject:
             zObject.extractall(path=t)
        shutil.move(list(pathlib.Path(t).glob("**/mp4decrypt.exe"))[0],bin_path)
        # st = os.stat(bin_path)
        # os.chmod(bin_path, st.st_mode | stat.S_IEXEC)
        return str(bin_path)

def mp4_decrypt_linux():
    with tempfile.TemporaryDirectory() as t:
        zip_path=pathlib.Path(t,"mp4decrypt.zip")
        with Progress(  TextColumn("{task.description}"),
        BarColumn()) as download:
            with httpx.stream("GET",constants.MP4DECRYPT_LINUX,timeout=None) as r:
                    total = int(r.headers['Content-Length'])
                    task1=download.add_task("mp4decrypt download",total=total)
                    num_bytes_downloaded = r.num_bytes_downloaded
                    with open(pathlib.Path(zip_path),"wb") as f:
                        for chunk in r.iter_bytes(chunk_size=1024):
                            f.write(chunk)
                            download.update(task1, advance=r.num_bytes_downloaded - num_bytes_downloaded)
                            num_bytes_downloaded = r.num_bytes_downloaded
            download.remove_task(task1)
        bin_path=pathlib.Path.home() / constants.configPath / "bin"/"mp4decrypt"
        bin_path.parent.mkdir(exist_ok=True,parents=True)
        with ZipFile(zip_path) as zObject:
             zObject.extractall(path=t)
        shutil.move(list(pathlib.Path(t).glob("**/mp4decrypt"))[0],bin_path)
        st = os.stat(bin_path)
        os.chmod(bin_path, st.st_mode | stat.S_IEXEC)
        return str(bin_path)
      


def ffmpeg_windows():
    with tempfile.TemporaryDirectory() as t:
        zip_path=pathlib.Path(t,"ffmpeg.zip")
        with Progress(  TextColumn("{task.description}"),
        BarColumn()) as download:
            with httpx.stream("GET",constants.FFMPEG_WINDOWS,timeout=None) as r:
                    total = int(r.headers['Content-Length'])
                    task1=download.add_task("ffmpeg download",total=total)
                    num_bytes_downloaded = r.num_bytes_downloaded
                    with open(pathlib.Path(zip_path),"wb") as f:
                        for chunk in r.iter_bytes(chunk_size=1024):
                            f.write(chunk)
                            download.update(task1, advance=r.num_bytes_downloaded - num_bytes_downloaded)
                            num_bytes_downloaded = r.num_bytes_downloaded
            download.remove_task(task1)
        bin_path=pathlib.Path.home() / constants.configPath / "bin"/"ffmpeg.exe"
        bin_path.parent.mkdir(exist_ok=True,parents=True)
        with ZipFile(zip_path) as zObject:
             zObject.extractall(path=t)
        shutil.move(list(pathlib.Path(t).glob("**/ffmpeg.exe"))[0],bin_path)
        # st = os.stat(bin_path)
        # os.chmod(bin_path, st.st_mode | stat.S_IEXEC)
        return str(bin_path)

def ffmpeg_linux():
    with tempfile.TemporaryDirectory() as t:
        zip_path=pathlib.Path(t,"ffmpeg.tar.xz")
        with Progress(  TextColumn("{task.description}"),
        BarColumn()) as download:
            with httpx.stream("GET",constants.FFMPEG_LINUX,timeout=None) as r:
                    total = int(r.headers['Content-Length'])
                    task1=download.add_task("ffmpeg download",total=total)
                    num_bytes_downloaded = r.num_bytes_downloaded
                    with open(pathlib.Path(zip_path),"wb") as f:
                        for chunk in r.iter_bytes(chunk_size=1024):
                            f.write(chunk)
                            download.update(task1, advance=r.num_bytes_downloaded - num_bytes_downloaded)
                            num_bytes_downloaded = r.num_bytes_downloaded
            download.remove_task(task1)
        bin_path=pathlib.Path.home() / constants.configPath / "bin"/"ffmpeg"
        bin_path.parent.mkdir(exist_ok=True,parents=True)
        with TarFile.open(zip_path,mode="r:xz") as zObject:
             zObject.extractall(path=t)
        shutil.move(list(pathlib.Path(t).glob("**/ffmpeg"))[0],bin_path)
        st = os.stat(bin_path)
        os.chmod(bin_path, st.st_mode | stat.S_IEXEC)
        return str(bin_path)
