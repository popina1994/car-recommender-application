package com.example.nenad.kocija.DesignBasics.MyElements;

import android.app.Activity;
import android.graphics.Color;
import android.view.Gravity;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.example.nenad.kocija.Activity.HelpClass.Data;
import com.example.nenad.kocija.DesignBasics.MyMonitor.MyMonitor;
import com.example.nenad.kocija.Dictonary.Font;

/**
 * Created by nenad on 18.12.2017..
 */

public class MyButton {

    public static Button createButtonForCardView(Activity activity, String string, int left_marginue){
        Button button = new Button(activity);
        LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT, Data.CARD_VIEW_HEIGHT/6);
        layoutParams.setMargins(left_marginue,0,0,0);
        button.setLayoutParams(layoutParams);
        button.setText(string);
        button.setTextColor(Color.BLACK);
        button.setBackgroundColor(Color.TRANSPARENT);
        button.setGravity(Gravity.CENTER_VERTICAL);
        button.setTypeface(Font.trueno_light(activity));
        return button;
    }

}
