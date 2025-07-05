"""
Advanced Set Operations Tool
============================
A comprehensive Python application for performing mathematical set operations
with enhanced features, history tracking, and professional visualization.

Original Project (2022-2023): Coursework for "Formal Languages and Compilers"
Authors: Oğuzhan Berke Özdil & Berkay Doruk
Institution: AGH University of Science and Technology, Krakow

Enhanced Version 2.0 (2025): Professional redesign by Oğuzhan Berke Özdil
Contact: https://www.linkedin.com/in/oguzhanberkeozdil/
"""

import os
import json
import time
from datetime import datetime
from typing import Dict, Set, List, Any

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class SetOperations:
    """Main class for handling set operations and management"""
    
    def __init__(self):
        self.sets: Dict[str, Set] = {}
        self.operation_history: List[Dict] = []
        self.load_sets_from_file()
    
    def load_sets_from_file(self):
        """Load sets from a.txt file"""
        try:
            file_path = os.path.join(SCRIPT_DIR, 'a.txt')
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Execute the file content to load sets
                local_vars = {}
                exec(content, {}, local_vars)
                # Get all sets from local variables
                for name, value in local_vars.items():
                    if isinstance(value, set) and not name.startswith('_'):
                        self.sets[name] = value
                print(f"✓ Loaded {len(self.sets)} sets from configuration file")
        except FileNotFoundError:
            print("⚠ Configuration file not found. Creating default sets...")
            self.create_default_sets()
        except Exception as e:
            print(f"⚠ Error loading configuration: {e}")
            self.create_default_sets()
    
    def create_default_sets(self):
        """Create default sets if file doesn't exist"""
        self.sets = {
            'set1': {1, 2, 3},
            'set2': {1, 2, 41},
            'set3': {1, 2, 42525}
        }
        self.save_sets_to_file()
    
    def save_sets_to_file(self):
        """Save current sets to a.txt file"""
        try:
            file_path = os.path.join(SCRIPT_DIR, 'a.txt')
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("#Define your sets like this --> set1 = {1, 2, 3}, set2 = {99, 22, 12125}, ...\n\n")
                for name, set_data in self.sets.items():
                    file.write(f"{name} = {set_data}\n")
            print("✓ Current sets saved to file")
        except Exception as e:
            print(f"❌ Error saving sets: {e}")
    
    def log_operation(self, operation: str, result: str = ""):
        """Log operations for history"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.operation_history.append({
            'timestamp': timestamp,
            'operation': operation,
            'result': str(result)[:100]  # Limit result length
        })
    
    def show_history(self):
        """Display operation history"""
        if not self.operation_history:
            print("📜 No operations performed yet")
            return
        
        print("\n📜 Operation History:")
        print("-" * 60)
        for i, entry in enumerate(self.operation_history[-10:], 1):  # Show last 10
            print(f"{i:2d}. [{entry['timestamp']}] {entry['operation']}")
            if entry['result']:
                print(f"    Result: {entry['result']}")
        print("-" * 60)
    
    def create_new_set(self):
        """Create a new set interactively"""
        name = input("📝 Enter name for new set: ").strip()
        if name in self.sets:
            print(f"⚠ Set '{name}' already exists")
            return
        
        elements_str = input("📝 Enter elements (comma separated): ").strip()
        try:
            elements = {int(x.strip()) for x in elements_str.split(',') if x.strip()}
            self.sets[name] = elements
            print(f"✓ Created set '{name}': {elements}")
            self.log_operation(f"Create set {name}", elements)
        except ValueError:
            print("❌ Error: Please enter valid integers")
    
    def list_all_sets(self):
        """Display all current sets"""
        if not self.sets:
            print("📊 No sets available")
            return
        
        print("\n📊 Current Sets:")
        print("-" * 40)
        for name, set_data in self.sets.items():
            cardinality = len(set_data)
            print(f"  {name}: {set_data} (|{name}| = {cardinality})")
        print("-" * 40)


# Global instance
set_ops = SetOperations()

# Mathematical Operations
def printSet(x: str):
    """Print a specific set"""
    if x in set_ops.sets:
        anySet = set_ops.sets[x]
        print(f"📊 Set '{x}': {anySet}")
        set_ops.log_operation(f"Print set {x}", anySet)
    else:
        print("❌ ERROR: Invalid set name")

def addSet(x: str):
    """Add an element to a set"""
    if x in set_ops.sets:
        anySet = set_ops.sets[x]
        print(f"📊 Current set '{x}': {anySet}")
        try:
            y = int(input("➕ Enter the value to add: "))
            anySet.add(y)
            print(f"✓ Updated set '{x}': {anySet}")
            set_ops.log_operation(f"Add {y} to {x}", anySet)
        except ValueError:
            print("❌ ERROR: Please enter a valid integer")
    else:
        print("❌ ERROR: Invalid set name")

def removeSet(x: str):
    """Remove an element from a set"""
    if x in set_ops.sets:
        anySet = set_ops.sets[x]
        print(f"📊 Current set '{x}': {anySet}")
        try:
            y = int(input("➖ Enter the value to remove: "))
            if y in anySet:
                anySet.remove(y)
                print(f"✓ Updated set '{x}': {anySet}")
                set_ops.log_operation(f"Remove {y} from {x}", anySet)
            else:
                print(f"⚠ Value {y} not found in set '{x}'")
        except ValueError:
            print("❌ ERROR: Please enter a valid integer")
    else:
        print("❌ ERROR: Invalid set name")

def cardinalitySet(x: str):
    """Calculate cardinality and power set size"""
    if x in set_ops.sets:
        anySet = set_ops.sets[x]
        cardinality = len(anySet)
        power_set_size = 2 ** cardinality
        print(f"📊 Set '{x}': {anySet}")
        print(f"📈 Cardinality |{x}|: {cardinality}")
        print(f"🔢 Power set size 2^|{x}|: {power_set_size}")
        set_ops.log_operation(f"Cardinality of {x}", f"Card: {cardinality}, PowerSet: {power_set_size}")
    else:
        print("❌ ERROR: Invalid set name")

def isEqualSet(x: str, y: str):
    """Check if two sets are equal"""
    if x in set_ops.sets and y in set_ops.sets:
        anySet1 = set_ops.sets[x]
        anySet2 = set_ops.sets[y]
        print(f"📊 Set '{x}': {anySet1}")
        print(f"📊 Set '{y}': {anySet2}")
        if anySet1 == anySet2:
            print("✓ Sets are equal")
            result = "Equal"
        else:
            print("❌ Sets are not equal")
            result = "Not equal"
        set_ops.log_operation(f"Compare {x} and {y}", result)
    else:
        print("❌ ERROR: Invalid set name(s)")

def power_set(A: Set) -> List[Set]:
    """Generate power set of a given set"""
    length = len(A)
    l = list(A)
    ps = []
    
    for i in range(2 ** length):
        selector = f'{i:0{length}b}'
        subset = {l[j] for j, bit in enumerate(selector) if bit == '1'}
        ps.append(subset)
    return ps

def cartesianSet(x: str, y: str):
    """Calculate cartesian product of two sets"""
    if x in set_ops.sets and y in set_ops.sets:
        anySet1 = set_ops.sets[x]
        anySet2 = set_ops.sets[y]
        print(f"📊 Set '{x}': {anySet1}")
        print(f"📊 Set '{y}': {anySet2}")
        result = [(a, b) for a in anySet1 for b in anySet2]
        print(f"🔗 Cartesian product ({x} × {y}): {result}")
        print(f"📏 Size: {len(result)}")
        set_ops.log_operation(f"Cartesian {x} × {y}", f"Size: {len(result)}")
    else:
        print("❌ ERROR: Invalid set name(s)")

def differenceSet(x: str, y: str):
    """Calculate set difference"""
    if x in set_ops.sets and y in set_ops.sets:
        anySet1 = set_ops.sets[x]
        anySet2 = set_ops.sets[y]
        print(f"📊 Set '{x}': {anySet1}")
        print(f"📊 Set '{y}': {anySet2}")
        result = anySet1 - anySet2
        print(f"➖ {x} - {y} = {result}")
        set_ops.log_operation(f"Difference {x} - {y}", result)
    else:
        print("❌ ERROR: Invalid set name(s)")

def unionSet(x: str, y: str):
    """Calculate union of two sets"""
    if x in set_ops.sets and y in set_ops.sets:
        anySet1 = set_ops.sets[x]
        anySet2 = set_ops.sets[y]
        print(f"📊 Set '{x}': {anySet1}")
        print(f"📊 Set '{y}': {anySet2}")
        result = anySet1.union(anySet2)
        print(f"∪ {x} ∪ {y} = {result}")
        set_ops.log_operation(f"Union {x} ∪ {y}", result)
    else:
        print("❌ ERROR: Invalid set name(s)")

def intersectionSet(x: str, y: str):
    """Calculate intersection of two sets"""
    if x in set_ops.sets and y in set_ops.sets:
        anySet1 = set_ops.sets[x]
        anySet2 = set_ops.sets[y]
        print(f"📊 Set '{x}': {anySet1}")
        print(f"📊 Set '{y}': {anySet2}")
        result = anySet1.intersection(anySet2)
        print(f"∩ {x} ∩ {y} = {result}")
        set_ops.log_operation(f"Intersection {x} ∩ {y}", result)
    else:
        print("❌ ERROR: Invalid set name(s)")

def symmetricDifferenceSet(x: str, y: str):
    """Calculate symmetric difference of two sets"""
    if x in set_ops.sets and y in set_ops.sets:
        anySet1 = set_ops.sets[x]
        anySet2 = set_ops.sets[y]
        print(f"📊 Set '{x}': {anySet1}")
        print(f"📊 Set '{y}': {anySet2}")
        result = anySet1.symmetric_difference(anySet2)
        print(f"⊕ {x} ⊕ {y} = {result}")
        set_ops.log_operation(f"Symmetric difference {x} ⊕ {y}", result)
    else:
        print("❌ ERROR: Invalid set name(s)")

def isSubset(x: str, y: str):
    """Check if x is subset of y"""
    if x in set_ops.sets and y in set_ops.sets:
        anySet1 = set_ops.sets[x]
        anySet2 = set_ops.sets[y]
        print(f"📊 Set '{x}': {anySet1}")
        print(f"📊 Set '{y}': {anySet2}")
        if anySet1.issubset(anySet2):
            print(f"✓ {x} ⊆ {y} (is subset)")
            result = "Is subset"
        else:
            print(f"❌ {x} ⊄ {y} (is not subset)")
            result = "Is not subset"
        set_ops.log_operation(f"Subset check {x} ⊆ {y}", result)
    else:
        print("❌ ERROR: Invalid set name(s)")

def createFile():
    """Save sets to sets.txt file with better formatting"""
    try:
        file_path = os.path.join(SCRIPT_DIR, 'sets.txt')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("SET OPERATIONS - CURRENT STATE\n")
            f.write("=" * 40 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for name, set_data in set_ops.sets.items():
                f.write(f"{name}: {set_data}\n")
                f.write(f"Cardinality: {len(set_data)}\n")
                f.write("-" * 20 + "\n")
        
        print("✓ Export completed successfully")
        set_ops.log_operation("Export sets to file", f"{len(set_ops.sets)} sets exported")
    except Exception as e:
        print(f"❌ Error creating file: {e}")

# Operation handlers
def one(oper: str, x: str):
    """Handle single-set operations"""
    operations = {
        "print": lambda: printSet(x),
        "add": lambda: addSet(x),
        "remove": lambda: removeSet(x),
        "cardinal": lambda: cardinalitySet(x),
        "power": lambda: print(f"🔢 Power set of '{x}': {[set(s) for s in power_set(set_ops.sets[x])]}") if x in set_ops.sets else print("❌ ERROR: Invalid set name")
    }
    
    if oper in operations:
        operations[oper]()
    else:
        print("❌ ERROR: Invalid operation name")
        print("Available operations: print, add, remove, cardinal, power")

def two(oper: str, x: str, y: str):
    """Handle two-set operations"""
    operations = {
        "equal": lambda: isEqualSet(x, y),
        "cartesian": lambda: cartesianSet(x, y),
        "difference": lambda: differenceSet(x, y),
        "union": lambda: unionSet(x, y),
        "intersection": lambda: intersectionSet(x, y),
        "symmetric": lambda: symmetricDifferenceSet(x, y),
        "subset": lambda: isSubset(x, y)
    }
    
    if oper in operations:
        operations[oper]()
    else:
        print("❌ ERROR: Invalid operation name")
        print("Available operations: equal, cartesian, difference, union, intersection, symmetric, subset")

def show_main_menu():
    """Display the main menu"""
    print("\n" + "=" * 60)
    print("🔢 ADVANCED SET OPERATIONS TOOL v2.0")
    print("    Developed by Oğuzhan Berke Özdil")
    print("=" * 60)
    print("1️⃣  Single Set Operations")
    print("2️⃣  Two Set Operations") 
    print("3️⃣  Save Sets to File")
    print("4️⃣  View All Sets")
    print("5️⃣  Create New Set")
    print("6️⃣  View Operation History")
    print("7️⃣  Exit Program")
    print("=" * 60)

# Main program
def main():
    """Main program loop"""
    print("🚀 Starting Advanced Set Operations Tool...")
    time.sleep(1)
    
    while True:
        try:
            show_main_menu()
            choice = input("🎯 Select an option (1-7): ").strip()
            
            if choice == "1":
                try:
                    file_path = os.path.join(SCRIPT_DIR, "operations1.txt")
                    with open(file_path, "r", encoding='utf-8') as f:
                        print("\n📋 Single Set Operations:")
                        print("-" * 40)
                        print(f.read())
                        print("-" * 40)
                    
                    user_input = input("➤ Enter command (setName operation): ").strip().split()
                    if len(user_input) == 2:
                        x, oper = user_input
                        one(oper, x)
                    else:
                        print("❌ Invalid format. Use: setName operation")
                except FileNotFoundError:
                    print("❌ Operations help file not found. Available operations:")
                    print("  print, add, remove, cardinal, power")
                    user_input = input("➤ Enter command (setName operation): ").strip().split()
                    if len(user_input) == 2:
                        x, oper = user_input
                        one(oper, x)
                    else:
                        print("❌ Invalid format. Use: setName operation")
                    
            elif choice == "2":
                try:
                    file_path = os.path.join(SCRIPT_DIR, "operations2.txt")
                    with open(file_path, "r", encoding='utf-8') as f:
                        print("\n📋 Two Set Operations:")
                        print("-" * 40)
                        print(f.read())
                        print("-" * 40)
                    
                    user_input = input("➤ Enter command (setName1 setName2 operation): ").strip().split()
                    if len(user_input) == 3:
                        x, y, oper = user_input
                        two(oper, x, y)
                    else:
                        print("❌ Invalid format. Use: setName1 setName2 operation")
                except FileNotFoundError:
                    print("❌ Operations help file not found. Available operations:")
                    print("  equal, cartesian, difference, union, intersection, symmetric, subset")
                    user_input = input("➤ Enter command (setName1 setName2 operation): ").strip().split()
                    if len(user_input) == 3:
                        x, y, oper = user_input
                        two(oper, x, y)
                    else:
                        print("❌ Invalid format. Use: setName1 setName2 operation")
                    
            elif choice == "3":
                createFile()
                
            elif choice == "4":
                set_ops.list_all_sets()
                
            elif choice == "5":
                set_ops.create_new_set()
                
            elif choice == "6":
                set_ops.show_history()
                
            elif choice == "7":
                print("💾 Saving current work...")
                set_ops.save_sets_to_file()
                print("👋 Thank you for using the Set Operations Tool!")
                break
                
            else:
                print("❌ Invalid option. Please select 1-7.")
                
        except KeyboardInterrupt:
            print("\n\n⚠ Program stopped by user")
            print("💾 Saving current work...")
            set_ops.save_sets_to_file()
            print("👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            print("🔄 Continuing...")

if __name__ == "__main__":
    main()
