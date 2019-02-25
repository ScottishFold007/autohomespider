rem 执行改批处理前先要目录下创建yahei_properties文件 

echo Run Tesseract for Training.. 
tesseract.exe ocr_sim.yahei.exp0.tif ocr_sim.yahei.exp0 nobatch box.train 
 
echo Compute the Character Set.. 
unicharset_extractor.exe ocr_sim.yahei.exp0.box 
mftraining -F yahei_properties -U unicharset -O ocr_sim.unicharset ocr_sim.yahei.exp0.tr 


echo Clustering.. 
cntraining.exe ocr_sim.yahei.exp0.tr 

echo Rename Files.. 
rename normproto ocr_sim.normproto 
rename inttemp ocr_sim.inttemp 
rename pffmtable ocr_sim.pffmtable 
rename shapetable ocr_sim.shapetable  

echo Create Tessdata.. 
combine_tessdata.exe ocr_sim. 

echo. & pause