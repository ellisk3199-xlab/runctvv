import wandb

print(f'The version of wandb is:{wandb.__version__}')
#Comment on data type

def display_it(text):
  print(text)
display_it("hello this is just a script")
display_it(type("seeking friends")) # Type 'string' 
display_it(type(3)) # Type 'int'
display_it(type(0.33))  # Type 'bfloat'
