package popina.mlcars.upload;

import android.content.Context;

import net.gotev.uploadservice.ServerResponse;
import net.gotev.uploadservice.UploadInfo;
import net.gotev.uploadservice.UploadServiceBroadcastReceiver;

import org.json.*;

import popina.mlcars.upload.UploadActivity;


/**
 * Created by NORDEUS2 on 22.2.2018.
 */

public class UploadReceiver extends UploadServiceBroadcastReceiver {
    private UploadActivity activity;

    public UploadReceiver()
    {
        activity = null;
    }

    public UploadReceiver(UploadActivity activity){
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
            String carCompany = jsonResponse.getString("car_company");
            String carModel = jsonResponse.getString("car_model");
            String carChassis = jsonResponse.getString("car_chassis");

            if(activity !=null)
            {
                activity.displayCarName(carCompany + " " + carModel + " " +  carChassis, carModel);
            }

        }
        catch (JSONException ex)
        {
        }
    }
}
