from tqdm import tqdm

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from better_profanity import profanity
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sentence_transformers import SentenceTransformer, util

from utils import helpers

minilm_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
labse_model = SentenceTransformer("sentence-transformers/LaBSE")

en_stemmer = PorterStemmer()
id_stemmer = StemmerFactory().create_stemmer()


def compute_similarity(text1, text2, labse=True):
    if labse:
        model = labse_model
    else:
        model = minilm_model

    embeddings1 = model.encode([text1], convert_to_tensor=True)
    embeddings2 = model.encode([text2], convert_to_tensor=True)

    cosine_scores = util.cos_sim(embeddings1, embeddings2)

    return float(cosine_scores[0][0])


def filter_concept(text, lang="indonesian"):
    # Step 1: Lowercase both question and question_concept
    question = text["question"].lower()
    question_concept = text["question_concept"].lower()

    # Step 2: Check if question_concept appears in question
    if question_concept in question:
        return True

    # Step 3: If not, split and remove stopwords
    if lang != "sundanese":
        stop_words = stopwords.words(lang)
    else:
        stop_words = []

    concept_words = question_concept.split()
    concept_words = [word for word in concept_words if word not in stop_words]

    # Check if any of the remaining words in question_concept appear in question
    if any(word in question for word in concept_words):
        return True

    # Step 4: Stem words and check if any stem word appears in question

    if lang != "sundanese":
        if lang == "english":
            stemmer = en_stemmer
        elif lang == "indonesian":
            stemmer = id_stemmer
        else:
            raise ValueError(
                f"lang is not in ['english', 'indonesian', 'sundanese'] = {lang}"
            )

        question_stemmed = " ".join(stemmer.stem(word) for word in question.split())
        if any(
            word in question_stemmed
            for word in [stemmer.stem(w) for w in concept_words]
        ):
            return True

    # Step 5: If none of the above conditions met, return False
    return False


def filter_concept_strict(text):
    question = text["question"].lower()
    question_concept = text["question_concepts"].lower()

    return question_concept in question


def filter_profanity(data):
    all_texts = helpers.generate_input_text(data)

    return not profanity.contains_profanity(all_texts)


def filter_data(id_data, su_data, su_id_data, translation_threshold):
    kept_idx = []
    for idx, data in tqdm(enumerate(id_data)):
        direct_sim = compute_similarity(
            helpers.generate_input_text(data),
            helpers.generate_input_text(su_data[idx]),
            labse=True,
        )
        backtrans_sim = compute_similarity(
            helpers.generate_input_text(data),
            helpers.generate_input_text(su_id_data[idx]),
            labse=False,
        )

        direct_decision = bool(direct_sim >= translation_threshold)
        backtrans_decision = bool(backtrans_sim >= translation_threshold)
        id_ca = filter_concept(data, lang="indonesian")
        su_ca = filter_concept(su_data[idx], lang="sundanese")

        su_data[idx]["backtrans_similarity"] = backtrans_sim
        su_data[idx]["backtrans_decision"] = backtrans_decision
        su_data[idx]["direct_similarity"] = direct_sim
        su_data[idx]["direct_decision"] = direct_decision
        su_data[idx]["su_concept_appearance"] = su_ca

        data["backtrans_similarity"] = backtrans_sim
        data["backtrans_decision"] = backtrans_decision
        data["direct_similarity"] = direct_sim
        data["direct_decision"] = direct_decision
        data["su_concept_appearance"] = su_ca
        data["id_concept_appearance"] = id_ca

        if id_ca and su_ca and (backtrans_decision or direct_decision):
            kept_idx.append(idx)

    return kept_idx
