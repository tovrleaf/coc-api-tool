#!/usr/bin/env bash

cd "$(dirname $0)/.."

 pytest --cov-report html:htmlcov --cov apiclient tests/
