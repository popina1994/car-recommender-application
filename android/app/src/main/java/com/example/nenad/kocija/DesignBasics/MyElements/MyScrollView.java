package com.example.nenad.kocija.DesignBasics.MyElements;

import android.app.Activity;
import android.content.Context;
import android.view.ViewGroup;
import android.widget.LinearLayout;
import android.widget.ScrollView;

/**
 * Created by nenad on 2.10.2017..
 */

public class MyScrollView {

    public static LinearLayout scrollViewLinearLayout(LinearLayout linearLayout_out, Context context, int width){
        LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(width, ViewGroup.LayoutParams.MATCH_PARENT);
        ScrollView scrollView = new ScrollView(context);
        scrollView.setLayoutParams(layoutParams);
        LinearLayout linearLayout_in = new LinearLayout(context);
        linearLayout_in.setLayoutParams(layoutParams);
        linearLayout_in.setOrientation(LinearLayout.VERTICAL);

        linearLayout_out.addView(scrollView);
        scrollView.addView(linearLayout_in);
        return linearLayout_in;
    }

    public static LinearLayout scrollViewLinearLayout(LinearLayout linearLayout_out, Activity activity){
        LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT);
        ScrollView scrollView = new ScrollView(activity);
        scrollView.setLayoutParams(layoutParams);
        LinearLayout linearLayout_in = new LinearLayout(activity);
        linearLayout_in.setLayoutParams(layoutParams);
        linearLayout_in.setOrientation(LinearLayout.VERTICAL);

        linearLayout_out.addView(scrollView);
        scrollView.addView(linearLayout_in);
        return linearLayout_in;
    }

}
