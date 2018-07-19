# mkuuid

A small Windows tool to solve UCHEM's problem where references (in
metadata) to folders might be lost if folders are renamed.

## Installation

Download the setup wrapper here:    
https://github.com/eawag-rdm/mkuuid/raw/master/setup.exe

Click through the install procedure (defaults are ok). In case you can't
install because you don't have local admin rights on your PC, please
contact PC support or simply download the executable directly here:

https://github.com/eawag-rdm/mkuuid/raw/master/mkuuid/dist/mkuuid.exe

and put it in a convenient location.

## Usage

When you run this you are presented with a directory-chooser. Select the
directory in which you want to have the unique ID and click "OK". An
empty file with the name "uuid-<long random unique number>" will be
created there. This ID will be also in the clipboard, so you can
directly paste it into the metadata-file.
