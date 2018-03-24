# Crawling-Wiktionary

[Intro] This is a simplified parser and crawler used to download words from Wiktionary, and write them into json files for further education/research uses.

[Usage] 
1. List the words you want to download alphabetally in a txt file. A sample is ./words_alpha.txt. I downloaded this file from https://github.com/dwyl/english-words.
2. Divide the list against their first letters, using command "list_divider.py -divAB words_alpha.txt" for example.
Then individual files will be in their folders, e.g., ./word_list/a/a.txt
3. I recommand you keep a single file smaller than 100KB because all words are written into memory first when being downloaded. Therefore keeping the file small reduces the possibility of data losing before written into outer storages.
For example, if you have a single file "a.txt" whose size is near 400KB, use "list_divider.py -divBig a.txt 4", then you can get
"a1.txt","a2.txt","a3.txt", and "a4.txt". Each of them has a size near 100KB. Finally, put the four smaller files into ./word_list/a/
4. Use command "wiktcrl.py -download a" for example, which will download all the words listed in the files belonged to folder "./word_list/a/", from Wiktionary. Moreover, the outputs will be in the folders "./word_dict/a/", saved as "a1.json","a2.json","a3.json", and "a4.json".
5. Additionally, you can test the Wiktionary web API by using command like "wiktcrl.py -lookup bicep", to get the definition from Wiktionary.

[Copyright] The copyright of the sample word list belongs to the creator of repository https://github.com/dwyl/english-words. The copyright of the word definitions belongs to Wiktionary https://www.wiktionary.org/. Follow CC-BY-SA / the GFDL. CC-BY-SA required by Wiktionary if you want to use this repository for your education or/and research purposes.

[Contact me] mailto:jc-shen@ist.osaka-u.ac.jp
