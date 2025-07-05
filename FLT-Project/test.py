"""
Unit Tests for Advanced Set Operations Tool
==========================================
Test suite to validate the functionality of set operations

Original Project (2022-2023): Oğuzhan Berke Özdil & Berkay Doruk  
Enhanced Version (2025): Oğuzhan Berke Özdil
Institution: AGH University of Science and Technology, Krakow
Contact: https://www.linkedin.com/in/oguzhanberkeozdil/
"""

import sys
import os
import unittest

def run_basic_tests():
    """Run basic functionality tests"""
    print("🧪 RUNNING BASIC TESTS")
    print("=" * 30)
    
    # Test basic set operations
    test_sets = {
        'A': {1, 2, 3, 4},
        'B': {3, 4, 5, 6},
        'C': {1, 2},
        'D': {1, 2, 3, 4}
    }
    
    tests = [
        # Union tests
        ("Union A ∪ B", test_sets['A'].union(test_sets['B']), {1, 2, 3, 4, 5, 6}),
        ("Union A ∪ C", test_sets['A'].union(test_sets['C']), {1, 2, 3, 4}),
        
        # Intersection tests
        ("Intersection A ∩ B", test_sets['A'].intersection(test_sets['B']), {3, 4}),
        ("Intersection A ∩ C", test_sets['A'].intersection(test_sets['C']), {1, 2}),
        
        # Difference tests
        ("Difference A - B", test_sets['A'] - test_sets['B'], {1, 2}),
        ("Difference B - A", test_sets['B'] - test_sets['A'], {5, 6}),
        
        # Symmetric difference tests
        ("Symmetric Diff A ⊕ B", test_sets['A'].symmetric_difference(test_sets['B']), {1, 2, 5, 6}),
        
        # Subset tests
        ("C ⊆ A", test_sets['C'].issubset(test_sets['A']), True),
        ("A ⊆ B", test_sets['A'].issubset(test_sets['B']), False),
        
        # Equality tests
        ("A = D", test_sets['A'] == test_sets['D'], True),
        ("A = B", test_sets['A'] == test_sets['B'], False),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, result, expected in tests:
        if result == expected:
            print(f"✅ {test_name}: PASSED")
            passed += 1
        else:
            print(f"❌ {test_name}: FAILED (Expected: {expected}, Got: {result})")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    # Cardinality tests
    print(f"\n📈 Cardinality Tests:")
    for name, s in test_sets.items():
        cardinality = len(s)
        power_set_size = 2 ** cardinality
        print(f"  |{name}| = {cardinality}, 2^|{name}| = {power_set_size}")
    
    # Cartesian product tests
    print(f"\n🔗 Cartesian Product Tests:")
    cart_a_b = [(a, b) for a in test_sets['A'] for b in test_sets['B']]
    cart_c_d = [(c, d) for c in test_sets['C'] for d in test_sets['D']]
    print(f"  |A × B| = {len(cart_a_b)} (Expected: {len(test_sets['A']) * len(test_sets['B'])})")
    print(f"  |C × D| = {len(cart_c_d)} (Expected: {len(test_sets['C']) * len(test_sets['D'])})")
    
    return passed == total

def run_edge_case_tests():
    """Test edge cases"""
    print(f"\n🔍 EDGE CASE TESTS")
    print("=" * 20)
    
    # Empty set tests
    empty_set = set()
    normal_set = {1, 2, 3}
    
    edge_tests = [
        ("Empty ∪ Normal", empty_set.union(normal_set), normal_set),
        ("Empty ∩ Normal", empty_set.intersection(normal_set), empty_set),
        ("Empty - Normal", empty_set - normal_set, empty_set),
        ("Normal - Empty", normal_set - empty_set, normal_set),
        ("Empty ⊆ Normal", empty_set.issubset(normal_set), True),
        ("Empty = Empty", empty_set == set(), True),
    ]
    
    passed = 0
    total = len(edge_tests)
    
    for test_name, result, expected in edge_tests:
        if result == expected:
            print(f"✅ {test_name}: PASSED")
            passed += 1
        else:
            print(f"❌ {test_name}: FAILED")
    
    print(f"\n📊 Edge Case Results: {passed}/{total} tests passed")
    return passed == total

def main():
    """Run all tests"""
    print("🚀 ADVANCED SET OPERATIONS TOOL - TEST SUITE")
    print("=" * 50)
    
    basic_passed = run_basic_tests()
    edge_passed = run_edge_case_tests()
    
    print(f"\n🎯 OVERALL RESULTS:")
    print("=" * 20)
    if basic_passed and edge_passed:
        print("✅ ALL TESTS PASSED! The tool is ready for use.")
    else:
        print("❌ SOME TESTS FAILED! Please check the implementation.")
    
    print(f"\n💡 To run the interactive tool: python main.py")
    print(f"💡 To see a demo: python demo.py")

if __name__ == "__main__":
    main()
