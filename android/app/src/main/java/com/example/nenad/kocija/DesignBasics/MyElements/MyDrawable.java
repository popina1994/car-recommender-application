package com.example.nenad.kocija.DesignBasics.MyElements;

import android.graphics.drawable.Drawable;
import android.graphics.drawable.GradientDrawable;

/**
 * Created by nenad on 13.10.2017..
 */

public class MyDrawable {

    public static GradientDrawable top_bottom(int color){
        int colors[] = {color,color,color};
        GradientDrawable shape = new GradientDrawable(GradientDrawable.Orientation.TOP_BOTTOM,colors);
        return shape;
    }

    public static GradientDrawable top_bottom_stroke(int color, int strokeColor){
        int colors[] = {color,color,color};
        GradientDrawable shape = new GradientDrawable(GradientDrawable.Orientation.TOP_BOTTOM,colors);
        shape.setStroke(2, strokeColor);
        return shape;
    }

    public static GradientDrawable top_bottom_circle(int color,int radius){
        int colors[] = {color,color};
        GradientDrawable shape = new GradientDrawable(GradientDrawable.Orientation.TL_BR,colors);
        shape.setGradientType(GradientDrawable.RADIAL_GRADIENT);
        shape.setShape(GradientDrawable.OVAL);
        shape.setGradientRadius(radius/2);
        shape.setGradientCenter(0.5f,0.5f);
        return shape;
    }

    public static GradientDrawable top_bottom_square(int color){
        int colors[] = {color,color};
        GradientDrawable shape = new GradientDrawable(GradientDrawable.Orientation.TL_BR,colors);
        return shape;
    }

    public static GradientDrawable tl_br(int color1, int color2){
        int colors[] = {color1,color2};
        GradientDrawable shape = new GradientDrawable(GradientDrawable.Orientation.TL_BR,colors);
        return shape;
    }

    public static GradientDrawable top_bottom(int color1, int color2){
        int colors[] = {color1,color2};
        GradientDrawable shape = new GradientDrawable(GradientDrawable.Orientation.TOP_BOTTOM,colors);
        return shape;
    }

}
