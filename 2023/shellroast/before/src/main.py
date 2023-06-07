"""
Author: Hossin azmoud (Moody0101)
Reviewer: Cameron McPherson (LegitWIZRD)
Date: 10/18/2022
Review Date: 6/2/2023
LICENCE: MIT
Language: Python3.10
Review Language: Python3.11
"""

from time import sleep
from colorama import Fore as f
from UtilPackage import (
	Shell, 
	Command,
	ENCODING,
	HASHING,
	EncodingManager, # EncodingManager(Func: callable, s: str, Op: int)
	ENCODE, 
	DECODE,
	Hasher # Hasher(HashingFunc: callable, s: str) -> str: 
)

DOC = f"""{f.YELLOW}

	Author: {f.BLUE}Hossin azmoud {f.YELLOW}({f.BLUE}Moody0101{f.YELLOW})
 	Refactored by: {f.MAGENTA}Cameron McPherson {f.YELLOW}({f.MAGENTA}LegitWIZRD{f.YELLOW})
  	Refactored Date: {f.BLUE}6/2/2023{f.YELLOW}
	Date: {f.BLUE}10/18/2022{f.YELLOW}
	LICENCE: {f.BLUE}MIT{f.YELLOW}
	Language: {f.BLUE}Python3.10 {f.YELLOW}
 	Refactored Language: {f.MAGENTA}Python3.11 {f.YELLOW}
  
	Descripion: {f.BLUE}A tool to hash, encode, decode text.{f.YELLOW}
 
	Commands: {f.GREEN}hash, encode, decode, help, exit{f.YELLOW}
 
	Usage:{f.GREEN}
		To Encode/Decode:{f.LIGHTGREEN_EX}
			-Encode/Decode <Text> <Algorithm>
				-Only a single value is allowed. (No spaces are allowed)
			-Encode/Decode only for help.{f.GREEN}
		To Hash:{f.LIGHTGREEN_EX}
			-Hash <Text> <Algorithm>
			-Hash only for help.
"""

class Interface:
	""" An interface that handles user interactions with the shell program """
	
	def __init__(self) -> None:
		# Shell initializer
		self.shell = Shell()
		
		
		self.DefaultCommands = {
			'EXIT': self.Exit,
			'HELP': self.Help,
			"HASH": self.hashDoc,
			"DECODE": self.DeDoc,
			"ENCODE": self.EnDoc
		}

		self.Commands = {
			"HASH": self.hashVal,
			"DECODE": self.Decode,
			"ENCODE": self.Encode
		}

	def hashDoc(self):
		""" Displays doc for hashing """
		return HASHING["Doc"] 

	def DeDoc(self):
		""" Displays doc for decoding """
		return ENCODING["Doc"][DECODE]

	def EnDoc(self):
		""" Displays doc for encoding """
		return ENCODING["Doc"][ENCODE]

	def Encode(self, Text, EncoderName):
		if EncoderName.upper().strip() not in ENCODING.keys():
			print()
			print(f"  Incorrect algorithm name, '{EncoderName}'")
			print("  you can only use from this list:")
			for i in ENCODING.keys():
				print(f"     -{i}")
			return

		# Get Encoder function
		func_ = ENCODING[EncoderName.upper().strip()][ENCODE]
		# Map the value
		encode = EncodingManager(func_, ENCODE)
		# return the value
		return encode(Text)

	def Decode(self, Text, DecoderName):
		if DecoderName.upper().strip() not in ENCODING.keys():
			print()
			print(f"  Incorrect algorithm name, '{DecoderName}'")
			print("  you can only use from this list:")
			for i in ENCODING.keys():
				print(f"     -{i}")
			return

		# Get Encoder function
		func_ = ENCODING[DecoderName.upper().strip()][DECODE]
		# Map the value
		decode = EncodingManager(func_, DECODE)
		# return the value
		return decode(Text)

	def hashVal(self, Text, HasherName):
		if HasherName.upper().strip() not in HASHING.keys():
			print()
			print(f"  Incorrect algorithm name, '{HasherName}'")
			print("  you can only use from this list:")
			for i in HASHING.keys():
				print(f"     -{i}")
			return

		return Hasher(HASHING[HasherName.upper().strip()], Text)

	def Exit(self) -> None:
		for i in ['.', '..', '...']:
			print(f"  {f.RED}Exiting{i}{f.WHITE}", end="\r")
			sleep(1)
		exit(0)

	def Help(self):     
		return f"""
		{f.BLUE}
		To Encode/Decode:{f.LIGHTGREEN_EX}
			-Encode/Decode <Text> <Algorithm>
				-Only a single value is allowed. (No spaces are allowed)
			-Encode/Decode only for help.{f.BLUE}
		To Hash:{f.LIGHTGREEN_EX}
			-Hash <Text> <Algorithm>
			-Hash only for help.

		"""
	
 
 
 	# TODO: argv is being used here, but nothing is ever passed into the variable.
	
	def execute(self, command: Command) -> None:
		"""  """
		try:
			if command.CMD in self.DefaultCommands.keys():
				if len(command.argv) > 0:
					print(self.Commands[command.CMD](*command.argv))
				else:
					print(self.DefaultCommands[command.CMD]())
			elif command.CMD in self.Commands.keys():
				if len(command.argv) > 0:
					print(self.Commands[command.CMD](*command.argv))
				else:
					print(self.Commands[command.CMD]())
		except Exception as e:
			print(f"Error: {str(e).capitalize()}.")
		
	def run(self) -> None:
		print(DOC)
		while True:
			self.execute(self.shell.shellInput(Tool=f"ShellRoast"))

def main():
	Interface_ = Interface()
	Interface_.run()

if __name__ == '__main__':
	main()
