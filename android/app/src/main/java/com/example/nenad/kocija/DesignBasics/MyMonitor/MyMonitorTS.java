package com.example.nenad.kocija.DesignBasics.MyMonitor;

/**
 * Created by nenad on 27.9.2017..
 */

public class MyMonitorTS {

    private static float TEXT_SIZE;

    static void setupMyMonitorTS(){
        TEXT_SIZE = (float) (setTextSize() * 0.95);
    }

    private static float setTextSize(){
        if(MyMonitor.DENSITY_DPI < 140){
            return (float) ( 3 * coefficient_ldpi() / MyMonitor.DENSITY ) * 3;
        }
        if( (140 <= MyMonitor.DENSITY_DPI) && (MyMonitor.DENSITY_DPI < 180)){
            return (float) ( 4.2 * coefficient_mdpi() / MyMonitor.DENSITY ) * 3;
        }
        if( (180 <= MyMonitor.DENSITY_DPI) && (MyMonitor.DENSITY_DPI < 226.5)){
            return 32/5 * coefficient_tvdpi();
        }
        if( (226.5 <= MyMonitor.DENSITY_DPI) && (MyMonitor.DENSITY_DPI < 280)){
            if(MyMonitor.MONITORWIDTH < 700){
                return (float) (6.1 * coefficient_hdpi() / MyMonitor.DENSITY )*3;
            }
            else {
                return (float) (8.3 * coefficient_hdpi() / MyMonitor.DENSITY) * 3;
            }
        }
        if( (280 <= MyMonitor.DENSITY_DPI) && (MyMonitor.DENSITY_DPI < 400)){
            return (float) ( 9.6 * coefficient_xhdpi() / MyMonitor.DENSITY ) * 3;
        }
        if( (400 <= MyMonitor.DENSITY_DPI) && (MyMonitor.DENSITY_DPI < 560)){
            return (float) ( 14.3 * coefficient_xxhdpi() / MyMonitor.DENSITY ) * 3;
        }
        else{
            return (float) ( 18.7 * coefficient_xxxhdpi() / MyMonitor.DENSITY ) * 3;
        }
    }

    private static float coefficient_ldpi(){
        return (float) (MyMonitor.MONITORWIDTH/240);
    }

    private static float coefficient_mdpi(){
        return (float) (MyMonitor.MONITORWIDTH/320);
    }

    private static float coefficient_tvdpi(){
        return (float) (MyMonitor.MONITORWIDTH/800);
    }

    private static float coefficient_hdpi(){
        return (float) (MyMonitor.MONITORWIDTH/480);
    }

    private static float coefficient_xhdpi(){
        return (float) (MyMonitor.MONITORWIDTH/720);
    }

    private static float coefficient_xxhdpi(){
        return (float) (MyMonitor.MONITORWIDTH/1080);
    }

    private static float coefficient_xxxhdpi(){
        return (float) (MyMonitor.MONITORWIDTH/1440);
    }

    public static int getTextSize(){
        return (int) TEXT_SIZE;
    }

    public static int getTextSize(int mul, int divider){
        return (int) (TEXT_SIZE*mul/divider);
    }

    public static int getTextSize(double mul, double divider){
        return (int) (TEXT_SIZE*mul/divider);
    }

    public static int getTextSize(int mul){
        return (int) TEXT_SIZE*mul;
    }

    public static int getTextSize(double mul){
        return (int) (TEXT_SIZE*mul);
    }

}
