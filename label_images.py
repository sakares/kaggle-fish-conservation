import tensorflow as tf, sys

# change this as you see fit
image_path = sys.argv[1]

# Read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("epoch500/retrained_graph.pb", 'rb') as f:
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
    result = ''

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

    result = '%s,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f' % ("image_id_n",ALB,BET,DOL,LAG,NoF,OTHER,SHARK,YFT )
    print(result)