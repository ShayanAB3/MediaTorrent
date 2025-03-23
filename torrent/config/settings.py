

class Settings:
    download_rate_limit = 500000
    """Лимит скачивания (500 KB/s)"""

    upload_rate_limit = 100000
    """Лимит отдачи (100 KB/s)"""

    connections_limit = 200
    """Макс. число соединений"""

    listen_interfaces = "0.0.0.0:6881"
    """Порт для входящих соединений"""

    enable_dht:bool = True
    """Включить DHT (поиск пиров без трекеров)"""

    enable_lsd:bool = True
    """Включить локальное обнаружение пиров"""

    enable_upnp:bool = True
    """Включить UPnP (авто-проброс портов)"""

    enable_natpmp:bool = True
    """Включить NAT-PMP (аналог UPnP)"""

    alert_mask = lt.alert.category_t.all_categories
    """Все уведомления"""

    def get(self) -> dict[str]:
        return __dict__