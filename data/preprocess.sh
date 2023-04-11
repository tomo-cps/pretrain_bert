FILE=$1
if [ $# -ne 1 ]; then
  echo "Usage: ./preprocess.sh INPUT_TEXT"
  exit 1
fi
echo "Processing ${FILE}"
sed -i -e '/<doc id/,+1d; s/<\/doc>//g' ${FILE}
sed -i -e 's/ *$//g; s/。\([^」|)|）|"]\)/。\n\1/g; s/^[ ]*//g' ${FILE}
sed -i -e '/^。/d' ${FILE}