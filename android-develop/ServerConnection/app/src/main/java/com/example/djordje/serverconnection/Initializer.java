package com.example.djordje.serverconnection;

import android.app.Application;

import net.gotev.uploadservice.UploadService;
import net.gotev.uploadservice.UploadServiceBroadcastReceiver;

/**
 * Created by NORDEUS2 on 22.2.2018.
 */

public class Initializer extends Application {
    private UploadReceiver uploadReceiver;

    @Override
    public void onCreate(){
        super.onCreate();


        UploadService.NAMESPACE = BuildConfig.APPLICATION_ID;

        uploadReceiver = new UploadReceiver();
        uploadReceiver.register(this.getApplicationContext());

    }
}
