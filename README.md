# doker削除
docker-compose down --rmi all

# doker install
docker-compose up -d

# dokcer 接続
 docker-compose exec backend /bin/bash
 
 # npm 起動
 npm run dev
 
 # pytohn 起動
 python3 srv.py -d
 
 # 初期設定
 ログイン後、
 `npm install`
 
  文字化け設定
```
 https://sweep3092.hatenablog.com/entry/2014/12/15/105515
```
 # python sql 出力
 `vi /usr/local/lib/python3.6/dist-packages/pymysql/cursors.py`
 ```
166         query = self.mogrify(query, args)
167         print(query) # print文でクエリを出力する。
168         result = self._query(query)
```

# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
