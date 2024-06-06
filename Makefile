initialize:	
	echo "git init ..."
	git init
	sleep 1
	echo "git add to track all files"
	git add .
	echo "git commit for commiting all tracked files in the local repository"
	git commit -m "My first commit"
	echo "set up of the branch"
	git branch -M main
	echo "set up of the remote repository"
	git remote add origin https://github.com/ELFAHIM96/multi-agents_crewai.git
	git push -u origin main
push:
	echo "pushing ..."
	git add .
	git commit -m "changes"
	git push -u origin main
readme:
	@echo "Adding README.md to the repository..."
	touch README.md
	git add README.md
	git commit -m "Add README.md"
	git push -u origin main