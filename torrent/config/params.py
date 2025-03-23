from torrent.config.config import Config
import libtorrent as lt

class Params(Config):
    """
    Класс для хранения параметров конфигурации торрента.
    """

    save_path:str
    """Путь для сохранения загруженных файлов."""

    storage_mode:any = lt.storage_mode_t.storage_mode_allocate
    """Режим хранения файлов:
    - 0 (sparse) – выделяет место по мере загрузки (экономия места).
    - 1 (allocate) – сразу резервирует весь объем (ускоряет работу с файлами).
    """
    
    def get(self) -> dict[str]:
        return __dict__