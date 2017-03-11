import os
import json
import subprocess
import time
from glob import glob
import re
import tensorflow as tf, sys

def tf_predict(image_path):
    result = ''
    image_name = image_path.split('/')[-1]
    # Read in the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line 
        in tf.gfile.GFile("retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("epoch10000/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, \
            {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        ALB = BET = DOL = LAG = NoF = OTHER = SHARK = YFT = 0.0
        
        for node_id in top_k:
            human_string = label_lines[node_id]
            if human_string == 'alb':
                ALB = predictions[0][node_id]
            elif human_string == 'bet':
                BET = predictions[0][node_id]
            elif human_string == 'dol':
                DOL = predictions[0][node_id]
            elif human_string == 'lag':
                LAG = predictions[0][node_id]
            elif human_string == 'nof':
                NoF = predictions[0][node_id]
            elif human_string == 'other':
                OTHER = predictions[0][node_id]
            elif human_string == 'shark':
                SHARK = predictions[0][node_id]
            elif human_string == 'yft':
                YFT = predictions[0][node_id]

        result = '%s,%.17f,%.17f,%.17f,%.17f,%.17f,%.17f,%.17f,%.17f' % (image_name,ALB,BET,DOL,LAG,NoF,OTHER,SHARK,YFT )
        # print(result)
    return result


def process_file(content_list, continue_idx):
    n = len(content_list)
    idx = continue_idx + 1
    
    processed_count = 0
    time_usage=0
    for image in content_list:
        if processed_count > 4 or time_usage > 10:
            print('terminated! waiting for respawn')
            break

        checking_image = 'data/test/' + image
        print('checking image %s' % checking_image)
        #bucket = image.split('.')
        #image_id = bucket[0]
        
        print('predicting fish probability list from ' + checking_image)
        start = time.time()
        result = tf_predict(checking_image)
        end = time.time()
        time_usage = end - start
        print(time_usage)
        print('sample: %s' % (idx))
        # print(result)

        # bashCommand = "echo \"%s\" >> result/epoch10k/result.txt" % (result)
        # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        # output, error = process.communicate()

        text_file = open("result/epoch10k/result.txt", "a")
        text_file.write('%s\n' % result)
        text_file.close()

        idx = idx + 1
        print('processed_count = %s' % processed_count)
        processed_count = processed_count + 1

    # csv_writer(id_list,label_list)

def last_processed_file(content_list):
    bc = 'll="$(wc -l result/epoch10k/result.txt)"; echo $ll'
    process = subprocess.Popen(bc, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    last_idx =  int(output.split()[0]) - 1
    last_file = content_list[last_idx]
    continue_file = content_list[last_idx + 1]
    print('last_processed file is %s' % last_file)
    print('Continue file is %s' % continue_file)
    return last_idx + 1



content_list = []
for content in os.listdir("data/test/"):
    content_list.append(content)


continue_idx = last_processed_file(content_list)
processing_list = content_list[continue_idx:]
process_file(processing_list, continue_idx)




