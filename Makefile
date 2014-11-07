check:
	python2.7 tests/test.py

clean:
	rm -f *.pyc src/*.pyc

reset:
	rm -f training/datas.db && echo ".table" | sqlite3 training/datas.db

distclean: clean reset
