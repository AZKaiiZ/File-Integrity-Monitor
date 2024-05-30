import os
import syslog
import getpass
from pyinotify import WatchManager, Notifier, ProcessEvent, IN_MODIFY, IN_CREATE, IN_DELETE # type: ignore
from hash_utils import take_file_hash

MASK = IN_MODIFY | IN_CREATE | IN_DELETE

def check_file_integrity(directory):
    """
    Vérifie l'intégrité des fichiers en surveillant les modifications avec inotify.
    
    Args:
        directory (str): Le répertoire à surveiller.
    """
    class EventHandler(ProcessEvent):
        def process_IN_MODIFY(self, event):
            file_path = event.pathname
            current_hash = take_file_hash(file_path)
            current_user = getpass.getuser()  # Utilisation de getuser() pour obtenir le nom de l'utilisateur actuel
            syslog.syslog(syslog.LOG_ALERT, f"Le fichier {file_path} a été modifié par le processus {os.getpid()} de l'utilisateur {current_user}. Nouveau hash: {current_hash}")
            
        def process_IN_CREATE(self, event):
            file_path = event.pathname
            current_user = getpass.getuser()  # Utilisation de getuser() pour obtenir le nom de l'utilisateur actuel
            syslog.syslog(syslog.LOG_ALERT, f"Un nouveau fichier {file_path} a été créé par le processus {os.getpid()} de l'utilisateur {current_user}")

        def process_IN_DELETE(self, event):
            file_path = event.pathname
            current_user = getpass.getuser()  # Utilisation de getuser() pour obtenir le nom de l'utilisateur actuel
            syslog.syslog(syslog.LOG_ALERT, f"Le fichier {file_path} a été supprimé par le processus {os.getpid()} de l'utilisateur {current_user}")
                
    wm = WatchManager()
    handler = EventHandler()
    notifier = Notifier(wm, handler)
    wdd = wm.add_watch(directory, MASK, rec=True)

    notifier.loop()
