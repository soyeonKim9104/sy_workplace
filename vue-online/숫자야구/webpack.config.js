//webpack node환경이라서 외부 경로를 require로 불러온다.

const VueLoaderPlugin = require('vue-loader/lib/plugin');
const path = require('path');

module.exports = {
    mode:'development',
    devtool:'eval',
    resolve:{
        extensions:['.js','.vue'], // import나 require 확장자명을 생략할 수 있다.
    },
    entry:{
        app:path.join(__dirname, 'main.js'), //app 은 파일이름 
    },
    module:{
        rules:[{
            test:/\.vue$/,
            loader:'vue-loader',   
        }],
    },
    plugins:[
        new VueLoaderPlugin(),
    ],
    output:{ //npm run build 를 하게 되면 dist 파일에 app.js 가 생성된다
        filename:'[name].js', //app.js 와 동일 [name] = app/ entry에 적은 파일 이름을 변경해도 되는 [name] 으로 지정하면 좋다
        path:path.join(__dirname, 'dist'), //__dirname = 현재폴더 라는 뜻
    },
};