test:
	mkdir -p var/reports/
	py.test --junitxml=var/reports/junit.xml tests/*
