if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/KarunaTG/Tnlink /Tnlink
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Tnlink
fi
cd /Tnlink
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
