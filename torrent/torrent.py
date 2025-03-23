import libtorrent as lt
import time
from torrent.config.params import Params

class Torrent:
    ses = lt.session()
    def __init__(self,port_listen_on: tuple[int] = (6881, 6891)):
        self.ses.listen_on(*port_listen_on)  # Настройка диапазона портов

    def add_torrent(self,path:str,params:Params ) -> lt.torrent_handle:
        info = lt.torrent_info(path)
        torrent_params = {'ti': info} | params.get()
        h = self.ses.add_torrent(torrent_params)
        print(f"Добавлен торрент: {h.name()}")
        return h
    
    def add_torrent_magnet(self,link:str,params:Params) -> lt.torrent_handle:
        magnet_params = lt.parse_magnet_uri(link)
        magnet_params.save_path = params.save_path
        magnet_params.storage_mode = params.storage_mode
        h = self.ses.add_torrent(magnet_params)
        print(f"Добавлен торрент: {h .name()}")
        return h

    def monitor_progress(handle: lt.torrent_handle):
        while not handle.is_seed():
            s = handle.status()
            print(f"Прогресс: {s.progress * 100:.2f}%,\nСкорость: {s.download_rate / 1024:.2f} KB/s")
            time.sleep(2)
        print("Загрузка завершена!")