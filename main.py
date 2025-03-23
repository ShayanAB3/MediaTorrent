from parsers.rutor.search import RutorSearch
import threading
from torrent.torrent import Torrent
from torrent.config.params import Params

rutor_search = RutorSearch("Назад в будущее")
rutor_search.start()
link_magnet = rutor_search.results[0]["link_magnet"]

params = Params()
params.save_path = "./downloads"

torrent = Torrent()
handle = torrent.add_torrent_magnet(link_magnet,params)

# Запускаем мониторинг в отдельном потоке
monitor_thread = threading.Thread(target=torrent.monitor_progress(), args=(handle,))
monitor_thread.start()
