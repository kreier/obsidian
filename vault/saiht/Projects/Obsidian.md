Organizing your thoughts, ideas, projects and notes is an ongoing task for many of us. Galilei took notes of the moons of Jupiter he discovered. He was not the first to observe them, but the first to write down notes about it. And so the improved [Jupyter](https://en.wikipedia.org/wiki/Project_Jupyter) notebook format from 2011 with Python support resembles his original pursuit.
## Local vault - static version I
The vault I use is the **/content** folder inside my quartz repository. The updated content is found on [kreier.github.io/quartz](https://kreier.github.io/quartz). This is rendered each time I push a commit to the repository, running with GitHub Actions.
## Static version II at saiht.de/obsidian and [diary.saiht.de](https://diary.saiht.de)
There is also a second static version, that needs to be generated with node.js on my hp mini 400 G9 i7-13700T. The steps are:

- Create an updated static site version with `npx quartz build --serve`
- Check it on `http://localhost:8080`
- Upload the content of the `public` folder with **FileZilla**
## Update Quartz
Sometimes there are some updates in Quartz that should be included in the obsidian repository. Here are the 3 steps from the command line:

1. `npx quartz update`
2. `npx quartz sync`
3. `npx quartz build --serve`

The first checks for updates in Quartz and downloads updates to the codebase from the original source the Quartz repository was cloned from. The second makes a Github push for edits to the personalized copy with content in the **/content** folder. And the third one actually starts the quartz web server and creates the static website under **/public** and serves it at http://localhost:8080 to investigate
## Statistics of this Obsidian vault
Some first steps with Obsidian date back to [[First use of Obsidian]], but I actually started the current version in combination with Quartz 4.0 on October 27th, 2025. It was my [[Official start of my study at Su Pham and Extension of a few projects]], my first day of study - while being in Hanoi. Some local statistics is immediately available with the novel word count. I installed this one on December 13, 2025, with [[Novel Word Count and Quartz Update]] from Saigon.

- 2025/12/22 14,422 words, 54 minutes to read
- 2025/12/25 19,069 words, 1h11 to read

## Automated statistics
The Novel Word Count plugin is quite helpful when working with Obsidian, but I have a few more places where I keep my diary entries and would like to have more statistics. It is partly inspired by Github itself. It gives a nice graphical overview of the contribution frequency for a period of a year, including each day. For example, 8 years at Github look like this:

![[2025-12-25 Github statistic.png]]

Could I extend this for my diary and my whole life? The repository [statistics-diary](https://github.com/kreier/statistics-diary) does exactly that. There is still a lot of work to do. Some brainstorming and planning was done here at [[Statistics of my diary, projects and other stories]].

## Statistics for 21639 days
By the end of 2034 I will have lived 21639 days. That's a little more than 59 years, and can be visualized in 4 columns of 15 years. It would look like this:

![[2026-01-02_21639.png]]

The repository will be created.