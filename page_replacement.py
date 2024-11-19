def fifo_page_replacement(pages, capacity):
    """
    FIFO Page Replacement Algorithm
    :param pages: List of page requests
    :param capacity: Number of frames available in memory
    :return: Total page faults
    """
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) >= capacity:
                memory.pop(0)  # Remove the first page (FIFO)
            memory.append(page)  # Add the new page
    return page_faults


def lru_page_replacement(pages, capacity):
    """
    LRU Page Replacement Algorithm
    :param pages: List of page requests
    :param capacity: Number of frames available in memory
    :return: Total page faults
    """
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) >= capacity:
                # Remove the least recently used page
                memory.pop(0)
        else:
            # Remove the page and re-add it to mark it as recently used
            memory.remove(page)
        memory.append(page)
    return page_faults


def optimal_page_replacement(pages, capacity):
    """
    Optimal Page Replacement Algorithm
    :param pages: List of page requests
    :param capacity: Number of frames available in memory
    :return: Total page faults
    """
    memory = []
    page_faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            page_faults += 1
            if len(memory) >= capacity:
                # Find the page to replace (farthest in future)
                farthest = -1
                index_to_replace = -1
                for j in range(len(memory)):
                    if memory[j] not in pages[i + 1:]:
                        index_to_replace = j
                        break
                    else:
                        next_occurrence = pages[i + 1:].index(memory[j])
                        if next_occurrence > farthest:
                            farthest = next_occurrence
                            index_to_replace = j
                memory.pop(index_to_replace)
            memory.append(pages[i])
    return page_faults


# Main Code
if __name__ == "__main__":
    print("Page Replacement Algorithms Comparison\n")
    pages = list(map(int, input("Enter the sequence of page requests (space-separated): ").split()))
    capacity = int(input("Enter the number of frames available: "))

    fifo_faults = fifo_page_replacement(pages, capacity)
    lru_faults = lru_page_replacement(pages, capacity)
    optimal_faults = optimal_page_replacement(pages, capacity)

    print("\nResults:")
    print(f"FIFO Page Faults: {fifo_faults}")
    print(f"LRU Page Faults: {lru_faults}")
    print(f"Optimal Page Faults: {optimal_faults}")
