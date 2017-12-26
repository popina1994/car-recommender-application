package com.example.nenad.kocija.Activity.HelpClass;

import android.widget.RelativeLayout;

/**
 * Created by nenad on 18.12.2017..
 */

public class CardIDHelper {

    RelativeLayout cardView;
    int id;

    public CardIDHelper(RelativeLayout cardView, int id) {
        this.cardView = cardView;
        this.id = id;
    }

    public int getId() {
        return id;
    }

    public RelativeLayout getCard(){
        return cardView;
    }


}
