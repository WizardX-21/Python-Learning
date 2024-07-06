glossary={
   "Variable": "A storage location identified by a memory address and a symbolic name, which contains some known or unknown quantity of information referred to as a value.",
    "Function": "A block of code that performs a specific task, usually taking some input and returning an output.",
    "Loop": "A control structure used to repeat a block of code a certain number of times or until a condition is met.",
    "List": "A collection of items in a particular order, which can be of different data types.",
    "Dictionary": "A collection of key-value pairs where each key is unique and is used to store data values."
}
for word,meaning in glossary.items():
  print(f'{word}:\n\t{meaning}\n')