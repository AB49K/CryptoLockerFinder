# CryptoLockerFinder
A script that will find encrypted files on a network as a result of a CryptoLocker infection


Fortunately, the malware creators don't seem to want to encrypt the same file twice so they have a magic string, I've written a tool that searches every file on your server and any connected shared drive.
First you have to find the Magic string - It'll usually be at the top of the file. like these:

http://i.imgur.com/HLruMkF.png
 
http://i.imgur.com/hTzgGva.png 

Then change StringMatch in the script and fire it up.