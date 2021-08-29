install:
	pip install -r requirements.txt

run:
	uvicorn main:app --reload

pylint:
	pylint -j`nproc` backend