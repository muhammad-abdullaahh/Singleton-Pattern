class SessionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating SessionManager instance...")
            cls._instance = super(SessionManager, cls).__new__(cls)
            cls._instance.sessions = {}
        return cls._instance

    def create_session(self, user_id):
        self.sessions[user_id] = "Active"
        print(f"Session created for user {user_id}")

    def get_sessions(self):
        return self.sessions

session1 = SessionManager()
session2 = SessionManager()

session1.create_session("user123")

print(session2.get_sessions())  
print(session1 is session2)     

