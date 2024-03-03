"""
This script is designed for use in reverse engineering or code analysis tools to identify and collect strings within binary code or scripts that start with "http". These strings are typically URLs or web resource identifiers. The script examines each operand of a given instruction, checks for data references, and collects those that qualify as "interesting" based on our criteria. The results are returned as a list of StringNode objects, encapsulating the instruction's minimum address, the address of the string, and the string content itself.

This functionality can be particularly useful in security analysis, malware research, or any scenario where identifying external communication attempts or resources is relevant.

@author: Jonas Hagstroem
@category: Strings
@keybinding: None specified
@menupath: None specified
@toolbar: None specified
"""

def isAnInterestingString(string):
 """Returns True if the string is interesting for us"""
 return string.startswith("http")

def getStringReferences(insn):
 """Get strings referenced in any/all operands of an
 	instruction, if present"""
 numOperands = insn.getNumOperands()
 found = []
 for i in range(numOperands):
 	opRefs = insn.getOperandReferences(i)
 	for o in opRefs:
 		if o.getReferenceType().isData():
 			string = getStringAtAddr(o.getToAddress())
 			if string is not None and \
 					isAnInterestingString(string):
 				found.append(StringNode(
 						insn.getMinAddress(),
 						o.getToAddress(),
 						string))
 return found