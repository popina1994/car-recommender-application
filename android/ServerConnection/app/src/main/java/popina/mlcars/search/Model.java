package popina.mlcars.search;

import android.graphics.drawable.Drawable;

/**
 * Created by Djordje on 05-May-18.
 */

public class Model {
    public String link;
    public String real_link;
    public int drawableResource;


    public Model(String l, int d, String rl){
        link = l;
        drawableResource = d;
        real_link = rl;
    }
}
