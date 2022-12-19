if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/IamEasyIce/Priyanka /Priyanka
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Priyanka
fi
cd /Priyanka
pip3 install -U -r requirements.txt
echo "Starting Priyanka...."
python3 bot.py
