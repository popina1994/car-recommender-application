package com.example.djordje.serverconnection;

import android.app.Activity;
import android.content.Context;
import android.util.Log;
import android.widget.Toast;

import net.gotev.uploadservice.ServerResponse;
import net.gotev.uploadservice.UploadInfo;
import net.gotev.uploadservice.UploadServiceBroadcastReceiver;

import static android.content.ContentValues.TAG;
import org.json.*;


/**
 * Created by NORDEUS2 on 22.2.2018.
 */

public class UploadReceiver extends UploadServiceBroadcastReceiver {

    private MainActivity activity;


    public UploadReceiver()
    {
    }

    public UploadReceiver(MainActivity activity)
    {
        this.activity = activity;
    }

    @Override
    public void onProgress(Context context, UploadInfo uploadInfo) {
        super.onProgress(context, uploadInfo);
    }

    @Override
    public void onError(Context context, UploadInfo uploadInfo, ServerResponse serverResponse, Exception exception) {
        super.onError(context, uploadInfo, serverResponse, exception);
    }

    @Override
    public void onCompleted(Context context, UploadInfo uploadInfo, ServerResponse serverResponse) {
        super.onCompleted(context, uploadInfo, serverResponse);
        try
        {
            JSONObject jsonResponse = new JSONObject(serverResponse.getBodyAsString());
            int carType = jsonResponse.getInt("car_type");
            if (activity != null)
            {
                activity.tellCar(carType);
            }

        }
        catch (JSONException ex)
        {

        }
    }
}
