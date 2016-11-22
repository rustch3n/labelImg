Here's some tools for format data as what VOC2007 stays.

After image labelling with labelimg.py, 
1)make images and annotations as VOC2007's dir and filename format;
make_voc.sh dir_of_image dir_od_anno target_dir
2)split data into train/validate/test;
split_data.py target_dir int_train int_validate int_test

After all, $target_dir contains the final dataset for further CNN training.