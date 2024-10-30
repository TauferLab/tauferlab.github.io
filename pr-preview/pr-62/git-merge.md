# Merge branch to master
git checkout SOMOSPIE-scratch
git pull origin SOMOSPIE-scratch
git checkout master
git merge SOMOSPIE-scratch
git add --all
git commit -m "Merge SOMOSPIE branch to master"
git push origin master

