package org.velezreyes.quiz.question6;

public class DrinkImpl implements Drink {


    private String name;

    private boolean isFizzy;

    public DrinkImpl(String n, Boolean f)
    {
        this.name=n;
        this.isFizzy=f;
    }

    @Override
    public String getName() {
        // TODO Auto-generated method stub
        //throw new UnsupportedOperationException("Unimplemented method 'getName'");
        return this.name;
    }

    @Override
    public boolean isFizzy() {
        // TODO Auto-generated method stub
        //throw new UnsupportedOperationException("Unimplemented method 'isFizzy'");
        return this.isFizzy;
    }



}
