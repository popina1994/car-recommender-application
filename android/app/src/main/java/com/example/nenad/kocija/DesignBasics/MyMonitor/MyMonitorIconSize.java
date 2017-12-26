package com.example.nenad.kocija.DesignBasics.MyMonitor;

/**
 * Created by nenad on 8.10.2017..
 */

class MyMonitorIconSize {

    static int setTextSize(){
        if( MyMonitor.DENSITY_DPI < 226.5){
            return 32;
        }
        if( (226.5 <= MyMonitor.DENSITY_DPI) && (MyMonitor.DENSITY_DPI < 280)){
            return 48;
        }
        if( (280 <= MyMonitor.DENSITY_DPI) && (MyMonitor.DENSITY_DPI < 400)){
            return 64;
        }
        if( 400 <= MyMonitor.DENSITY_DPI){
            return 96;
        }
        return 0;
    }

}
