.PHONY: clean lint

clean:
	rm -rf fluid_simulation/__pycache__
	rm -rf tests/__pycache__
	rm -rf logs/

lint:
	python -m black .
