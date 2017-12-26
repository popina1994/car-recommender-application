package com.example.nenad.kocija.Dictonary;


import com.example.nenad.kocija.DesignBasics.MyMonitor.MyMonitorTS;

/**
 * Created by nenad on 12.10.2017..
 */

public class TextSize {

    public static int getTextSize(){
        return MyMonitorTS.getTextSize();
    }

    public static int getTitleSize(){
        return MyMonitorTS.getTextSize(1.4);
    }

    public static int getCarNameSize(){
        return MyMonitorTS.getTextSize(2);
    }

    public static int getSellerSize(){
        return MyMonitorTS.getTextSize(1.2);
    }

}
