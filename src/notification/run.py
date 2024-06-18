from src.notification.daemons import daemon
from src.notification.api import server

if __name__ == "__main__":
    try:
        daemon.start()
        server.run()
    except KeyboardInterrupt:
        pass
