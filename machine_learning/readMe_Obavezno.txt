Uputstvo:
U folderu inception nalazi se potrebni materijal za preprocesiranje slika i treniranje neuralne mreze.
U okviru tog foldera su:
Folder create_tfrecords - Koristi se za konvertovanje slika u .tfrecord format. Ovaj format kasnije
sluzi za treniranje i validaciju mreze.

Folder transfer_learning - U ovom folderu se obavlja treniranje i validacija.

Fajl checkpoint_model_api.py - Ovaj fajl predstavlja vezu izmedju ML dela i servera. Sluzi za
ucitavanje mreze i predikciju novih slika. U njemu je objasnjeno kako se pokrece.

car_models.txt - Sadrzi spisak modela koje planiramo da koristimo u ovom projektu.
