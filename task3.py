class Logger:
    _instance = None

    def __new__(cls, logfile="app.log"):
        if cls._instance is None:
            print("Creating Logger instance...")
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logfile = logfile
        return cls._instance

    def log(self, message):
        with open(self.logfile, "a") as f:
            f.write(message + "\n")
        print(f"Logged: {message}")

logger1 = Logger()
logger2 = Logger()

logger1.log("Application started")
logger2.log("Another log entry")
print(logger1 is logger2)  
