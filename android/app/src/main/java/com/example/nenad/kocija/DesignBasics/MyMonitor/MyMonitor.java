package com.example.nenad.kocija.DesignBasics.MyMonitor;

import android.app.Activity;
import android.content.Context;
import android.content.res.Configuration;
import android.content.res.Resources;
import android.graphics.Point;
import android.net.ConnectivityManager;
import android.view.Display;

/**
 * Created by nenad on 3/2/2017.
 */

public class MyMonitor {

    public static int MONITORHEIGHT;
    public static int MONITORWIDTH;
    public static float DENSITY_DPI;
    public static float DENSITY;
    protected static int MARGINS;
    public static int S_MARGINS;
    public static int M_MARGINS;
    public static int L_MARGINS;
    public static int XL_MARGINS;
    public static int XXL_MARGINS;
    public static Display DISPLAY;
    private static int ICON_SIZE;

    /// have to call in MainActivity like this:
    /// MyMonitor.setUpMonitor(getWindowManager().getDefaultDisplay());
    public static void setUpMonitor(Display display, Activity activity){
        DENSITY_DPI = activity.getResources().getDisplayMetrics().densityDpi;
        DENSITY = activity.getResources().getDisplayMetrics().density;
        DISPLAY = display;
        ICON_SIZE = MyMonitorIconSize.setTextSize();
        navigationBarSize(activity);
        setMonitorHeight(display,activity);
        setMonitorWidth(display,activity);
        MyMonitorTS.setupMyMonitorTS();
        XXL_MARGINS = ICON_SIZE/2;
        XL_MARGINS = ICON_SIZE *3/8;
        L_MARGINS = ICON_SIZE *2/8;
        M_MARGINS = L_MARGINS *2/3;
        S_MARGINS = M_MARGINS/2;
    }

    private static void setMonitorHeight(Display display, Activity activity) {
        Point size = new Point();
        display.getSize(size);
        MONITORHEIGHT = size.y;
        if(activity.getResources().getConfiguration().orientation == Configuration.ORIENTATION_PORTRAIT) {
            if (producerCondition()) {
                MONITORHEIGHT += MARGINS;
            }
            else{

            }
        }
    }

    private static void setMonitorWidth(Display display, Activity activity) {
        Point size = new Point();
        display.getSize(size);
        MONITORWIDTH = size.x;
        if(activity.getResources().getConfiguration().orientation == Configuration.ORIENTATION_LANDSCAPE){
            if (producerCondition()){
                MONITORWIDTH += MARGINS;
            }
        }
    }

    private static boolean producerCondition(){
        if(!android.os.Build.MANUFACTURER.toLowerCase().equals("samsung"))
            return true;
        else
            return false;
    }

    public static int getMonitorHeight(){
        return MONITORHEIGHT;
    }

    public static int getMonitorWidth(){
        return MONITORWIDTH;
    }

    public static int getMonitorHeight(int devider){
        return MONITORHEIGHT / devider;
    }

    public static int getMonitorWidth(int devider){
        return MONITORWIDTH / devider;
    }

    public static double getMonitorHeight(double devider){
        return MONITORHEIGHT / devider;
    }

    public static double getMonitorWidth(double devider){
        return MONITORWIDTH / devider;
    }

    public static int getMonitorHeight(int mul, int devider){
        return MONITORHEIGHT * mul / devider;
    }

    public static int getMonitorHeight(double mul, int devider){
        return (int) (MONITORHEIGHT * mul / devider);
    }

    public static double getMonitorHeight(double mul, double devider){
        return MONITORHEIGHT * mul / devider;
    }

    public static int getMonitorWidth(int mul, int devider) {
        return MONITORWIDTH * mul / devider;
    }

    public static int getMonitorWidth(double mul, int devider) {
        return (int) (MONITORWIDTH * mul / devider);
    }

    private static int navigationBarSize(Context context){
        Resources resources = context.getResources();
        int resourceId = resources.getIdentifier("navigation_bar_height", "dimen", "android");
        if (resourceId > 0) {
            MARGINS = resources.getDimensionPixelSize(resourceId);
            return resources.getDimensionPixelSize(resourceId);
        }
        MARGINS = 0;
        return 0;
    }

    public static int getStatusBarHeight(Context context) {
        int result = 0;
        int resourceId = context.getResources().getIdentifier("status_bar_height", "dimen", "android");
        if (resourceId > 0) {
            result = context.getResources().getDimensionPixelSize(resourceId);
        }
        return result;
    }

    public static int getMonitorWidthMargins() {
        return MONITORWIDTH - 2*M_MARGINS;
    }

    public static int getIconSize(){
        return ICON_SIZE;
    }

    public static boolean isNetworkConnected(Activity activity) {
        ConnectivityManager cm = (ConnectivityManager) activity.getSystemService(Context.CONNECTIVITY_SERVICE);
        return cm.getActiveNetworkInfo() != null;
    }

}
