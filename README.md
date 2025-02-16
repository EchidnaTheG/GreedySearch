# GreedySearch

## 📌 Introduction
GreedySearch is a command-line file explorer that allows users to navigate directories, search for files, and perform basic file operations—all from the terminal.

This project is designed to provide a lightweight, fast, and efficient way to browse files without using a GUI.

## ⚡ Features
- Navigate directories (`cd <dir>`, `..`)
- List directory contents (`ls`)
- Search for files (`find <filename>`)
- Open files (`open <filename>`) *(Future Feature)*
- File operations (`rm`, `mv`, `cp`) *(Future Feature)*

## 📥 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/GreedySearch.git
cd GreedySearch
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Explorer
```bash
python GreedSearch.py
```

## 🛠️ Usage Guide

### 📂 Navigating Directories
| Command     | Description                    |
|------------|--------------------------------|
| `ls`       | List files in current directory|
| `cd <dir>` | Change to a specific directory |
| `..`       | Go up one directory            |

### 🔎 Searching for Files
| Command           | Description                                    |
|------------------|------------------------------------------------|
| `find <filename>`| Search for a file in current directory (recursive)|

### 📄 File Operations (Planned)
| Command           | Description                      |
|------------------|----------------------------------|
| `open <file>`    | Open file with default program   |
| `rm <file>`      | Delete a file (with confirmation)|
| `mv <src> <dst>` | Move/rename a file              |
| `cp <src> <dst>` | Copy a file                     |

## 📌 Development Plan

### ✅ Phase 1: Core Features
- [x] Implement `ls`, `cd`, `..` for directory navigation
- [x] Basic error handling for invalid directories

### 🚀 Phase 2: Searching & File Management
- [ ] Implement `find <filename>` for file searching
- [ ] Implement `open <filename>` to open files

### 🛠️ Phase 3: File Operations
- [ ] Implement `rm <file>` with confirmation
- [ ] Implement `mv <src> <dst>` for moving files
- [ ] Implement `cp <src> <dst>` for copying files

### 🌟 Phase 4: Enhancements & Optimizations
- [ ] Add better output formatting
- [ ] Support wildcard searches (`find *.txt`)
- [ ] Improve error handling and user prompts

## 🖥️ Example Session
```bash
INITIALIZING FILE EXPLORER
COMMANDS!
cd -> change into a dir
.. -> change into previous dir
INIT AT /home/user/GreedySearch
['README.md', 'GreedSearch.py', 'searchlogic.py']

TYPE A COMMAND: cd projects
Now at /home/user/GreedySearch/projects
['project1', 'project2']

TYPE A COMMAND: ..
Now at /home/user/GreedySearch
['README.md', 'GreedSearch.py', 'searchlogic.py']
```

## 🤝 Contributing
Feel free to contribute by submitting issues or pull requests.