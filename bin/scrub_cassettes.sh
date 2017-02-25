#!/bin/bash
for filename in ../tests/cassettes/*.yaml; do
	python scrub_cassettes.py < $filename > $filename.tmp
	mv $filename.tmp $filename
done
