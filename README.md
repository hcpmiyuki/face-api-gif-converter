# face-api-gif-converter
## 流れ(ディレクトリやパス関連は以下の通りじゃなくてもいい. 例として用意しただけ)
1. 環境構築
2. APIキーを設定
3. videosに変換元の動画をおく(といいと思う)
4. convert_video_into_image.pyで動画を画像に変換し,imagesに保存する(といいと思う)
5. create_gif.pyでimagesに入っている画像を感情分析して,結果をgifsに保存する(といいと思う)

## venvでの環境構築
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## APIキーの設定
- .env.sampleの<API_KEY>にFace APIのキーを入れて, .envというファイル名に変更する

## convert_video_into_image.py
- 動画を細かい画像に分割するためのファイル. 動画を再生しながらキーボード押下で保存するようにしている. 
- 参考:[これの最後](https://note.nkmk.me/python-opencv-video-to-still-image/)
- 定数の説明
  1. VIDEO_PATHに変換したい動画のパスを指定する
  2. RESULT_PATHに変換後の画像を入れるディレクトリのパスを指定する
  3. BASE_NAMEに変換後の画像の名前を指定する.(画像は複数生成されるので, 生成された順の番号がBASE_NAMEに追加される)
## create_gif.py
- 分割した画像をAPIに投げてその結果をgifにする
- 参考:gifにする方法は[これ](https://cpp-learning.com/python-gif/)
- 参考:opencvは[これ](https://qiita.com/G-awa/items/477f2324552cb908ecd0)
- 参考face apiの使い方は[これ](https://www.pc-koubou.jp/magazine/27499)
- 定数の説明
  1. IMG_DIR_PATHに画像が入っているディレクトリのパスを指定する
  2. SAVE_FILE_PATHにできたgifのファイルパスを指定する


