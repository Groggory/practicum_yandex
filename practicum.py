git config --global user.name "Groggory"
git config --global user.email "kruglov.grogory.praktica@gmail.com"


https://github.com/Groggory/practicum_yandex

git remote add origin https://github.com/ваш_логин/имя_репозитория.git

git remote add origin https://github.com/Groggory/practicum_yandex.git


ssh-keygen -t ed25519 -C "kruglov.grogory.praktica@gmail.com"
(/c/Users/user/.ssh/id_ed25519): 

debug1: Offering public key: /c/Users/user/.ssh/id_ed25519 ED25519 SHA256:Lz0NrjEwOl5XrDVCCCQmHE46x+d2aTwI6l0LaSjufH8


cat ~/.ssh/id_ed25519.pub


ssh -T git@github.com
Hi Groggory/practicum_yandex! You've successfully authenticated, but GitHub does not provide shell access.

git remote add origin git@github.com:ваш_логин/имя_репозитория.git
git remote add origin git@github.com:Groggory/practicum_yandex.git