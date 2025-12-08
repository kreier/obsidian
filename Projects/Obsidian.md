Organizing your thoughts, ideas, projects and notes is an ongoing task for many of us. Galilei took notes of the moons of Jupiter he discovered, and the names still link back to him. He was not the first to observe them, but the first to write down notes about it. And so the improved [Jupyter](https://en.wikipedia.org/wiki/Project_Jupyter) notebook format from 2011 with Python support resembles his original pursuit.
## Local vault
The vault I use is the `content` folder inside my quartz repository. The updated content is found on [kreier.github.io/quartz](https://kreier.github.io/quartz). This is rendered each time I push a commit to the repository, running with GitHub Actions.
## Static version at saiht.de/obsidian
There is also a second static version, that needs to be generated with node.js on my hp mini 400 G9 i7-13700T. The steps are:

- Create an updated static site version with `npx quartz build --serve`
- Check it on `http://localhost:8080`
- Upload the content of the `public` folder with **FileZilla**
## Update Quartz
Sometimes there are some updates in Quartz that should be included in the obsidian repository. Here are the 3 steps:
- From command line: `npx quartz update`
- `npx quartz sync`
- `npx quartz build --serve`