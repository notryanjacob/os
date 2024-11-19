def single_level_paging():
    print("=== Single-Level Paging Implementation===\n")
    #inputs
    logical_addr_space = int(input("Logical addr space : "))
    page_size = int(input("Page Size (in bytes) : "))
    physical_memory_size = int(input("Physical mem : "))

    #calculated
    no_pages = logical_addr_space // page_size
    no_frames = physical_memory_size % page_size
    page_table_size = no_pages*4 #assuming 4 bytes per page table

    print("====Calculated Parameters ====\n")
    print("No pages : ",no_pages)
    print("No frames : ",no_frames)
    print("Page table size : ",page_table_size)

    #Page table mapping
    print("Enter page table mappings (page -> frame)")
    page_table = {}
    for i in range(no_pages):
        frame_no = int(input(f"Page{i} -> Frame: "))
        page_table[i] = frame_no

    #Logical Address Translation
    logical_addr = int(input("\nEnter logical addr : "))
    if logical_addr >= logical_addr_space:
        print("Error: Logical addr exceeds logical addr space")
        return
    
    #Calculate page no and offset
    page_no = logical_addr // page_size
    offset = logical_addr % page_size

    if page_no not in page_table:
        print("Page fault : page not found in page table")
        return
    #Retrieve frame number and computer phy addr
    frame_no = page_table[page_no]
    phy_addr = (frame_no*page_size) + offset

    #output
    print("====Translation results====")
    print("Logical addr : ",logical_addr)
    print("Page num : ", page_no)
    print("Offest : ",offset)
    print("Frame NUmber: ", frame_no)
    print("Phy Addr : ", phy_addr)


single_level_paging()