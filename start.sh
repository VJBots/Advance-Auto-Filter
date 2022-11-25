if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/KarunaTG/Easysky2 /Easysky2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Easysky2
fi
cd /Easysky2
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
