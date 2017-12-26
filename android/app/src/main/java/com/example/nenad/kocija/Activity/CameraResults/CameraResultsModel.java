package com.example.nenad.kocija.Activity.CameraResults;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.Space;
import android.widget.TextView;

import com.example.nenad.kocija.Activity.DetailsActivity.DetailsActivity;
import com.example.nenad.kocija.Activity.DetailsActivity.DetailsModel;
import com.example.nenad.kocija.Activity.HelpClass.CardIDHelper;
import com.example.nenad.kocija.Activity.HelpClass.Data;
import com.example.nenad.kocija.DesignBasics.MyElements.MyButton;
import com.example.nenad.kocija.DesignBasics.MyElements.MyCardView;
import com.example.nenad.kocija.DesignBasics.MyElements.MyDrawable;
import com.example.nenad.kocija.DesignBasics.MyElements.MyImageView;
import com.example.nenad.kocija.DesignBasics.MyElements.MyScrollView;
import com.example.nenad.kocija.DesignBasics.MyElements.MyTextView;
import com.example.nenad.kocija.DesignBasics.MyMonitor.MyMonitor;
import com.example.nenad.kocija.Dictonary.Font;
import com.example.nenad.kocija.Dictonary.TextSize;
import com.example.nenad.kocija.R;

/**
 * Created by nenad on 18.12.2017..
 */

public class CameraResultsModel {

    private Activity activity;
    private LinearLayout scrollView_in;
    private LinearLayout scrollView_out;

    public CameraResultsModel(Activity activity, LinearLayout scrollView_out){
        this.activity = activity;
        this.scrollView_out = scrollView_out;
        scrollView_in = MyScrollView.scrollViewLinearLayout(scrollView_out,activity);

        for(int i = 0; i < 3; i++){
            scrollView_in.addView(createSpace());
            scrollView_in.addView(createCardView(i));
        }
        scrollView_in.addView(createSpace());

    }

    private RelativeLayout createCardView(int i){
        RelativeLayout cardView = MyCardView.getCardView_W_H_C(activity, Data.CARD_VIEW_WIDTH, Data.CARD_VIEW_HEIGHT,Data.CARD_VIEW_ELEVATION);
        LinearLayout linearLayout = new LinearLayout(activity);
        linearLayout.setLayoutParams(new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        linearLayout.setOrientation(LinearLayout.VERTICAL);

        RelativeLayout imageLayout = new RelativeLayout(activity);
        imageLayout.setLayoutParams(new RelativeLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, Data.CARD_VIEW_HEIGHT * 5/6));

//        ImageView imageView = new ImageView(activity);
//        imageView.setLayoutParams(new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
//        imageView.setImageBitmap(Data.PICTURE);
//        imageView.setScaleType(ImageView.ScaleType.FIT_XY);
//        imageLayout.addView(imageView);

        int res;
        switch (i){
            case 0:{
                res = R.drawable.car_1;
                break;
            }
            case 1:{
                res = R.drawable.car_2;
                break;
            }
            default:{
                res = R.drawable.car_3;
                break;
            }
        }
        ImageView imageView = MyImageView.width_height(activity,res,Data.CARD_VIEW_WIDTH,Data.CARD_VIEW_HEIGHT * 5/6);
        imageLayout.addView(imageView);

        LinearLayout shadow = new LinearLayout(activity);
        shadow.setLayoutParams(new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        shadow.setBackground(MyDrawable.top_bottom(Color.TRANSPARENT,Color.BLACK));
        imageLayout.addView(shadow);

        TextView seller = MyTextView.createButtonForCardView(activity, "Moj auto", TextSize.getSellerSize(),3,2);
        seller.setTypeface(Font.trueno_UltLt(activity));
        imageLayout.addView(seller);

        TextView automobile_type = MyTextView.createButtonForCardView(activity, "Mustang GT500", TextSize.getCarNameSize(),4,1);
        automobile_type.setTypeface(Font.trueno_SBd(activity));
        imageLayout.addView(automobile_type);

        linearLayout.addView(imageLayout);

        LinearLayout linearLayout_buttons = new LinearLayout(activity);
        linearLayout_buttons.setLayoutParams(new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT));
        linearLayout_buttons.setOrientation(LinearLayout.HORIZONTAL);
        linearLayout_buttons.setGravity(Gravity.CENTER_VERTICAL);

        Button details = MyButton.createButtonForCardView(activity,"Detalji",MyMonitor.XL_MARGINS);
        linearLayout_buttons.addView(details);

        Button conntact = MyButton.createButtonForCardView(activity,"kontakt",0);
        linearLayout_buttons.addView(conntact);

        linearLayout.addView(linearLayout_buttons);

        final CardIDHelper cardIDHelper = new CardIDHelper(cardView,i);
        details.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                DetailsModel.ID = cardIDHelper.getId();
                Intent intent = new Intent(activity, DetailsActivity.class);
                activity.startActivity(intent);
            }
        });

        cardView.addView(linearLayout);
        return cardView;
    }

    private Space createSpace(){
        Space space = new Space(activity);
        space.setLayoutParams(new RelativeLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, MyMonitor.L_MARGINS));
        return space;
    }

}
