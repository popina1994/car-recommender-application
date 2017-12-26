package com.example.nenad.kocija.Activity.StartCamera;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.graphics.Bitmap;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.FrameLayout;
import android.widget.RelativeLayout;

import com.example.nenad.kocija.Activity.CameraResults.CameraResultsActivity;
import com.example.nenad.kocija.Activity.HelpClass.Data;
import com.example.nenad.kocija.DesignBasics.MyMonitor.MyMonitor;
import com.example.nenad.kocija.R;

public class StartCameraActivity extends AppCompatActivity {

    FrameLayout frameLayout;
    RelativeLayout buttonRL;
    static final int CAM_REQUEST = 1;
    StartCameraModel startCameraModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_start_camera);
        MyMonitor.setUpMonitor(getWindowManager().getDefaultDisplay(),this);

        startCameraModel = new StartCameraModel(this);
        frameLayout = (FrameLayout) findViewById(R.id.frame_layout_startCamera);
        frameLayout.addView(startCameraModel.getStartCameraBackground());
        buttonRL = startCameraModel.getStartCameraButton();
        frameLayout.addView(buttonRL);
        frameLayout.addView(startCameraModel.getStartCameraDescriptionText());

        buttonRL.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                if (takePictureIntent.resolveActivity(getPackageManager())!=null){
                    startActivityForResult(takePictureIntent,CAM_REQUEST);
                }

            }
        });

    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == CAM_REQUEST && resultCode == RESULT_OK) {
            Bundle extras = data.getExtras();
            Data.PICTURE = (Bitmap) extras.get("data");
            startActivity(new Intent(StartCameraActivity.this, CameraResultsActivity.class));
        }
    }

    @SuppressLint("NewApi")
    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        getWindow().getDecorView().setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                        | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                        | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                        | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                        | View.SYSTEM_UI_FLAG_FULLSCREEN
                        | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY);
    }
}
