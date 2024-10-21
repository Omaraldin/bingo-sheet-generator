from merge import merge_a5_to_a4
from fill import generate_bingo_cards
import os
import sys

input_folder = "./out" 
output_folder = "./sheets" 

if __name__ == '__main__':
    sheets_number = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdecimal() else 50
    
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    generate_bingo_cards(sheets_number * 2)
    merge_a5_to_a4(input_folder, output_folder)