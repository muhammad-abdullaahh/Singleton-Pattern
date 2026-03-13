# 🔒 Singleton Design Pattern — Python

A clean Python implementation of the **Singleton Design Pattern** across three real-world tasks, all using the `__new__` method approach.

---

## 📌 What is the Singleton Pattern?

The **Singleton Pattern** is a creational design pattern that ensures a class has **only one instance** throughout the entire program, and provides a global point of access to it.

> No matter how many times you call the constructor, you always get back the same object.

---

## 🧠 How It Works in Python

All three tasks use the same core mechanism — overriding `__new__`:

```
First call  → _instance is None → creates the object → stores it in _instance
Second call → _instance already exists → returns the same object
```

The check `obj1 is obj2` returns `True` in every task, proving only one instance ever exists.

---

## 🗂️ Tasks Overview

| Task | Class | Real-World Use Case |
|---|---|---|
| `task1.py` | `Printer` | Shared printer resource |
| `task2.py` | `SessionManager` | Centralized user session store |
| `task3.py` | `Logger` | Single file logger across the app |

---

## 🌍 Real-World Applications

The Singleton pattern is used everywhere in production systems:

- **Database connection pools** — one shared connection manager
- **Config managers** — one object holds all app settings
- **Logging systems** — all modules write to one logger
- **Thread pools** — one scheduler manages all workers
- **Cache managers** — one shared in-memory store

---

## 🧠 Key OOP Concepts Used

- **Encapsulation** — instance creation logic is hidden inside the class
- **Single Responsibility** — each class manages exactly one shared resource
- **Controlled Access** — `__new__` acts as a gatekeeper for instantiation

---

## 🐍 Requirements

- Python 3.x
- No external libraries needed

---

## 👤 Author

**Muhammad Abdullah**  
