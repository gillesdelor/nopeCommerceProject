pytest -s -v -m "sanity" --html=./Reports/reportTestCaseSanity.html testCases/ --browser chrome
rem pytest -s -v -m "sanity or regression" --html=./Reports/reportTestCaseSanity.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/reportTestCaseSanity.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/reportTestCaseSanity.html testCases/ --browser chrome

