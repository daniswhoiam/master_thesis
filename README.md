# Comparative Analysis of Natural Language Processing Models in Materials Science Research

This repository contains the code for the master thesis with the above title, written by Daniil Belazovschi for the Master of Science in Industrial Engineering and Management degree at the Technical University Berlin, in cooperation with the Burton Materials Discovery Lab at Tel Aviv University.

## Installation

Run the following command to install all dependencies.

`pip install -r requirements.txt`

It is recommended to use a conda environment. The dependency file was compiled from a conda environment on a MacBook Pro M2 2023, so platform-specific issues may arise.

## Structure

#### Coprora

The corpora folder contains files with the respective identifiers (DOI for papers, ISBN-13 for textbooks) for the papers and textbooks that have been used in the thesis to create corpora for the use in RAG pipelines. The obtained corpora cannot be uploaded here due to copyright.

### Embedding

The embedding folder contains scripts to embed corpora either from PDF files or from a CSV file using a Haystack-based pipeline. Note that these scripts might assume a certain structure in the source files.

### LLM

The llm folder contains scripts based on Haystack to run experiments on the MaScQA dataset with LLMs only, using the OpenRouter API. The results folder within contains sample results for the experiments performed in the thesis.

### RAG

The rag folder contains scripts based on Haystack to run experiments on the MaScQA dataset with a RAG setup. It assumes that Qdrant is being used as a vector database. LLMs are called via OpenRouter. The results folder within contains sample results for the experiments performed in the thesis.

## Evaluation

For the evaluation, the llm and rag folders contain an automatic evaluation script that uses an LLM from OpenRouter to evaluate the overlap between the correct answers and the generated answers. Note that this process is error-prone and a manual evaluation should follow.
