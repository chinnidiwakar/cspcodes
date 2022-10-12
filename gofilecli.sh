#execute with zsh gofilecli.sh

userver=$(curl -s https://api.gofile.io/getServer | cut -d '"' -f 10)
read "myfile?Please Give File with Path ex /home/user/file.txt:"
curl -s -F file=@$(realpath $myfile) https://$userver.gofile.io/uploadFile | tr  ',"' '\n '| tr -d '}{'
