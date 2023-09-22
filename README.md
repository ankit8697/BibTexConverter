# Introduction

This program is used to convert BibTeX and HeinOnline citations to a Literature Review Mapping used for research in many fields.
There are two programs in this project. `heinonline.py` is used to read through text files taken from [HeinOnline](https://heinonline.org/HOL/Welcome),
which is a platform that aggregates research documents, and `jstor.py` does the same thing with BibTeX files imported from [JSTOR](https://www.jstor.org/).

# How to Use

## Clone the GitHub repo

The first thing you need to do is either clone or download the code from GitHub. We don't have a web platform or anything yet, but if you feel like contributing
then feel free to create an issue and send a pull request! Also you'll need to install all the python dependencies found in `requirements.txt`.

## HeinOnline

To use the HeinOnline script, first go to HeinOnline and select any research documents you would like. Then choose to export them via email. Add your email address
and HeinOnline should send you an email with information on each source you selected. Now copy the contents of that email excluding the very first line that says
`The following documents have been sent to you:`. Make sure you remove this line otherwise the program won't work (if you think that's annoying, feel free to send a fix!).
Now add the contents to a text file in the same directory as the rest of the code. Update the `FILE_NAME` variable with the name of the text file. Then run the `heinonline.py` file.
This should generate an Excel spreadsheet of the same name as your text file, as well as download all the PDFs via the download links found on HeinOnline in a folder named after your
text file. Each PDF is given the name of the article taken from HeinOnline.

## JSTOR

To use the JSTOR script, it's similar to HeinOnline but a lot simpler. Choose the documents you want on JSTOR, then export it as a BibTex file. Add the BibTeX file to the project directory,
update the `FILE_NAME` variable with the path to the BibTeX file to `jstor.py`, and run the program. This will create the Excel file in the same way.

One caveat here is the file downloads. Since JSTOR is protected by an authentication layer, the process to get the files is a bit more involved. You need to complete the authentication to JSTOR
via your university/company/account. Once you have that, paste in your cookies to the program and run it. When obtaining your cookies, make sure you're in an incognito window so that you don't
accidentally share unrelated cookies. Note that the URL is currently only setup to work with Jindal as the university. If you work with a different organization and wish to use the download files
feature, open an issue on GitHub and I'll see what I can do. Alternatively, feel free to contribute to this project and send me a pull request!

*Note:* Please protect your cookies at every possible step. Make sure to only use the cookies required by JSTOR and nothing else. Your cookies are tied to your online identity for a given website
and if someone gets a hold of your cookies, they can impersonate you online. Never share your cookies publicly and keep them protected. (Also if someone can find a way to download the files without
relying on cookies, send me a pull request!)

As with HeinOnline, the Excel sheet will be named the same as the BibTeX file name. Make sure to double check the citations if you find it to your liking, since this is dynamically generated from
existing data and not pre-formatted. It might be missing a comma here and there.

# Contributing

To contribute to this project, clone the repo, install the python dependencies, and run either of the programs. Please first make an issue on the repo describing the feature request or bug. The more detailed
it is, the easier it will be to add/fix. Also, I *HIGHLY* encourage you to try to contribute to this project! I welcome any and all pull requests, whether it's updating documentation or adding a web server.
A few potential features that would be helpful to add would be:

- A web interface for either of these files so that you don't need to be technically literate to use them. Most likely via a simple Flask server.
- Refactor the files to take CLI flags to toggle required features.
- Figure out a way to get JSTOR file downloads working without relying on copying over auth cookies.
- Parallelize the downloads to make it more efficient.
- Any bug fixes or feature requests. If you really really want something and don't want to wait, feel free to add it yourself!
- Improve the documentation here!
