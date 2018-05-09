package popina.mlcars.upload;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;

import popina.mlcars.R;

import net.gotev.uploadservice.MultipartUploadRequest;
import net.gotev.uploadservice.UploadNotificationConfig;

import java.io.File;
import java.io.FileOutputStream;
import java.text.SimpleDateFormat;
import java.util.Date;

import popina.mlcars.Constants;
import popina.mlcars.common.CommonActivity;
import popina.mlcars.search.SearchActivity;

public class UploadActivity extends CommonActivity
{

    private String filename = "";

    private String absolutePath = "";
    public static final String FULL_MODEL = "fullModel";
    public static final String MODEL = "model";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_upload);

        Intent intent = getIntent();

        absolutePath = intent.getStringExtra("filename");
        Bitmap bitmap = null;

        bitmap = BitmapFactory.decodeFile(absolutePath);
        //mImageView.setImageBitmap(bitmap);
        /*
        try {
            bitmap = MediaStore.Images.Media.getBitmap(getContentResolver(), Uri.parse(absolutePath));
        } catch (IOException e) {
            e.printStackTrace();
        }
        */
        ImageView imgView = (ImageView)findViewById(R.id.uploadImgView);

        imgView.setImageBitmap(bitmap);

    }

    private String currentDateFormat(){
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyyMMdd_HH_mm_ss");
        String  currentTimeStamp = dateFormat.format(new Date());
        return currentTimeStamp;
    }

    public void uploadMultipart() {


        //getting the actual path of the image

        String path = absolutePath;
        Integer size = 0;
        File file = new File(path);
        Bitmap bf = BitmapFactory.decodeFile(path);
        Integer height = bf.getHeight();
        Integer width = bf.getWidth();


        size = width*height;
        try {
            //Creating a multi part request
            new MultipartUploadRequest(this.getApplicationContext(), "", Constants.UPLOAD_URL)
                    .addFileToUpload(absolutePath, "file") //Adding file
                    .addParameter("size", size.toString()) //Adding text parameter to the request
                    .setNotificationConfig(new UploadNotificationConfig())
                    .setMaxRetries(2)
                    .setDelegate(new UploadReceiver(this))
                    .startUpload(); //Starting the upload

        } catch (Exception exc) {
            Toast.makeText(this, exc.getMessage(), Toast.LENGTH_SHORT).show();
        }
    }

    public void displayCarName(String fullModel, String model)
    {
        Toast.makeText(this, fullModel, Toast.LENGTH_LONG).show();
        try {
            Intent intent = new Intent(this,SearchActivity.class);
            intent.putExtra(MODEL, model);
            intent.putExtra(FULL_MODEL, fullModel);
            startActivity(intent);
        } catch (Exception e) {
            // TODO: handle exception
        }
    }


    public boolean saveImageToInternalStorage(Bitmap image) {

        try {
            // Use the compress method on the Bitmap object to write image to
            // the OutputStream
            filename  = "photo_" + currentDateFormat() + ".png";

            FileOutputStream fos = this.openFileOutput(filename, this.MODE_PRIVATE);

            absolutePath = getFileStreamPath(filename).getAbsolutePath();

            // Writing the bitmap to the output stream
            image.compress(Bitmap.CompressFormat.PNG, 100, fos);
            fos.close();
            return true;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    public void onClickUpload(View view){
        uploadMultipart();
    }

}
