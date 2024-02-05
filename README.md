avec render :
start command = streamlit run interface.py
pour fastapi : ajouter gunicorn au fichier requirements.txt  
start command: gunicorn api:app -w 4 -k uvicorn.workers.UvicornWorker
