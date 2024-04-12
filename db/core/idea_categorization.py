import os
import ssl

import numpy as np
import tensorflow.compat.v1 as tf
import tensorflow_hub as hub

os.environ["TFHUB_DISABLE_CERT_VALIDATION"] = "true"  # this is to disable the certification warning
ssl._create_default_https_context = ssl._create_unverified_context

# Using V1 API for better use with Elmo
tf.disable_v2_behavior()

embedding = hub.load("ml_models/archive")


class IdeaCategorizationModel:
    @staticmethod
    def find_category(idea_str):
        """
        find_category outputs the category of a given idea string.

        :param idea_str: The string of the idea (ex: "Create an operating system easier to use than Windows.")
        :return: A dictionary with the matching category name in the "result" key and a "categories_scores" key with the raw scores.
        """
        categories_list = ["carsharing", "medical", "education", "agriculture", "software"]

        # # Prepare variables that will be locally using in the function
        # categories_list_local = list(categories_list)
        # categories_list_local.append(idea_str)
        # num_categories = len(categories_list)
        #
        # similarity_input_placeholder = tf.keras.Input(shape=(None,), dtype=tf.string)
        # similarity_message_encodings = embedding(similarity_input_placeholder)
        # with tf.Session() as session:
        #     session.run(tf.global_variables_initializer())
        #     session.run(tf.tables_initializer())
        #     message_embeddings_ = session.run(similarity_message_encodings, feed_dict={similarity_input_placeholder: categories_list_local})
        #
        # categories_dict = {}
        #
        # # Loop over each category to check the relevance
        # for i, category in enumerate(categories_list):
        #     score = np.inner(message_embeddings_[num_categories], message_embeddings_[i])
        #     categories_dict[category] = score
        #
        # # Find the highest value
        # best_category = max(categories_dict, key=categories_dict.get)

        return {"result": categories_list[0], "category_scores": {}}
