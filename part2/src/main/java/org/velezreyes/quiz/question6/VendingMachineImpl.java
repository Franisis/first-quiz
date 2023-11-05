package org.velezreyes.quiz.question6;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {

  private Map<String, Integer> drinks ;

  private Integer quarters;

  private ArrayList<String> names;

  private VendingMachineImpl()
  {
      this.names = new ArrayList<String>();
      this.drinks = new HashMap<String, Integer>();

      this.drinks.put("ScottCola", 75);
      this.names.add("ScottCola");
      this.drinks.put("KarenTea", 100);
      this.names.add("KarenTea");
      
      this.quarters = 0;

  }

  public static VendingMachine getInstance() {
    // Fix me!
    return new VendingMachineImpl() ;
  }

  @Override
  public void insertQuarter() {

    this.quarters+=25;
    //throw new UnsupportedOperationException("Unimplemented method 'insertQuarter'");
    
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    if (this.quarters ==0 ){
      throw new NotEnoughMoneyException();
    }
    if (names.contains(name))
    {
        Integer cost = drinks.get(name);
        if (quarters>=cost && name == "ScottCola")
        {
          quarters= quarters-cost;
          return new DrinkImpl(name, true);
        } 

        if (quarters>=cost && name == "KarenTea")
        {
          quarters= quarters-cost;
          return new DrinkImpl(name, false);
        }
        else { throw new NotEnoughMoneyException();}
        
    }
    else { throw new UnknownDrinkException();}
    

  }

}
