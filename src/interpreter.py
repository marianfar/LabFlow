'''Instruction interpreter to convert a list of instructions into a dictionary.
!!This experiment assumes the instruction contains a recognizable volume and exactly two well names. 
It isn't robust enough to handle arbitrary instructions yet.
'''

# import python (re) to use regular expressions to parse the instructions
import re

#Convert a simple liquid-transfer instruction into structured data.
def interpret_instruction(instruction):
    if not isinstance(instruction, str): #if the instruction is not a string, return None
        return None

    match = re.search(r"(-?\d+)\s*µL", instruction) 
    #pattern (-?\d+)\s*µL looks for one or more digits, optional whitespace, and then µL. 
    #The parentheses capture the digits so match.group(1) returns the volume.
    
    if match is None: # if no match is found, return None
        return None

    well_matches = re.findall(r"\b[A-B][1-2]\b", instruction)
    #pattern \b[A-B][1-2]\b looks for a capital letter A or B followed by a digit 1 or 2, 
    #with word boundaries on either side.
    
    if len(well_matches) != 2: #if there are not exactly two well matches, return None
        return None
    
    volume = int(match.group(1))
    source = well_matches[0]
    destination = well_matches[1]

    return { #build the transfer dictionary using the extracted values
    "action": "transfer_liquid",
    "source": source,
    "destination": destination,
    "volume_ul": volume,
}
