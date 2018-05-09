package popina.mlcars.upload;

import android.app.Application;

import popina.mlcars.BuildConfig;

import net.gotev.uploadservice.UploadService;

import popina.mlcars.upload.UploadReceiver;

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
