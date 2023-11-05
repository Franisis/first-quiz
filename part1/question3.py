################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

class Oven:
      def __init__(self, ):
            self.items=[]
            self.message=""
            
      def add(self,item):
            self.items.append(item)
      
      def freeze(self):
            if self.items == ['water','air'] or self.items == ['air','water']:
                  self.message='snow'
                  
      def boil(self):
          results={
          "pizza":0,
          "gold":0,
          }
          for i in self.items:
              if i == "tomato":
                    results["pizza"]+=1
              elif i == "dough":
                    results["pizza"]+=1
              elif i == "cheese":
                    results["pizza"]+=1
              elif i == "lead":
                    results["gold"]+=1
              elif i == "mercury":
                    results["gold"]+=1
          if results['pizza']==3 and results['gold']==0:
                self.message="pizza"     
          elif results['pizza']==0 and results['gold']==2:
                self.message="gold"     
          return self.message
          
      def wait(self):
            self.message=None
      
      def get_output(self):
            return self.message
      
def make_oven():
  return Oven()

def alchemy_combine(oven, ingredients, temperature):
  """
    oven: An object of type <Oven>
    ingredients: is a list of strings 
    temperature: an integer or a float?
  """  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()
