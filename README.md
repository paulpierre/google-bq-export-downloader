![logo](https://seeklogo.com/images/G/google-big-query-logo-AC63E7C329-seeklogo.com.png)
# Exported CSV Downloader
### by [@paulpierre](https://www.paulpierre/?ref=github)
---

### Who is google-bq-export-downloader.py for?
When exporting a massive amount of data, like a year's worth of analytics from Big Query, GCP will drop your files serialized into a storage bucket. Depending on usage, this could mean thousands of files. This script allows you download those files on autopilot

### How to use it?
* The remote file path syntax is the following: https://storage.googleapis.com/[folder]/[prefix]_export/[prefix]_[year]_[month]_[serialization].csv.gz
* In the python file, set the following variables:
    * **folder** - just set the name of the folder path in your bucket storage
    * **prefix** - set the prefix of your exported name scheme
    * **start_month** - the month you want to start counting up from
    * **start_year** - the month you want to start counting up from
    * optionally you can set a different variable on line 58 **while not _year > 2019:** to modify what year to end in the loop
* Run: python google-bq-export-downloader.py

### Features
* **Stop/Resume** Skips files that exist in the current director so you can stop / resume downloading
* **Smart serialization** Will skip, continue and reset serialization if files don't exist in the remote path
* **Month/Year serialization** Properly increments month and year

Note: If you found this useful, throw a star my way. This is as-is, I wrote and debugged this in 30 minutes and threw it up as soon as I had it running so it's not refactored nor clean.. but hey, I threw colors in so stfu<3 :)



### MIT License
- - -

Copyright (c) 2019 Paul Pierre

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in allcopies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
