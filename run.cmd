# python yaml.dict.to.org.py base/*.dict.yaml
cat extra.base.org org/gbkpy.org >> pybase.org
sort pybase.org | uniq > tt
mv tt pybase.org

cat org/pyPhrase.org >> pyphrase.org
python yaml.dict.to.org.py phrase/THUOCL_*.dict.yaml
python yaml.dict.to.org.py phrase/sogou_new_words.dict.yaml
python yaml.dict.to.org.py -1000 phrase/clover.phrase.dict.yaml
sort pyphrase.org | uniq > tt
mv tt pyphrase.org
createPYMB pybase.org pyphrase.org
