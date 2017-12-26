package com.example.nenad.kocija.Activity.DetailsActivity;

import android.support.constraint.ConstraintLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import com.example.nenad.kocija.R;

public class DetailsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_details);

        ConstraintLayout constraintLayout = (ConstraintLayout) findViewById(R.id.constraintLayoutID);
        TextView textView = new TextView(this);
        textView.setText("" + DetailsModel.ID);
        constraintLayout.addView(textView);
    }
}
