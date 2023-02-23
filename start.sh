if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Vijay14958/url-Shortner- /url-Shortner-
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /url-Shortner-
fi
cd /url-Shortner-
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
