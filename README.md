# ARAM_tool
## 仕様技術
<img src="https://img.shields.io/badge/-Javascript-000000.svg?logo=javascript&style=for-the-badge"><img src="https://img.shields.io/badge/-Jquery-0769AD.svg?logo=jquery&style=for-the-badge"><img src="https://img.shields.io/badge/-Python-ffff00.svg?logo=python&style=for-the-badge">
## 概要
ゲーム「League of Legends」におけるカスタムゲームで、ローカルルールで遊ぶ時用のツールです。
ゲームに参加するプレイヤー全員の名前を入力して「ランダム！」ボタンを押すとチーム分けをされチャンピオンのアイコンが表示されます。
## 使い方
1. 本家ゲームLoLのアップデートが入った場合、ツールを起動する前にchampion_list.jsonの中身を更新する必要があります。scraplolwiki.pyを起動する。(リポジトリに含まれているchampion_list.jsonのバージョンは14.4)
```
python scraplolwiki.py
```
2. httpサーバを建てる。(動作確認をしたのはpythonによるhttp.server)
```windows console
python -m http.server
```
3. localhostに接続する。(http.serverのデフォルトはhttp://localhost:8000/)
## 遊び方
1. カスタムゲームで遊ぶプレイヤーを偶数人数で10人まで集めてください。
2. スライドバーを動かして人数を調整します。
3. 「ランダム！」の上にある黒い四角にプレイヤーの名前を入力します。
4. 「ランダム！」ボタンを押すと画面右側にチーム分けとチャンピオンのアイコンが表示されます。
5. ゲーム「League of Legends」クライアントから「プレイ > カスタムを作成 > ハウリングアビス」を選択しゲームタイプはブラインドピックを選択します。
6. 「確認」を押してカスタムゲームを作成します。遊ぶプレイヤーをLoLクライアントからカスタムゲームに招待します。
7. このツールの画面に表示されたチーム分けに従ってチームを移動します。
8. 「ゲーム開始」を押してゲーム開始した後、ブルーサイドのプレイヤーはツール画面のblue side側に表示されたアイコンのチャンピオンの中から、レッドサイドのプレイヤーはツール画面のred side側に表示されたアイコンのチャンピオンの中から選んでゲームをプレイしてください。
## オプション
- ミラーマッチを含める
  blue sideとred sideで同じチャンピオンが選択される可能性があります。
- メレ―限定！
  lol-wiki.jp内の表記におけるmelee区分のチャンピオンのみが選択されます。(nidalee等meleeとrenged両方を持つチャンピオンは、含まれます)
- 選択されるチャンピオンの数
  デフォルトではプレイヤーの数*2が選択されます。これはindex.html内のスクリプト内にあるSELECTING_CHAMIPON_PER_PLAYERで定義されています。この数字を変更すると、プレイヤー毎のチャンピオン数を変更することができます。
