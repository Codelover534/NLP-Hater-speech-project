from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s], %(message)s:') 

project_name = "Hate"

list_of_files = [
  f"{project_name}/components/__init__.py",
  f"{project_name}/components/data_ingestion.py",
  f"{project_name}/components/data_transformation.py",
  f"{project_name}/components/model_trainer.py",
  f"{project_name}/components/model_evaluation.py",
  f"{project_name}/components/model_pusher.py",
  f"{project_name}/configuration/__init__.py",
  f"{project_name}/configuration/gclound_syncer.py",
  f"{project_name}/constants/__init__.py",
  f"{project_name}/entity/__init__.py",
  f"{project_name}/entity/config_entity.py",
  f"{project_name}/entity/artifact_entity.py",
  f"{project_name}/exception/__init__.py",
  f"{project_name}/logger/__init__.py",
  f"{project_name}/pipline/__init__.py", 
  f"{project_name}/pipline/train_pipeline.py", 
  f"{project_name}/pipline/prediction_pipeline.py", 
  f"{project_name}/ml/__init__.py", 
  f"{project_name}/ml/model.py", 
  f"{project_name}/ml/model.py", 
  "app.py",
  "demo.py",
  "requirements.txt",
  "Dockerfile",
  "setup.py",
  ".dockerignore"
]

for file_path in list_of_files:
  # convert string to path object
  file_path = Path(file_path) 

  file_dir = file_path.parent
  file_name = file_path.name

  if file_dir != "":
    # file.dir to make folder
    file_dir.mkdir(parents=True, exist_ok=True)
    logging.info(f"Creating directory: {file_dir} for the file: {file_name}")

  if file_name != "":
    file_path.touch(exist_ok=True)
    logging.info(f"Creating file: {file_path}")

  else:
    logging.info(f"File already exists: {file_path}")
