package com.example.nenad.kocija.Dictonary;

import android.content.Context;
import android.graphics.Typeface;

/**
 * Created by nenad on 17.12.2017..
 */

public class Font {

    public static Typeface dancingScriptBold(Context context){
        return Typeface.createFromAsset(context.getAssets(), "fonts/DancingScript-Bold.otf");
    }

    public static Typeface dancingScriptRegular(Context context){
        return Typeface.createFromAsset(context.getAssets(),"fonts/DancingScript-Regular.otf");
    }

    public static Typeface vila_madalena(Context context){
        return Typeface.createFromAsset(context.getAssets(),"fonts/vila_madalena.otf");
    }

    public static Typeface trueno_light(Context context){
        return Typeface.createFromAsset(context.getAssets(),"fonts/TruenoLt.otf");
    }

    public static Typeface trueno_SBd(Context context){
        return Typeface.createFromAsset(context.getAssets(),"fonts/TruenoSBd.otf");
    }

    public static Typeface trueno_UltLt(Context context){
        return Typeface.createFromAsset(context.getAssets(),"fonts/TruenoUltLt.otf");
    }

}
