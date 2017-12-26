package com.example.nenad.kocija.DesignBasics.MyElements;

import android.app.Activity;
import android.content.res.Resources;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.widget.ImageView;
import android.widget.LinearLayout;

/**
 * Created by nenad on 17.12.2017..
 */

public class MyImageView {

    public static ImageView width_height(Activity activity, int resources, int width, int height){
        ImageView imageView = imageView(activity,resources,width,height);
        imageView.setScaleType(ImageView.ScaleType.FIT_XY);
        return imageView;
    }

    ///////////////////////////////////////////////////////////////////////////////////////////

    private static ImageView imageView(Activity activity, int resources, int width, int height){
        ImageView imageView = new ImageView(activity);
        imageView.setImageBitmap(decodeBitmapWithGiveFromResource(activity.getResources(),resources,width,height));
        LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(width,height);
        imageView.setLayoutParams(layoutParams);
        return imageView;
    }

    private static Bitmap decodeBitmapWithGiveFromResource(Resources res, int resID, int reqWidth, int reqHeight){
        final BitmapFactory.Options options = new BitmapFactory.Options();
        options.inJustDecodeBounds = true;
        BitmapFactory.decodeResource(res, resID, options);
        options.inSampleSize = calculateSampleSize(options,reqWidth,reqHeight);
        options.inJustDecodeBounds = false;
        return BitmapFactory.decodeResource(res,resID,options);
    }

    private static int calculateSampleSize(BitmapFactory.Options options, int reqWidth, int reqHeight){
        final int height = options.outHeight;
        final int width = options.outWidth;
        int inSampleSize = 1;

        if(height > reqHeight || width > reqWidth){
            final int halfHeight = height/2;
            final int halfWidth = width/2;
            while((halfHeight / inSampleSize) > reqHeight && (halfWidth / inSampleSize) > reqWidth){
                inSampleSize *= 2;
            }
        }

        return inSampleSize;
    }

}
