package popina.mlcars.search;

import android.app.SearchManager;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.TextView;

import popina.mlcars.R;

import java.text.MessageFormat;
import java.util.ArrayList;
import java.util.HashMap;

import popina.mlcars.common.CommonActivity;
import popina.mlcars.upload.UploadActivity;

public class SearchActivity extends CommonActivity
{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);

        String fullModel = getIntent().getStringExtra(UploadActivity.FULL_MODEL);
        String model = getIntent().getStringExtra(UploadActivity.MODEL);

        TextView tv = (TextView)findViewById(R.id.modelNameId);
        tv.setText(fullModel);

        ListView listView = (ListView)findViewById((R.id.listViewId));

        final ArrayList<Model> arrayOfModels = new ArrayList<Model>();

        String googleURL = "https://www.google.com/search?hl=en&site=imghp&tbm=isch&source=hp&q="+fullModel;

        arrayOfModels.add(new Model("Best cars in the world", R.drawable.stevens_creek_bmw,stevenCreekBmw(model)));
        arrayOfModels.add(new Model("Trade car and get best match", R.drawable.autotrader,"https://www.autotrader.com/"));
        arrayOfModels.add(new Model("Find your favourite fullModel", R.drawable.bmw_usa,"https://www.bmwusa.com/"));
        arrayOfModels.add(new Model("We are here for you", R.drawable.audi_usa,"https://www.audiusa.com/"));
        arrayOfModels.add(new Model("Check for fullModel online", R.drawable.google_pic, googleURL));

        ModelAdapter adapter = new ModelAdapter(this,arrayOfModels);



        listView.setAdapter(adapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                goOnlineWithLink(arrayOfModels.get(i).real_link);
            }
        });
    }

    private static String stevenCreekBmw(String model)
    {
        String homePage = "https://www.stevenscreekbmw.com/new-inventory/index.htm?search=&saveFacetState=true&model={0}&lastFacetInteracted=inventory-listing1-facet-anchor-model-27";
        HashMap<String, String> modelToModel = new HashMap<>();
        modelToModel.put("x5", "X5");
        modelToModel.put("x3", "X3");
        modelToModel.put("x1", "X1");
        modelToModel.put("3xd", "320i");
        modelToModel.put("520d", "540d");
        modelToModel.put("118d", "118d");
        String urlToFollow;
        urlToFollow = MessageFormat.format(homePage, modelToModel.get(model));
        return urlToFollow;
    }

    public void goOnlineWithLink(String link){
        Intent intent = new Intent(Intent.ACTION_WEB_SEARCH);
        intent.putExtra(SearchManager.QUERY, link);
        startActivity(intent);
    }
}
