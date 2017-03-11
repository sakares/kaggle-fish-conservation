python ~/tensorflow/tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=~/tf_files/bottlenecks \
--how_many_training_steps 500 \
--model_dir=~/tf_files/inception \
--output_graph=~/tf_files/retrained_graph.pb \
--output_labels=~/tf_files/retrained_labels.txt \
--image_dir ~/tf_files/opg



# tensorflow

docker run -it -p 8888:8888 -p 6006:6006 -v $HOME/dl-opg-tumor/tf_files:/tf_files gcr.io/tensorflow/tensorflow:latest-devel 

cp /tf_files/retrain_opg.py tensorflow/examples/image_retraining/retrain_opg.py


# tensorboard

docker run -it -p 8889:8889 -p 6007:6006 -v $HOME/dl-opg-tumor/tf_files:/tf_files  gcr.io/tensorflow/tensorflow:latest-devel 

# get a singleresult

python /tf_files/label_image.py /tf_files/test-set/2-k-case.jpg 

==============================================================================================================================

epoch = 500

python tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/tf_files/bottlenecks \
--how_many_training_steps 500 \
--model_dir=/tf_files/inception \
--output_graph=/tf_files/retrained_graph.pb \
--output_labels=/tf_files/retrained_labels.txt \
--image_dir /tf_files/opg

python retrain.py \
--bottleneck_dir=/tf_files/bottlenecks \
--how_many_training_steps 500 \
--model_dir=/tf_files/inception \
--output_graph=/tf_files/retrained_graph.pb \
--output_labels=/tf_files/retrained_labels.txt \
--image_dir /tf_files/opg

python tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/tf_files/bottlenecks \
--how_many_training_steps 500 \
--model_dir=/tf_files/inception \
--output_graph=/tf_files/retrained_graph.pb \
--output_labels=/tf_files/retrained_labels.txt \
--image_dir /tf_files/ak_case

python tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir ../kaggle-fish-monitoring/bottlenecks \
--how_many_training_steps 500 \
--model_dir ../kaggle-fish-monitoringtf_files/inception \
--output_graph ../kaggle-fish-monitoring/retrained_graph.pb \
--output_labels ../kaggle-fish-monitoring/retrained_labels.txt \
--image_dir ../kaggle-fish-monitoring/data/train \
--summaries_dir ../kaggle-fish-monitoring/retrain_logs

==============================================================================================================================

epoch = 4000

python tensorflow/examples/image_retraining/retrain_original.py \
--bottleneck_dir ../kaggle-fish-monitoring/bottlenecks \
--how_many_training_steps 4000 \
--model_dir ../kaggle-fish-monitoringtf_files/inception \
--output_graph ../kaggle-fish-monitoring/retrained_graph.pb \
--output_labels ../kaggle-fish-monitoring/retrained_labels.txt \
--image_dir ../kaggle-fish-monitoring/data/train \
--summaries_dir ../kaggle-fish-monitoring/retrain_logs/epoch4000



==============================================================================================================================

epoch = 10000

python tensorflow/examples/image_retraining/retrain_original.py \
--bottleneck_dir ../kaggle-fish-monitoring/bottlenecks \
--how_many_training_steps 10000 \
--model_dir ../kaggle-fish-monitoringtf_files/inception \
--output_graph ../kaggle-fish-monitoring/retrained_graph.pb \
--output_labels ../kaggle-fish-monitoring/retrained_labels.txt \
--image_dir ../kaggle-fish-monitoring/data/train \
--summaries_dir ../kaggle-fish-monitoring/retrain_logs/epoch10000