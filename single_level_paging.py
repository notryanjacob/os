def single_level_paging():
    # Input Parameters
    print("=== Single-Level Paging Implementation ===\n")
    logical_address_space = int(input("Enter total logical address space (in bytes): "))
    page_size = int(input("Enter page size (in bytes): "))
    physical_memory_size = int(input("Enter total physical memory size (in bytes): "))
    
    # Calculate Number of Pages and Frames
    number_of_pages = logical_address_space // page_size
    number_of_frames = physical_memory_size // page_size
    page_table_entry_size = 4  # Assume 4 bytes per page table entry (can vary)
    
    # Calculate Page Table Size
    page_table_size = number_of_pages * page_table_entry_size

    print("\n=== Calculated Parameters ===")
    print(f"Number of Pages: {number_of_pages}")
    print(f"Number of Frames: {number_of_frames}")
    print(f"Page Table Size: {page_table_size} bytes\n")

    # Page Table Mapping (User Input)
    print("Enter page table mappings (page number to frame number):")
    page_table = {}
    for i in range(number_of_pages):
        frame_number = int(input(f"Page {i} -> Frame: "))
        page_table[i] = frame_number

    # Logical Address Translation
    logical_address = int(input("\nEnter a logical address to translate (in bytes): "))
    if logical_address >= logical_address_space:
        print("Error: Logical address exceeds logical address space.")
        return

    # Calculate Page Number and Offset
    page_number = logical_address // page_size
    offset = logical_address % page_size

    if page_number not in page_table:
        print("Page fault: Page not found in page table.")
        return

    # Retrieve Frame Number and Compute Physical Address
    frame_number = page_table[page_number]
    physical_address = frame_number * page_size + offset

    # Output Results
    print("\n=== Translation Results ===")
    print(f"Logical Address: {logical_address}")
    print(f"Page Number: {page_number}")
    print(f"Offset: {offset}")
    print(f"Frame Number: {frame_number}")
    print(f"Physical Address: {physical_address}")


# Run the implementation
if __name__ == "__main__":
    single_level_paging()
