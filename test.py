#from langchain_community.llms import Ollama
import ollama

models_ollama = ollama.list()["models"]
print([m["model"] for m in models_ollama])
print([m["size"] for m in models_ollama])