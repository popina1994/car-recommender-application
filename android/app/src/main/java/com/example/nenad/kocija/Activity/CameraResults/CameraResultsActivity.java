package com.example.nenad.kocija.Activity.CameraResults;

import android.app.Activity;
import android.graphics.Color;
import android.os.Build;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;

import com.example.nenad.kocija.Activity.HelpClass.Data;
import com.example.nenad.kocija.DesignBasics.MyElements.MyCardView;
import com.example.nenad.kocija.R;

public class CameraResultsActivity extends AppCompatActivity {

    ImageView imageView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_camera_results);
        setLightStatusBar(getWindow().getDecorView(),this);

        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        toolbar.setTitle("Results");
        toolbar.setTitleTextColor(Color.BLACK);
        toolbar.setElevation(Data.TOOL_BAR_ELEVATION);

        LinearLayout linearLayout = (LinearLayout) findViewById(R.id.activity_camera_results);
        CameraResultsModel cameraResultsModel = new CameraResultsModel(this,linearLayout);

//        imageView = new ImageView(this);
//        imageView.setLayoutParams(new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT));
//        imageView.setImageBitmap(Data.PICTURE);
//        linearLayout.addView(imageView);

        RelativeLayout cardView = MyCardView.getCardView_W_H_C(this, Data.CARD_VIEW_WIDTH, Data.CARD_VIEW_HEIGHT,Data.CARD_VIEW_ELEVATION);
        linearLayout.addView(cardView);
    }

    public static void setLightStatusBar(View view, Activity activity){

        if (Build.VERSION.SDK_INT >= 23) {
            int flags = view.getSystemUiVisibility();
            flags |= View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR;
            view.setSystemUiVisibility(flags);
            activity.getWindow().setStatusBarColor(Color.parseColor("#f7f7f7"));
        }
    }
}
