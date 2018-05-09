package popina.mlcars.search;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import popina.mlcars.R;

import java.util.ArrayList;

import popina.mlcars.search.Model;

/**
 * Created by Djordje on 05-May-18.
 */

public class ModelAdapter extends ArrayAdapter<Model> {
    public ModelAdapter(Context context, ArrayList<Model> models){
        super(context,0,models);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        // Get the data item for this position
        Model model = getItem(position);
        // Check if an existing view is being reused, otherwise inflate the view
        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.my_view, parent, false);
        }
        // Lookup view for data population
        TextView tvName = (TextView) convertView.findViewById(R.id.linkId);
        ImageView imgView = (ImageView) convertView.findViewById(R.id.iconId);
        // Populate the data into the template view using the data object
        tvName.setText(model.link);
        imgView.setImageResource(model.drawableResource);
        //imgView.setImageDrawable(model.drawableResource);
        // Return the completed view to render on screen
        return convertView;
    }

}
