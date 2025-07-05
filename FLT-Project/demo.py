"""
Demo Script for Advanced Set Operations Tool
============================================
This script demonstrates the main features of the Set Operations Tool

Original Project (2022-2023): Oğuzhan Berke Özdil & Berkay Doruk
Enhanced Version (2025): Oğuzhan Berke Özdil
Institution: AGH University of Science and Technology, Krakow
Contact: https://www.linkedin.com/in/oguzhanberkeozdil/
"""

def run_demo():
    """Run a demonstration of the Set Operations Tool"""
    print("🚀 SET OPERATIONS TOOL - DEMONSTRATION")
    print("=" * 50)
    
    # Demo sets
    demo_sets = {
        'demo_a': {1, 2, 3, 4},
        'demo_b': {3, 4, 5, 6},
        'demo_c': {1, 3, 5, 7, 9}
    }
    
    print("\n📊 Demo Sets:")
    for name, set_data in demo_sets.items():
        print(f"  {name}: {set_data}")
    
    print("\n🔧 Performing Operations:")
    print("-" * 30)
    
    # Demo operations
    operations = [
        ("Union", "demo_a ∪ demo_b", demo_sets['demo_a'].union(demo_sets['demo_b'])),
        ("Intersection", "demo_a ∩ demo_b", demo_sets['demo_a'].intersection(demo_sets['demo_b'])),
        ("Difference", "demo_a - demo_b", demo_sets['demo_a'] - demo_sets['demo_b']),
        ("Symmetric Diff", "demo_a ⊕ demo_b", demo_sets['demo_a'].symmetric_difference(demo_sets['demo_b'])),
        ("Cartesian Product", "|demo_a × demo_b|", len([(a, b) for a in demo_sets['demo_a'] for b in demo_sets['demo_b']]))
    ]
    
    for name, expression, result in operations:
        print(f"  {name:15} | {expression:15} = {result}")
    
    print("\n📈 Set Properties:")
    print("-" * 30)
    for name, set_data in demo_sets.items():
        cardinality = len(set_data)
        power_set_size = 2 ** cardinality
        print(f"  |{name}| = {cardinality}, Power set size = {power_set_size}")
    
    print("\n✅ Demo completed successfully!")
    print("Run 'python main.py' to start the interactive tool.")

if __name__ == "__main__":
    run_demo()
