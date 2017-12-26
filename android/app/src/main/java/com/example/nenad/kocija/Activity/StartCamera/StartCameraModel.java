package com.example.nenad.kocija.Activity.StartCamera;

import android.app.Activity;
import android.graphics.Color;
import android.view.Gravity;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.TextView;

import com.example.nenad.kocija.DesignBasics.MyElements.MyDrawable;
import com.example.nenad.kocija.DesignBasics.MyElements.MyImageView;
import com.example.nenad.kocija.DesignBasics.MyMonitor.MyMonitor;
import com.example.nenad.kocija.Dictonary.Dictonary;
import com.example.nenad.kocija.Dictonary.Font;
import com.example.nenad.kocija.Dictonary.TextSize;
import com.example.nenad.kocija.R;

/**
 * Created by nenad on 18.12.2017..
 */

public class StartCameraModel {

    Activity activity;

    public StartCameraModel(Activity activity){
        this.activity = activity;
    }

    public RelativeLayout getStartCameraBackground(){
        RelativeLayout background = new RelativeLayout(activity);
        background.setLayoutParams(new RelativeLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        ImageView imageView = MyImageView.width_height(activity, R.drawable.start_image, MyMonitor.getMonitorWidth(),MyMonitor.getMonitorHeight());
        background.addView(imageView);
        LinearLayout frontBlack = new LinearLayout(activity);
        frontBlack.setLayoutParams(new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        frontBlack.setBackgroundColor(Color.BLACK);
        frontBlack.setAlpha(0.7f);
        background.addView(frontBlack);
        return background;
    }

    public RelativeLayout getStartCameraButton(){
        RelativeLayout relativeLayout = new RelativeLayout(activity);
        relativeLayout.setLayoutParams(new RelativeLayout.LayoutParams(MyMonitor.getMonitorWidth(3),MyMonitor.getMonitorWidth(3)));
        relativeLayout.setX(MyMonitor.getMonitorWidth(2) - MyMonitor.getMonitorWidth(6));
        relativeLayout.setY(MyMonitor.getMonitorHeight(2) - MyMonitor.getMonitorWidth(6) - MyMonitor.getMonitorHeight(64));

        LinearLayout button_back = new LinearLayout(activity);
        button_back.setLayoutParams(new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        button_back.setBackground(MyDrawable.top_bottom_circle(Color.WHITE,MyMonitor.getMonitorWidth(3)));
        button_back.setAlpha(0.7f);
        button_back.setElevation(30);
        relativeLayout.addView(button_back);

        LinearLayout linearLayout = new LinearLayout(activity);
        linearLayout.setLayoutParams(new LinearLayout.LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT));
        linearLayout.setBackgroundResource(R.drawable.ic_camera);
        linearLayout.setElevation(31);
        linearLayout.setAlpha(1.0f);
        linearLayout.setX(MyMonitor.getMonitorWidth(6) - MyMonitor.getIconSize()/2);
        linearLayout.setY(MyMonitor.getMonitorWidth(6) - MyMonitor.getIconSize()/2);
        relativeLayout.addView(linearLayout);

        return relativeLayout;
    }

    public TextView getStartCameraDescriptionText(){
        TextView textView = new TextView(activity);
        textView.setLayoutParams(new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT));
        textView.setText(Dictonary.press_button_start_activity(activity));
        textView.setTextColor(Color.WHITE);
        textView.setGravity(Gravity.CENTER);
        textView.setY(MyMonitor.getMonitorHeight(28,32));
        textView.setAlpha(0.7f);
        textView.setTypeface(Font.dancingScriptRegular(activity));
        textView.setTextSize(TextSize.getTitleSize());
        return textView;
    }

}
