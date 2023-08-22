if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/VJBots/Advance-Auto-Filter /Advance-Auto-Filter
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Advance-Auto-Filter
fi
cd /Advance-Auto-Filter
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
