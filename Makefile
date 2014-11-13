checksvm:
	python2.7 tests/test.py --svm

checkknn:
	python2.7 tests/test.py --knn

check: checksvm checkknn

clean:
	rm -f *.pyc src/*.pyc

reset:
	rm -f training/datas.db && echo ".table" | sqlite3 training/datas.db

distclean: clean reset
