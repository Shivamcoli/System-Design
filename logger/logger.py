import threading
import queue
import datetime
from abc import ABC, abstractmethod
from enum import IntEnum

# 1. Define Log Levels
class LogLevel(IntEnum):
    DEBUG = 0
    INFO = 1
    WARN = 2
    ERROR = 3
    FATAL = 4

# 2. Data Transfer Object
class LogMessage:
    def __init__(self, level, message):
        self.level = level
        self.message = message
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. Formatter Strategy
class LogFormatter(ABC):
    @abstractmethod
    def format(self, log_msg): pass

class DefaultFormatter(LogFormatter):
    def format(self, log_msg):
        return f"[{log_msg.timestamp}] [{log_msg.level.name}] - {log_msg.message}"

# 4. Appender (Destinations)
class LogAppender(ABC):
    @abstractmethod
    def append(self, formatted_content): pass

class ConsoleAppender(LogAppender):
    def append(self, formatted_content):
        print(f"[Console] {formatted_content}")

class FileAppender(LogAppender):
    def __init__(self, file_path):
        self.file_path = file_path

    def append(self, formatted_content):
        with open(self.file_path, "a") as f:
            f.write(formatted_content + "\n")

# 5. The Core Logger (Singleton & Async)
class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
                cls._instance._init_logger()
        return cls._instance

    def _init_logger(self):
        self.min_level = LogLevel.INFO
        self.appenders = []
        self.formatter = DefaultFormatter()
        self.log_queue = queue.Queue()
        
        # Start background worker thread for Asynchronous Logging
        self.worker_thread = threading.Thread(target=self._process_queue, daemon=True)
        self.worker_thread.start()

    def set_config(self, level, appenders, formatter=None):
        self.min_level = level
        self.appenders = appenders
        if formatter:
            self.formatter = formatter

    def _process_queue(self):
        while True:
            log_msg = self.log_queue.get()
            formatted = self.formatter.format(log_msg)
            for appender in self.appenders:
                appender.append(formatted)
            self.log_queue.task_done()

    def _log(self, level, message):
        if level >= self.min_level:
            self.log_queue.put(LogMessage(level, message))

    # API for developers
    def debug(self, msg): self._log(LogLevel.DEBUG, msg)
    def info(self, msg):  self._log(LogLevel.INFO, msg)
    def warn(self, msg):  self._log(LogLevel.WARN, msg)
    def error(self, msg): self._log(LogLevel.ERROR, msg)
    def fatal(self, msg): self._log(LogLevel.FATAL, msg)

# --- 6. Usage (Main Application) ---
if __name__ == "__main__":
    logger = Logger()
    
    # Configure: Level is INFO, output to both Console and File
    config_appenders = [ConsoleAppender(), FileAppender("app.log")]
    logger.set_config(LogLevel.INFO, config_appenders)

    logger.info("System initialized.")
    logger.debug("This won't show up (below INFO level).")
    logger.error("Database connection failed!")
    
    # Ensure queue is processed before script ends
    logger.log_queue.join()