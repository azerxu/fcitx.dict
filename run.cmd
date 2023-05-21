python yaml.dict.to.org.py base/*.dict.yaml
python yaml.dict.to.org.py phrase/*.dict.yaml
sort pybase.org | uniq > tt
mv tt pybase.org
sort pyphras | uniq > tt
mv tt pyphras
createPYMB pybase.org pyphras.org
