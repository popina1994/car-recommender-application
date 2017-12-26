package com.example.nenad.kocija.DesignBasics.MyMonitor;

import android.app.Activity;
import android.content.Context;
import android.widget.Toast;

/**
 * Created by nenad on 11/25/2017.
 */

public class MyToast {

    public static void setText(Activity activity, int data){
        setToast(activity,"" + data);
    }

    public static void setText(Activity activity, double data){
        setToast(activity,"" + data);
    }

    public static void setText(Activity activity, float data){
        setToast(activity,"" + data);
    }

    public static void setText(Activity activity, long data){
        setToast(activity,"" + data);
    }

    public static void setText(Activity activity, String data){
        setToast(activity,"" + data);
    }

    private static void setToast(final Activity activity, final String string){
        activity.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                Toast.makeText(activity,string,Toast.LENGTH_SHORT).show();
            }
        });
    }

    public static void setText(Context context, int data){
        setToast(context,"" + data);
    }

    public static void setText(Context context, double data){
        setToast(context,"" + data);
    }

    public static void setText(Context context, float data){
        setToast(context,"" + data);
    }

    public static void setText(Context context, long data){
        setToast(context,"" + data);
    }

    public static void setText(Context context, String data){
        setToast(context,"" + data);
    }

    private static void setToast(final Context context, final String string){
        Toast.makeText(context,string,Toast.LENGTH_SHORT).show();
    }

}
