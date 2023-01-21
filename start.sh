if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Vijay14958/url-Shortner-3 /url-Shortner-3
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /url-Shortner-3
fi
cd /url-Shortner-3
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
