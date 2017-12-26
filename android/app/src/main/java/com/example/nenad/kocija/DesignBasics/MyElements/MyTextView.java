package com.example.nenad.kocija.DesignBasics.MyElements;

import android.app.Activity;
import android.graphics.Color;
import android.view.ViewGroup;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.example.nenad.kocija.Activity.HelpClass.Data;
import com.example.nenad.kocija.DesignBasics.MyMonitor.MyMonitor;
import com.example.nenad.kocija.Dictonary.TextSize;

/**
 * Created by nenad on 18.12.2017..
 */

public class MyTextView {

    public static TextView createButtonForCardView(Activity activity, String string, int textSize, int y, int h){
        TextView textView = new TextView(activity);
        LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT, Data.CARD_VIEW_HEIGHT/(6*h));
        layoutParams.setMargins(MyMonitor.XL_MARGINS,0,0,0);
        textView.setLayoutParams(layoutParams);
        textView.setText(string);
        textView.setTextSize(textSize);
        textView.setTextColor(Color.WHITE);
        if(y == 4) {
            textView.setY(Data.CARD_VIEW_HEIGHT * y / (6));
        }
        else{
            textView.setY(Data.CARD_VIEW_HEIGHT * y / (6) + Data.CARD_VIEW_HEIGHT/12);
        }
        textView.setBackgroundColor(Color.TRANSPARENT);
        return textView;
    }

}
