---
created: 2023-06-10
tags:
  - projects
  - timeline
---
The idea started for me already in the 90s of the last century or millennia. But it ended with a few small sketches on paper, and the purchase of a 10m long "endless" paper roll to make a physical long version. It's one of my long term [[Projects]].
## Paper version as a book 2008
In 2008 I got "*Knaur's Zeittafel der Weltgeschichte - Den letzten 6000 Jahren auf der Spur*" with a total length of 7 meters. It is so large that it takes considerable space to open and access the information. As far as I can tell it is a German translation of [Adams Synchronological Chart or Map of History](https://en.wikipedia.org/wiki/Adams_Synchronological_Chart_or_Map_of_History) from 1871 (more than 150 years ago). In wikimedia is [a scan of 40445x4309 pixel](https://commons.wikimedia.org/wiki/File:Adams_Synchronological_Chart,_1881.jpg) of this masterpiece. And there you would find a link to the 700 Megapixel JPEG 2000 scan file. Here are links to the [two German editions](https://www.amazon.de/-/en/Alex-Klubertanz/dp/3828908519/ref=monarch_sidesheet) at [amazon.de](https://www.amazon.de/-/en/dp/3829017057/ref=monarch_sidesheet).

![Adams Chart](https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Adams_Synchronological_Chart%2C_1881.jpg/1280px-Adams_Synchronological_Chart%2C_1881.jpg)

## v1.0 First digital version in February 2009
I soon realized that the large size of the "Zeittafel" allows it to have a lot of information. But it is also its weakness - it is just too large to comprehend. Or to view at a glance. No matter how large you make it, you can't put in all the information you want. There is always something more to study, discover and integrate. So I started with a target size decision first: Three landscape A4 papers should contain the last 6000 years. This automatically also determines the resolution.

![timeline 2009](https://raw.githubusercontent.com/kreier/timeline/4.6/docs/zeitleiste2009full.png)

My first approach was a spreadsheet. And because I want it to be easily available, I chose to use OpenOffice 3.0 and the ODS format. I created the file on February 10th, 2009 with 3 tabs for the time 4050-1450 BCE, 1550 BCE - 150 CE and 150-2050 CE. All are designed to fit on a A4 paper, so these 3 pages can be glued together for a single timeline spanning 6000 years.

[![Zeitleiste 2009](https://raw.githubusercontent.com/kreier/timeline/main/docs/zeitleiste2009.png)](https://raw.githubusercontent.com/kreier/timeline/main/docs/zeitleiste2009.png)
### 4050 - 1450 BCE
For these 2600 years I chose a resolution of **10 years**. The spreadsheet has **260 columns**, but for the long periods of this time it is precise enough.

[![Zeitleiste 4050-1450](https://raw.githubusercontent.com/kreier/timeline/main/docs/zeitleiste_4050-1450.png)](https://raw.githubusercontent.com/kreier/timeline/main/docs/zeitleiste_4050-1450.png)
### 1550 BCE - 150 CE

The resolution of only 10 years makes it difficult to visualize shorter time periods like the 2 years that Pekachja ruled Israel from 780-778 BCE or the one year that Ahasja ruled Judah 907-906 BCE. The second tile therefore is divided into columns for **5 years** and needs **340 columns** for the 1700 years from 1550 BCE to 150 CE.

[![Zeitleiste 1550 BCE - 150 CE](https://raw.githubusercontent.com/kreier/timeline/main/docs/zeitleiste_1550-150.png)](https://raw.githubusercontent.com/kreier/timeline/main/docs/zeitleiste_1550-150.png)
### 130 BCE - 2050 CE

The third tile went back to 10 years per column and needs 218 columns. It was never finished.

[![Zeitleiste 130 BCE - 2050 CE](https://raw.githubusercontent.com/kreier/timeline/main/docs/zeitleiste_130-2050.png)](https://raw.githubusercontent.com/kreier/timeline/main/docs/zeitleiste_130-2050.png)
## v2.0 Creating a Vector Image with .odg in October 2015
The use of a spreadsheet really limits the possible resolution of the final product, being digital or a printed pdf. Here is a comparison of the resolution of my various approaches:

|page|begin|end|timespan|width/mm|years/mm|resolution|columns|created|
|---|---|---|---|---|---|---|---|---|
|table 1|-4050|-1450|2600|277|9.39|10|260|2009-02-10|
|table 2|-1550|150|1700|277|6.14|5|340|2009-02-10|
|table 3|-130|2050|2180|277|7.87|10|218|2009-02-10|
|drawing odg|-4000|2000|6000|1250|4.8|∞|∞|2015-12-13|
|reportlab python|-4050|2050|6100|1168|5.22|∞|∞|2023-10-17|

As next step I started to create a vector image that could be exported as pdf with the ability to zoom into details. On October 12, 2015 I started a LibreOffice 4.4 Drawing ODG with a scale of 1cm for 50 years or 5 years/millimeter, resulting in a document with the dimensions 1250x297 mm. This could be printed on my endless A4 paper roll. [Last export as pdf](https://github.com/kreier/timeline/blob/main/spreadsheet/Zeitleiste_wide_20151213.pdf) on December 13, 2015.

[![Zeitleiste 2015](https://raw.githubusercontent.com/kreier/timeline/main/docs/zeitleiste2015.png)](https://raw.githubusercontent.com/kreier/timeline/main/docs/zeitleiste2015.png)
## v1.1 Translation of v1.0 to English in June 2023

The original files from 2009 were created in German. Starting summer 2017 most of my life was going on in English. When sharing this project with friends in early June 2023 I promised to have the translated version ready until the end of month. And the translation was inded completed by June 30th, 2023.

[![timeline 2023](https://raw.githubusercontent.com/kreier/timeline/main/docs/timeline20230630.png)](https://raw.githubusercontent.com/kreier/timeline/main/docs/timeline20230630.png)

Some black/white copies were print out and shared for feedback. Yet the back of my mind was thinking of an elegant way to make v2.0 come to life.
## v3.0 Creation of an vector based version with python and reportlab in October 2023

After starting to write programs in python in 2018 and teaching it from 2022 on this looked like a good project to apply these skills. Reading values from a .csv data file would make the creation process much easier and structured. In early October 2023 I finally got reportlab working with python on both macOS and a WSL installation on Windows 11. The first step was to recreate the two pages from libreoffice with this new method. The targeted size is now 4 pages of A4 in landscape combined. This could be printed with the poster function or given to a professional printer to be released on one A0 paper and creating 4 timelines.

The current edition is v3.5. Early October I wrote "Hopefully by end of October 2023 this is done." That might be true for the initial edition, but the more you work with the document, the more ideas you get. See the growing content from v3.0 in October to v3.5 in November 2023:

[![timeline v3.0](https://github.com/kreier/timeline/raw/main/docs/timeline20231022.png)](https://github.com/kreier/timeline/blob/main/docs/timeline20231022.png) [![timeline v3.1](https://github.com/kreier/timeline/raw/main/docs/timeline20231023.png)](https://github.com/kreier/timeline/blob/main/docs/timeline20231023.png) [![timeline v3.2](https://github.com/kreier/timeline/raw/main/docs/timeline20231102.png)](https://github.com/kreier/timeline/blob/main/docs/timeline20231102.png) [![timeline v3.3](https://github.com/kreier/timeline/raw/main/docs/timeline20231104.png)](https://github.com/kreier/timeline/blob/main/docs/timeline20231104.png) [![timeline v3.4](https://github.com/kreier/timeline/raw/main/docs/timeline20231106.png)](https://github.com/kreier/timeline/blob/main/docs/timeline20231106.png) [![timeline v3.5](https://github.com/kreier/timeline/raw/main/docs/timeline20231110.png)](https://github.com/kreier/timeline/blob/main/docs/timeline20231110.png) [![timeline v3.5 updated](https://github.com/kreier/timeline/raw/main/docs/timeline20231129.png)](https://github.com/kreier/timeline/blob/main/docs/timeline20231129.png)

Since v3.4 it is also translated to German, with v3.5 a Vietnamese translation was added. And the respective translations have to be extended with each new detail added. The latest addition above includes the king of the North and South from Daniel 11.
## v4.0 Increase of version number to reflect the year in January 2024

To reflect the year of the timeline edition for at least the next 6 years I simply use the last digit of the year as the leading version indicator. In 2030 this might change to a two-digit version number, if I'm still working on this project. Here we start with v4.0 from January 2024 with extended language and script support:

[![timeline v4.0](https://github.com/kreier/timeline/raw/main/docs/timeline20240131_4.0.png)](https://github.com/kreier/timeline/blob/main/docs/timeline20240131_4.0.png) [![timeline v4.2](https://github.com/kreier/timeline/raw/main/docs/timeline20240309_4.2.png)](https://github.com/kreier/timeline/blob/main/docs/timeline20240309_4.2.png) [![timeline v4.4](https://github.com/kreier/timeline/raw/main/docs/timeline20240324_4.4.png)](https://github.com/kreier/timeline/blob/main/docs/timeline20240324_4.4.png) [![timeline v4.5](https://github.com/kreier/timeline/raw/main/docs/timeline20240413_4.5.png)](https://github.com/kreier/timeline/blob/main/docs/timeline20240413_4.5.png) [![timeline v4.6](https://github.com/kreier/timeline/raw/main/docs/timeline20240516_4.6.png)](https://github.com/kreier/timeline/blob/main/docs/timeline20240516_4.6.png)
### v4.7 Switch from reportlab to fpdf2 im May 2024

For 8 months I have been using the reportlab library in python to create the pdf files with the timeline. With a good documentation and support for utf-8 we were able to create the documents with embedded pixel and vector graphics. But by May 2024 I reached a limit of this package: the support for Text Shaping, especially the Glyph substitution is not implemented yet. The challenge is known for some time, but it requires significant manpower to implement properly. I documented my findings in [issue #35](https://github.com/kreier/timeline/issues/35). I tried other solutions like:

- [fpdf](http://www.fpdf.org/) as Free PDF in PHP on [github](https://github.com/Setasign/FPDF) since 2015, but [started in 2001 by Olivier Plathey](https://fr.wikipedia.org/wiki/FPDF) - currently at version 1.86
- [pdfkit](https://pdfkit.org/) library for Node.js in the browser, on [Github](https://github.com/foliojs/pdfkit) with 756 comits and 9600 stars, 16 releases since 2014, [latest 0.15.0](https://github.com/foliojs/pdfkit/releases/tag/v0.15.0) from March 2024
- [PyMuPDF](https://pypi.org/project/PyMuPDF/) for data extraction and more, on [Github](https://github.com/pymupdf/pymupdf) with 2399 commits and 4300 stars, 144 releases since 2015, [latest 1.24.4](https://github.com/pymupdf/PyMuPDF/releases/tag/1.24.4) from May 2024
- [weasyprint](https://weasyprint.org/) mainly to convert HTML to PDF, a professional product with good [documentation](https://doc.courtbouillon.org/weasyprint/stable/) on [Github](https://github.com/Kozea/WeasyPrint) with 5548 commits and 6700 stars, 71 releases since 2016, [latest v62.1](https://github.com/Kozea/WeasyPrint/releases/tag/v62.1) from May 2024 - yet as font subsetter Harfbuzz is [currently experimental](https://github.com/Kozea/WeasyPrint/issues/2120)
- [iText Core](https://itextpdf.com/products/itext-core) with [pdfCalligraph](https://itextpdf.com/products/pdfcalligraph) as add-on for fonts like Arabic, Hebrew or Khmer, in Java; on [Github](https://github.com/itext/itext-java) with 6246 commits and 1900 stars, 41 releases since 2016, latest [8.0.4 Community](https://github.com/itext/itext-java/releases/tag/8.0.4) from April 2024
- [reportlab](https://www.reportlab.com/) with [sourcecode](https://hg.reportlab.com/hg-public/reportlab) mirrored [on Github](https://github.com/MrBitBucket/reportlab-mirror) - all the way back to 2000 with version 0.85, 2.0 in 2006, 3.0 in 2014 and currently at 4.2.1

Interestingly, fpdf2 itself is a fork from PyPDF from [reingart/pypdf](https://github.com/reingart/pyfpdf) 2016, itself being a fork of the [fpdf](http://www.fpdf.org/) library by Max Pat in 2006. See a [little history](https://py-pdf.github.io/fpdf2/History.html). The [release history](https://pypi.org/project/fpdf2/#history) indicates that [Text Shaping](https://py-pdf.github.io/fpdf2/TextShaping.html) was only introduced with 2.7.5 in August 2023. Now with 1479 commits and 969 stars, 33 releases since 2021, the latest being [2.7.9](https://github.com/py-pdf/fpdf2/releases/tag/2.7.9) from May 2024.

## v5.1 with more history from January 2025

I have to describe some of the changes here.

## v6.01 Extends family trees from Terah, Noah and Cain in January 2026

The family tree from Terah was already included in 2024. In 2025 it was extended to Noah to have 20 nations related to their origin or later offspring. With the new January edition of 2026, labeled v6.01 (in a system year.month) this also includes the known part of Cain's family. There is little known of the people before the Great Deluge.
## New start with python and pdf in 2023

![2023-1](https://raw.githubusercontent.com/kreier/timeline/main/docs/timeline20231023.png)

After a few days of work, spanned over a few months, it had grown to something with a lot more information than previous editions:

![2023-2](https://raw.githubusercontent.com/kreier/timeline/main/docs/timeline20231129.png)