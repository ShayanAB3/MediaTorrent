import libtorrent as lt
import time

# Создаем сессию
ses = lt.session()
ses.listen_on(6881, 6891)  # Порты для P2P

# Добавляем торрент через Magnet-ссылку
magnet_link = "magnet:?xt=urn:btih:9a66fc15327ff520905eb3be695f878b18fee9dd&dn=rutor.info&tr=udp://opentor.net:6969&tr=http://retracker.local/announce"
params = {
    "save_path": "./downloads/",  # Куда сохранять файлы
    "storage_mode": lt.storage_mode_t.storage_mode_sparse,
}
handle = lt.add_magnet_uri(ses, magnet_link, params)

print("Добавлено, ждем метаданных...")
while not handle.has_metadata():
    time.sleep(1)

print("Метаданные получены, загрузка началась!")

# Ждем завершения загрузки
while not handle.is_seed():
    status = handle.status()
    print(f"Скорость: {status.download_rate / 1024:.2f} KB/s, Загружено: {status.progress * 100:.2f}%")
    time.sleep(2)

print("Загрузка завершена!")
