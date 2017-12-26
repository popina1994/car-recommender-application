package com.example.nenad.kocija.DesignBasics.MyElements;

import android.app.Activity;
import android.graphics.Color;
import android.view.ViewGroup;
import android.widget.RelativeLayout;

import com.example.nenad.kocija.DesignBasics.MyMonitor.MyMonitor;

/**
 * Created by nenad on 18.12.2017..
 */

public class MyCardView {



    public static RelativeLayout getCardView_W_H_C(Activity activity, int width, int height, int elevation){
        RelativeLayout relativeLayout = getCardView_W_H(activity,width,height,elevation);
        relativeLayout.setX((MyMonitor.getMonitorWidth() - width) /2);
        return relativeLayout;
    }

    public static RelativeLayout getCardView_W_H(Activity activity, int width, int height, int elevation){
        RelativeLayout relativeLayout = getCardView_W_H(activity,width,height);
        relativeLayout.setElevation(elevation);
        relativeLayout.setBackground(MyDrawable.top_bottom_square(Color.WHITE));
        return relativeLayout;
    }

    public static RelativeLayout getCardView_M_H(Activity activity, int height, int elevation){
        RelativeLayout relativeLayout = getCardView_M_H(activity,height);
        relativeLayout.setElevation(elevation);
        relativeLayout.setBackground(MyDrawable.top_bottom_square(Color.WHITE));
        return relativeLayout;
    }

    private static RelativeLayout getCardView_W_H(Activity activity, int width, int height){
        RelativeLayout relativeLayout = new RelativeLayout(activity);
        relativeLayout.setLayoutParams(new RelativeLayout.LayoutParams(width,height));
        return relativeLayout;
    }

    private static RelativeLayout getCardView_M_H(Activity activity, int height){
        RelativeLayout relativeLayout = new RelativeLayout(activity);
        relativeLayout.setLayoutParams(new RelativeLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT,height));
        return relativeLayout;
    }

}
