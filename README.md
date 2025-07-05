# 🔢 Advanced Set Operations Tool

> A comprehensive Python application for performing mathematical set operations with enhanced features and professional interface.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.0-orange.svg)](https://github.com/OguzhanBerkeOzdil/SET-Theory)

## 🎓 Academic Project Background

### Original Coursework (2022-2023)

**Course:** Formal Languages and Compilers  
**Institution:** AGH University of Science and Technology, Krakow, Poland  
**Faculty:** EAIIB (Faculty of Electrical Engineering, Automatics, Computer Science and Biomedical Engineering)  
**Program:** Computer Science Bachelor Degree  

**Original Development Team:**

- **Oğuzhan Berke Özdil** - Lead Developer, Computer Science Student
- **Berkay Doruk** - Lead Developer, Computer Science Student

The initial version provided basic set operations with a simple command-line interface as a coursework assignment.

### Professional Enhancement 2.0 (2025)

**Enhanced by:** Oğuzhan Berke Özdil  
**Contact:** [LinkedIn Profile](https://www.linkedin.com/in/oguzhanberkeozdil/)  
**Scope:** Complete professional redesign with modern development practices

**Major Improvements:**

- 🏗️ Object-oriented architecture with `SetOperations` class
- 🎨 Professional user interface with Unicode symbols and emojis
- 📊 Extended mathematical operations and visualizations
- 🧪 Comprehensive testing suite with validation
- ⚡ Advanced error handling and input validation
- 📜 Operation history tracking with timestamps
- 💾 Enhanced data persistence and export functionality

## ✨ Features

### Core Operations

- **Single Set Operations**: Print, Add/Remove elements, Cardinality, Power Set
- **Two Set Operations**: Union, Intersection, Difference, Symmetric Difference, Cartesian Product
- **Set Relationships**: Equality check, Subset verification

### Advanced Features

- 🎯 **Interactive Menu System** - User-friendly navigation
- 📊 **Professional Visualization** - Clean output with Unicode symbols  
- 📜 **Operation History** - Track all performed operations with timestamps
- 💾 **Data Persistence** - Save/Load sets and export results
- 🔧 **Dynamic Set Creation** - Create new sets during runtime
- ⚡ **Error Handling** - Comprehensive input validation and error management
- 🎨 **Enhanced UI** - Emoji icons and formatted displays

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- No external dependencies required

### Installation

```bash
# Clone the repository
git clone https://github.com/OguzhanBerkeOzdil/SET-Theory.git

# Navigate to project directory
cd SET-Theory/FLT-Project

# Run the application
python main.py
```

### Basic Usage

1. **Define Sets** (in `a.txt`):

```python
set1 = {1, 2, 3}
set2 = {1, 2, 41}
set3 = {1, 2, 42525}
```

2. **Run Application**:

```bash
python main.py
```

3. **Interactive Examples**:

```text
🎯 Select option: 1
➤ Enter command: set1 print
📊 Set 'set1': {1, 2, 3}

🎯 Select option: 2  
➤ Enter command: set1 set2 union
∪ set1 ∪ set2 = {1, 2, 3, 41}
```

## 📋 Available Operations

### Single Set Operations

| Command | Description | Example |
|---------|-------------|---------|
| `print` | Display set contents | `set1 print` |
| `add` | Add element to set | `set1 add` |
| `remove` | Remove element from set | `set1 remove` |
| `cardinal` | Show cardinality & power set size | `set1 cardinal` |
| `power` | Display all subsets | `set1 power` |

### Two Set Operations

| Command | Description | Symbol | Example |
|---------|-------------|--------|---------|
| `union` | Set union | ∪ | `set1 set2 union` |
| `intersection` | Set intersection | ∩ | `set1 set2 intersection` |
| `difference` | Set difference | - | `set1 set2 difference` |
| `symmetric` | Symmetric difference | ⊕ | `set1 set2 symmetric` |
| `cartesian` | Cartesian product | × | `set1 set2 cartesian` |
| `equal` | Equality check | = | `set1 set2 equal` |
| `subset` | Subset verification | ⊆ | `set1 set2 subset` |

## 📁 Project Structure

```text
SET-Theory/
├── FLT-Project/
│   ├── main.py              # Main application
│   ├── a.txt                # Set definitions
│   ├── operations1.txt      # Single set operations help
│   ├── operations2.txt      # Two set operations help
│   ├── sets.txt            # Export file (generated)
│   ├── demo.py             # Demonstration script
│   ├── test.py             # Test suite
│   ├── config.json         # Configuration file
│   └── requirements.txt     # Dependencies
├── README.md               # This documentation
└── LICENSE                 # License file
```

## 🎯 Menu Options

1. **Single Set Operations** - Perform operations on individual sets
2. **Two Set Operations** - Perform operations between two sets  
3. **Save Sets to File** - Export current state to `sets.txt`
4. **View All Sets** - Display all loaded sets with cardinalities
5. **Create New Set** - Dynamically create new sets
6. **View Operation History** - See last 10 operations with timestamps
7. **Exit Program** - Save state and exit gracefully

## 🔧 Advanced Features

### Operation History

All operations are automatically logged with timestamps:

```text
📜 Operation History:
────────────────────────────────────────────────────────
 1. [2025-07-05 22:30:15] Print set set1
    Result: {1, 2, 3}
 2. [2025-07-05 22:30:20] Union set1 ∪ set2  
    Result: {1, 2, 3, 41}
```

### Data Export

Export functionality creates detailed reports:

```text
SET OPERATIONS - CURRENT STATE
========================================
Generated: 2025-07-05 22:30:25

set1: {1, 2, 3}
Cardinality: 3
────────────────────
set2: {1, 2, 41}  
Cardinality: 3
────────────────────
```

### Error Handling

- Input validation for all operations
- Graceful handling of invalid set names
- Type checking for numeric inputs
- Comprehensive error messages with suggestions

## 🧪 Testing

The project includes comprehensive testing:

```bash
# Run the test suite
python test.py

# Run demonstration
python demo.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
