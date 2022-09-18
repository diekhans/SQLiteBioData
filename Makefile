ROOT = .
include ${ROOT}/defs.mk

pyprogs = $(shell file -F $$'\t' bin/* tests/bin/* | awk '/Python script/{print $$1}')

lint:
	${FLAKE8} --color=never ${pyprogs} lib/sqlitebiodata/*.py

test:
	cd tests && ${MAKE} test

clean:
	cd tests && ${MAKE} clean
	rm -rf ${binDir}/__pycache__ ${libDir}/__pycache__
