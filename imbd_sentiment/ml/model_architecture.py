import tensorflow as tf

def build_lstm_model(vocab_size, embedding_dim):
    # Input layer
    inputs = tf.keras.Input(shape=(None,), dtype=tf.int32, name='inputs')

    # Embedding layer
    x = tf.keras.layers.Embedding(vocab_size, embedding_dim, mask_zero=True, name='embedding')(inputs)

    # LSTM layer
    x = tf.keras.layers.LSTM(64, name='lstm')(x)

    # Dense layer with sigmoid activation
    outputs = tf.keras.layers.Dense(1, activation='sigmoid', name='output')(x)

    # Create the model
    model = tf.keras.Model(inputs=inputs, outputs=outputs, name='lstm_model')

    return model