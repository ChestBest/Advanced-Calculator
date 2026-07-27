This app while looking simple, has many guardrails inbuilt, for example, entering '' in the menu (empty input) defaults to addition mode, preventing program from crashing/data loss.
Another feature is that the software auto saves to the text file (logs.txt) after every mode change, allowing the user to know when the mode was changed
The program also writes "----Program Ended Successfully Here----" at the end, to confirm the program successfully ended and all the data was correctly written to it.
It also prevents numbers too large from being entered, as numbers above 1.7e+308 are considered as infinity and will cause the entire calculation to be infinity (however, it will ask if you wish to proceed
with infinity as the number - Just in case).
The entire program being in a loop allows for mode changes while program is running.
