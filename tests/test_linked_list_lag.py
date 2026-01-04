import time
import sys
import os
# Ensure 'app' is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.linked_list import LinkedList

def test_performance():
    ll = LinkedList()
    start_time = time.time()
    
    # Append 10,000 items
    for i in range(10000):
        ll.append(f"item-{i}")
    
    append_duration = time.time() - start_time
    print(f"Time to append 10,000 items: {append_duration:.4f} seconds")

    # Traverse
    start_time = time.time()
    data = ll.to_list()
    traverse_duration = time.time() - start_time
    print(f"Time to to_list 10,000 items: {traverse_duration:.4f} seconds")

    # Remove end
    start_time = time.time()
    for i in range(100):
        ll.remove_at_end()
    remove_end_duration = time.time() - start_time
    print(f"Time to remove 100 items from end: {remove_end_duration:.4f} seconds")

if __name__ == "__main__":
    test_performance()
